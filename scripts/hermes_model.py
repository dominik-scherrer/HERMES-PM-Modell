"""Gemeinsame Ladefunktionen für das HERMES-Modell (model/hermes.yaml)."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
MODEL = ROOT / "model" / "hermes.yaml"

def load(path=MODEL):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def index(model):
    """Liefert Hilfsstrukturen: Ergebnisse nach ID, Phasenreihenfolge, Abhängige."""
    erg = {e["id"]: e for e in model["ergebnisse"]}
    phasen = [p["id"] for p in model["phasen"]]
    deps = {i: [] for i in erg}
    for e in model["ergebnisse"]:
        for v in e.get("voraussetzungen", []):
            if v["id"] in deps:
                deps[v["id"]].append(e["id"])
    return erg, phasen, deps

def phase_rank(model, phase, rolle):
    """Zeitlicher Rang einer Phase. Phasenunabhängige Ergebnisse liefern ab Konzept und lesen alles."""
    seq = [p["id"] for p in model["phasen"] if p["id"] != "phasenunabhaengig"]
    if phase == "phasenunabhaengig":
        return 1 if rolle == "liefert" else 99
    return seq.index(phase)

def wissen(e, art):
    return (e.get("wissen") or {}).get(art, [])
