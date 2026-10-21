# Stufe 1: Modell prüfen. Ist hermes.yaml fehlerhaft, bricht der Build ab
# und Coolify lässt die laufende Version stehen.
FROM python:3.12-slim AS check
WORKDIR /repo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model ./model
COPY scripts ./scripts
RUN python scripts/validate.py

# Stufe 2: Explorer und Modell statisch ausliefern
FROM nginx:1.27-alpine
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY explorer/index.html /usr/share/nginx/html/index.html
COPY --from=check /repo/model/hermes.yaml /usr/share/nginx/html/hermes.yaml
EXPOSE 80
HEALTHCHECK CMD wget -qO- http://127.0.0.1/healthz || exit 1
