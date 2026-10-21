"""Prüft model/hermes.yaml auf Konsistenz. Exit-Code 1 bei Fehlern.

Aufruf: python scripts/validate.py
"""
import sys
from hermes_model import load, index, wissen

def main():
    m = load()
    err, warn = [], []
    erg, phasen, deps = index(m)
    ids = [e["id"] for e in m["ergebnisse"]]
    for i in {x for x in ids if ids.count(x) > 1}:
        err.append(f"Doppelte Ergebnis-ID: {i}")
    module = {x["id"] for x in m["module"]}
    szen = {x["id"] for x in m["szenarien"]}
    wobj = {x["id"] for x in m["wissensobjekte"]}
    status = set(m.get("pipeline_status", {}))
    for mo in m["module"]:
        for s in mo["szenarien"]:
            if s not in szen:
                err.append(f"Modul {mo['id']}: unbekanntes Szenario {s}")
    for e in m["ergebnisse"]:
        p = f"Ergebnis {e.get('id')}"
        for k in ("id", "name", "typ", "phase", "module"):
            if k not in e:
                err.append(f"{p}: Pflichtfeld «{k}» fehlt")
        if e.get("typ") not in ("dokument", "zustand"):
            err.append(f"{p}: typ muss dokument oder zustand sein")
        if e.get("typ") == "dokument":
            if e.get("herkunft") not in ("hermes", "vorlage", "csi"):
                err.append(f"{p}: herkunft muss hermes, vorlage oder csi sein")
            if not e.get("zweck"):
                err.append(f"{p}: zweck fehlt")
        if e.get("phase") not in phasen:
            err.append(f"{p}: unbekannte Phase {e.get('phase')}")
        for mo in e.get("module", []):
            if mo not in module:
                err.append(f"{p}: unbekanntes Modul {mo}")
        if e.get("nur_vorgehen") not in (None, "klassisch", "agil"):
            err.append(f"{p}: nur_vorgehen muss klassisch oder agil sein")
        if e.get("pipeline_status") and e["pipeline_status"] not in status:
            err.append(f"{p}: unbekannter pipeline_status {e['pipeline_status']}")
        if e.get("abgedeckt_durch") and e["abgedeckt_durch"] not in erg:
            err.append(f"{p}: abgedeckt_durch verweist auf unbekanntes Ergebnis {e['abgedeckt_durch']}")
        for art in ("schreibt", "ergaenzt", "liest"):
            for f in wissen(e, art):
                if f not in wobj:
                    err.append(f"{p}: unbekanntes Wissensobjekt {f} in wissen.{art}")
        for v in e.get("voraussetzungen", []):
            if v.get("id") not in erg:
                err.append(f"{p}: Voraussetzung {v.get('id')} existiert nicht")
            if v.get("basis") not in ("phasenmodell", "pipeline"):
                err.append(f"{p}: Voraussetzung {v.get('id')} braucht basis phasenmodell oder pipeline")
    for t in m.get("phasentore", []):
        if t["ergebnis"] not in erg:
            err.append(f"Phasentor {t['entscheid']}: Ergebnis {t['ergebnis']} existiert nicht")
        if t["gilt_ab"] not in phasen:
            err.append(f"Phasentor {t['entscheid']}: unbekannte Phase {t['gilt_ab']}")
    # Zyklen in den Voraussetzungen
    state = {}
    def visit(i, path):
        state[i] = 1
        for v in erg[i].get("voraussetzungen", []):
            j = v["id"]
            if j not in erg:
                continue
            if state.get(j) == 1:
                err.append("Zyklus: " + " → ".join(path + [j]))
            elif not state.get(j):
                visit(j, path + [j])
        state[i] = 2
    for i in erg:
        if not state.get(i):
            visit(i, [i])
    # Hinweise: Wissensobjekte ohne Quelle oder ohne Abnehmer
    for f in sorted(wobj):
        w = [e for e in m["ergebnisse"] if f in wissen(e, "schreibt")]
        r = [e for e in m["ergebnisse"] if f in wissen(e, "liest") or f in wissen(e, "ergaenzt")]
        if not w and r:
            warn.append(f"Wissensobjekt {f}: wird verwendet, aber von keinem Ergebnis erzeugt")
        if w and not r:
            warn.append(f"Wissensobjekt {f}: wird erzeugt, aber nirgends weiterverwendet")
    for x in warn:
        print("Hinweis:", x)
    for x in err:
        print("Fehler: ", x)
    n_doc = sum(1 for e in m["ergebnisse"] if e.get("typ") == "dokument")
    print(f"{len(err)} Fehler, {len(warn)} Hinweise · {n_doc} Dokumente, {len(m['ergebnisse']) - n_doc} Zustände, {len(wobj)} Wissensobjekte")
    return 1 if err else 0

if __name__ == "__main__":
    sys.exit(main())
