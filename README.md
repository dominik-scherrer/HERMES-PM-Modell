# HERMES-Modell

Maschinenlesbares Modell der HERMES-2022-Ergebnisse für CSI. Eine Datei, zwei Verwendungen:

- **HERMES Explorer** (`explorer/index.html`): interaktive Ansicht von Ergebnissen, Abhängigkeiten und Wissensflüssen
- **HERMES-Skill** (`skill/hermes/references/`): Referenzdateien pro Dokument, aus dem Modell generiert

## Struktur

```
model/hermes.yaml                 einzige Quelle, wird von Hand gepflegt
explorer/index.html               Oberfläche, lädt ../model/hermes.yaml
scripts/validate.py               prüft das Modell (IDs, Verweise, Zyklen)
scripts/build_skill_refs.py       erzeugt skill/hermes/references/
skill/hermes/references/          generiert, nicht von Hand bearbeiten
.github/workflows/model.yml       prüft bei jedem Push Modell und Aktualität der Referenzen
```

## Arbeitsablauf

```bash
pip install -r requirements.txt
# model/hermes.yaml bearbeiten
python scripts/validate.py
python scripts/build_skill_refs.py
git add model skill && git commit -m "Modell: …"
```

## Explorer lokal öffnen

Browser blockieren das Laden der YAML-Datei bei Doppelklick auf die HTML-Datei. Deshalb im Repo-Ordner einen lokalen Server starten:

```bash
python -m http.server 8000
# http://localhost:8000/explorer/
```

Der Explorer sucht das Modell zuerst als `hermes.yaml` neben der Seite, dann unter `../model/hermes.yaml`. Für eine Veröffentlichung genügt es, `index.html` und `hermes.yaml` nebeneinander abzulegen. Die YAML-Bibliothek (js-yaml 4.1.0) wird von cdnjs geladen.

## Schema von `model/hermes.yaml`

Oberste Ebene: `phasen`, `agil`, `szenarien`, `module` (mit den Szenarien, in denen sie vorkommen), `phasentore`, `pipeline_status`, `wissensobjekte`, `ergebnisse`, `quellen`.

Felder eines Ergebnisses:

| Feld | Pflicht | Inhalt |
|---|---|---|
| `id` | ja | eindeutig, Kleinbuchstaben und `_`; zugleich Dateiname der Skill-Referenz |
| `name` | ja | offizieller Name |
| `kurz` | | Kürzel, z. B. PIA |
| `typ` | ja | `dokument` oder `zustand` |
| `herkunft` | bei Dokumenten | `hermes`, `vorlage` (HERMES-Vorlage ausserhalb des Phasenmodells) oder `csi` (CSI-Erweiterung) |
| `phase` | ja | ID aus `phasen` |
| `module` | ja | Liste von IDs aus `module`; bestimmt die Szenarien |
| `nur_vorgehen` | | `klassisch` oder `agil` |
| `entscheid` | | HERMES-Entscheid, für den das Ergebnis die Grundlage ist |
| `pipeline_status` | | Schlüssel aus `pipeline_status` |
| `zweck` | bei Dokumenten | Kurzbeschrieb |
| `zweck_quelle` | | `referenz` oder `sinngemaess` |
| `abgedeckt_durch` | | bei CSI-Erweiterungen: HERMES-Ergebnis, das den Inhalt abdeckt |
| `hinweis` | | freier Hinweis |
| `gliederung` | | Kapitel gemäss HERMES-Inhaltsvorlage |
| `wissen` | | `schreibt`, `ergaenzt`, `liest`: Listen von IDs aus `wissensobjekte` |
| `voraussetzungen` | | Liste von `{id, basis}`; `basis` ist `phasenmodell` oder `pipeline` |

Phasentore (z. B. Durchführungsfreigabe) gelten automatisch für alle Ergebnisse ab der Phase `gilt_ab` und werden nicht als Voraussetzung eingetragen.

## Einbindung in den HERMES-Skill

`scripts/build_skill_refs.py` schreibt:

- `references/ergebnisse-index.md`: alle Ergebnisse nach Phase mit Modulen, Entscheiden und Voraussetzungen
- `references/wissensobjekte.md`: wer welches Wissensobjekt erzeugt, ergänzt und liest
- `references/dokumente/<id>.md`: je Dokument Zweck, Gliederung, Voraussetzungen, Folgeergebnisse, Wissensspeicher und Wiederverwendungshinweise

Die `SKILL.md` des HERMES-Skills bleibt von Hand gepflegt und verweist auf diese Dateien. Beim Paketieren den Ordner `skill/hermes/references/` neben die `SKILL.md` legen.

## Auf Coolify bereitstellen

Das `Dockerfile` im Repo-Root prüft zuerst das Modell mit `scripts/validate.py` und liefert danach `explorer/index.html` und `model/hermes.yaml` mit nginx nebeneinander aus. Ein fehlerhaftes Modell lässt den Build scheitern; die laufende Version bleibt dann online.

In Coolify:

1. Neue Ressource → Repository (GitHub App oder Deploy Key) → Branch wählen
2. Build Pack: **Dockerfile**, Pfad `/Dockerfile`, Port **80**
3. Domain eintragen, Healthcheck-Pfad `/healthz`
4. Automatisches Deployment bei Push aktivieren

Jede Änderung an `model/hermes.yaml` ist damit nach dem Push ohne weiteren Schritt im Explorer sichtbar.
