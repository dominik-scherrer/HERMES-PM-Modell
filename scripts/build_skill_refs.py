"""Erzeugt die Referenzdateien des HERMES-Skills aus model/hermes.yaml.

Ausgabe (wird bei jedem Lauf vollständig neu geschrieben):
  skill/hermes/references/ergebnisse-index.md     Übersicht aller Ergebnisse nach Phase
  skill/hermes/references/wissensobjekte.md       wer welches Wissensobjekt erzeugt, ergänzt, liest
  skill/hermes/references/dokumente/<id>.md       eine Datei pro Dokument

Aufruf: python scripts/build_skill_refs.py
"""
import shutil
from hermes_model import ROOT, load, index, phase_rank, wissen

OUT = ROOT / "skill" / "hermes" / "references"
HEAD = "<!-- Generiert aus model/hermes.yaml mit scripts/build_skill_refs.py. Nicht von Hand bearbeiten. -->\n\n"
HERKUNFT = {"hermes": "HERMES-Ergebnis", "vorlage": "HERMES-Vorlage (nicht im Phasenmodell)", "csi": "CSI-Erweiterung (kein HERMES-Ergebnis)"}
BASIS = {"phasenmodell": "HERMES-Phasenmodell", "pipeline": "Pipeline-Annahme"}

def main():
    m = load()
    erg, phasen, deps = index(m)
    pname = {p["id"]: p["name"] for p in m["phasen"]}
    mname = {x["id"]: x["name"] for x in m["module"]}
    wname = {x["id"]: x["name"] for x in m["wissensobjekte"]}
    sname = {x["id"]: x["name"] for x in m["szenarien"]}
    mod_sz = {x["id"]: x["szenarien"] for x in m["module"]}
    docs = [e for e in m["ergebnisse"] if e["typ"] == "dokument"]

    def tore(e):
        out = []
        for t in m.get("phasentore", []):
            if t["ergebnis"] == e["id"]:
                continue
            if t["gilt_ab"] == "initialisierung" or (e["phase"] != "phasenunabhaengig" and phasen.index(e["phase"]) >= phasen.index(t["gilt_ab"])):
                out.append(t)
        return out

    def quellen(e):
        need = set(wissen(e, "liest") + wissen(e, "ergaenzt"))
        res = []
        for x in docs:
            if x["id"] == e["id"] or phase_rank(m, x["phase"], "liefert") > phase_rank(m, e["phase"], "liest"):
                continue
            f = [k for k in wissen(x, "schreibt") + wissen(x, "ergaenzt") if k in need]
            if f:
                res.append((x, sorted(set(f), key=f.index)))
        return res

    def abnehmer(e):
        give = set(wissen(e, "schreibt") + wissen(e, "ergaenzt"))
        res = []
        for x in docs:
            if x["id"] == e["id"] or phase_rank(m, x["phase"], "liest") < phase_rank(m, e["phase"], "liefert"):
                continue
            f = [k for k in wissen(x, "liest") + wissen(x, "ergaenzt") if k in give]
            if f:
                res.append((x, sorted(set(f), key=f.index)))
        return res

    def szenarien(e):
        s = sorted({z for mo in e["module"] for z in mod_sz[mo]}, key=list(sname).index)
        return "alle" if len(s) == len(sname) else ", ".join(sname[z] for z in s)

    def title(e):
        return e["name"] + (f" ({e['kurz']})" if e.get("kurz") else "")

    if (OUT / "dokumente").exists():
        shutil.rmtree(OUT / "dokumente")
    (OUT / "dokumente").mkdir(parents=True)

    for e in docs:
        L = [HEAD + f"# {title(e)}\n"]
        L.append(f"- **Phase:** {pname[e['phase']]}")
        L.append(f"- **Module:** {', '.join(mname[x] for x in e['module'])}")
        L.append(f"- **Szenarien:** {szenarien(e)}")
        L.append(f"- **Art:** {HERKUNFT[e['herkunft']]}")
        if e.get("nur_vorgehen"):
            L.append(f"- **Nur bei Vorgehen:** {e['nur_vorgehen']}")
        if e.get("entscheid"):
            L.append(f"- **Grundlage für Entscheid:** {e['entscheid']}")
        if e.get("pipeline_status"):
            L.append(f"- **Status in der Generierungspipeline:** {m['pipeline_status'][e['pipeline_status']]}")
        L.append("\n## Zweck\n")
        L.append(e["zweck"] + ("" if e.get("zweck_quelle", "referenz") == "referenz" or e["herkunft"] != "hermes" else "\n\n_Sinngemässer Kurzbeschrieb, nicht aus der Referenz übernommen._"))
        if e.get("abgedeckt_durch"):
            L.append(f"\nIn HERMES abgedeckt durch: {erg[e['abgedeckt_durch']]['name']}.")
        if e.get("hinweis"):
            L.append(f"\n> {e['hinweis']}")
        L.append("\n## Gliederung\n")
        if e.get("gliederung"):
            L += [f"{i}. {s}" for i, s in enumerate(e["gliederung"], 1)]
        else:
            L.append("_In der Referenz nicht hinterlegt. Im HERMES-Handbuch prüfen._" if e["herkunft"] != "csi" else "_Keine HERMES-Vorlage. Gliederung projektspezifisch festlegen._")
        L.append("\n## Voraussetzungen\n")
        vs = e.get("voraussetzungen", [])
        L += [f"- {erg[v['id']]['name']} ({BASIS[v['basis']]})" for v in vs]
        L += [f"- Phasentor: {t['entscheid']} ({erg[t['ergebnis']]['name']})" for t in tore(e)]
        if not vs and not tore(e):
            L.append("- Keine. Einstiegspunkt des Projekts.")
        fol = deps[e["id"]]
        L.append("\n## Folgeergebnisse\n")
        L += [f"- {erg[i]['name']}" + (" (Zustand)" if erg[i]["typ"] == "zustand" else "") for i in fol] or ["- Keine direkten Folgeergebnisse."]
        L.append("\n## Wissensspeicher\n")
        L.append("| Rolle | Wissensobjekte |\n|---|---|")
        for art, lab in (("schreibt", "erzeugt"), ("ergaenzt", "ergänzt"), ("liest", "liest")):
            L.append(f"| {lab} | {', '.join(wname[f] for f in wissen(e, art)) or '–'} |")
        L.append("\n## Wiederverwendung\n")
        L.append("Vor dem Erstellen diese Ergebnisse auswerten, statt die Informationen neu zu erfragen:\n")
        q = quellen(e)
        L += [f"- **{x['name']}:** {', '.join(wname[f] for f in fs)}" for x, fs in q] or ["- Keine Vorgängerergebnisse mit passendem Wissen."]
        a = abnehmer(e)
        if a:
            L.append("\nDieses Dokument liefert Wissen an:\n")
            L += [f"- **{x['name']}:** {', '.join(wname[f] for f in fs)}" for x, fs in a]
        (OUT / "dokumente" / f"{e['id']}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # Index
    L = [HEAD + "# HERMES-Ergebnisse — Index\n", "Eine Zeile pro Ergebnis. Details je Dokument unter `dokumente/<id>.md`.\n"]
    for p in m["phasen"]:
        es = [e for e in m["ergebnisse"] if e["phase"] == p["id"]]
        if not es:
            continue
        L.append(f"\n## {p['name']}\n")
        L.append("| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |\n|---|---|---|---|---|---|")
        for e in es:
            typ = "Zustand" if e["typ"] == "zustand" else {"hermes": "Dokument", "vorlage": "Vorlage", "csi": "CSI-Erweiterung"}[e["herkunft"]]
            vor = ", ".join(erg[v["id"]]["name"] + ("*" if v["basis"] == "pipeline" else "") for v in e.get("voraussetzungen", [])) or "–"
            datei = f"`dokumente/{e['id']}.md`" if e["typ"] == "dokument" else "–"
            L.append(f"| {title(e)} | {typ} | {', '.join(mname[x] for x in e['module'])} | {e.get('entscheid', '–')} | {vor} | {datei} |")
    L.append("\n\\* Pipeline-Annahme, nicht Teil des HERMES-Phasenmodells.")
    (OUT / "ergebnisse-index.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # Wissensobjekte
    L = [HEAD + "# Wissensobjekte — wer erzeugt, ergänzt und liest was\n"]
    for g in dict.fromkeys(x["gruppe"] for x in m["wissensobjekte"]):
        L.append(f"\n## {g}\n")
        L.append("| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |\n|---|---|---|---|---|")
        for w in [x for x in m["wissensobjekte"] if x["gruppe"] == g]:
            col = lambda art: ", ".join(e["name"] for e in docs if w["id"] in wissen(e, art)) or "–"
            L.append(f"| {w['name']}{' (Querschnitt)' if w.get('querschnitt') else ''} | `{w['id']}` | {col('schreibt')} | {col('ergaenzt')} | {col('liest')} |")
    (OUT / "wissensobjekte.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{len(docs)} Dokumentreferenzen, Index und Wissensobjekte geschrieben nach {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
