<!-- Generiert aus model/hermes.yaml mit scripts/build_skill_refs.py. Nicht von Hand bearbeiten. -->

# HERMES-Ergebnisse — Index

Eine Zeile pro Ergebnis. Details je Dokument unter `dokumente/<id>.md`.


## Initialisierung

| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |
|---|---|---|---|---|---|
| Projektinitialisierungsauftrag (PIA) | Dokument | Projektsteuerung · Projektführung | Projektinitialisierungsfreigabe | – | `dokumente/projektinitialisierungsauftrag.md` |
| Stakeholderliste | Dokument | Projektsteuerung · Projektführung | – | Projektinitialisierungsauftrag | `dokumente/stakeholderliste.md` |
| Rechtsgrundlagenanalyse | Dokument | Projektgrundlagen | – | Stakeholderliste | `dokumente/rechtsgrundlagenanalyse.md` |
| Studie | Dokument | Projektgrundlagen | Weiteres Vorgehen | Stakeholderliste, Rechtsgrundlagenanalyse, Schutzbedarfsanalyse | `dokumente/studie.md` |
| Schutzbedarfsanalyse | Dokument | Projektgrundlagen | – | Stakeholderliste | `dokumente/schutzbedarfsanalyse.md` |
| Beschaffungsanalyse | Dokument | Projektgrundlagen | – | Stakeholderliste | `dokumente/beschaffungsanalyse.md` |
| Projektmanagementplan | Dokument | Projektsteuerung · Projektführung | – | Studie, Beschaffungsanalyse | `dokumente/projektmanagementplan.md` |
| Durchführungsauftrag (DA) | Dokument | Projektsteuerung · Projektführung | Durchführungsfreigabe | Projektmanagementplan | `dokumente/durchfuehrungsauftrag.md` |

## Konzept

| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |
|---|---|---|---|---|---|
| Situationsanalyse | Dokument | Organisation, Produkt, IT-System | – | – | `dokumente/situationsanalyse.md` |
| Organisationsanforderungen | Dokument | Organisation | – | Situationsanalyse | `dokumente/organisationsanforderungen.md` |
| Organisationskonzept | Dokument | Organisation | – | Organisationsanforderungen | `dokumente/organisationskonzept.md` |
| Geschäftsmodellbeschreibung | Dokument | Organisation | – | Organisationskonzept | `dokumente/geschaeftsmodellbeschreibung.md` |
| Prozessbeschreibung | Dokument | Organisation | – | Geschäftsmodellbeschreibung | `dokumente/prozessbeschreibung.md` |
| Organisationsbeschreibung | Dokument | Organisation | – | Geschäftsmodellbeschreibung | `dokumente/organisationsbeschreibung.md` |
| Lösungsanforderungen | Dokument | Produkt, IT-System | – | Situationsanalyse | `dokumente/loesungsanforderungen.md` |
| Produktkonzept | Dokument | Produkt | Produktkonzept | Lösungsanforderungen | `dokumente/produktkonzept.md` |
| Systemkonzept | Dokument | IT-System | – | Lösungsanforderungen | `dokumente/systemkonzept.md` |
| Lösungsarchitektur | Dokument | IT-System | Lösungsarchitektur | Systemkonzept | `dokumente/loesungsarchitektur.md` |
| Integrationskonzept | Dokument | IT-System | – | Lösungsarchitektur, Lösungsanforderungen | `dokumente/integrationskonzept.md` |
| Ausschreibungsunterlagen | Dokument | Beschaffung | Ausschreibung | Lösungsanforderungen, Organisationsanforderungen, Beschaffungsanalyse* | `dokumente/ausschreibungsunterlagen.md` |
| Evaluationsbericht | Dokument | Beschaffung | Zuschlag | Ausschreibungsunterlagen | `dokumente/evaluationsbericht.md` |
| Vereinbarung | Dokument | Beschaffung | – | Evaluationsbericht | `dokumente/vereinbarung.md` |
| Testkonzept | Dokument | Testen | – | Lösungsanforderungen | `dokumente/testkonzept.md` |
| Einführungskonzept | Dokument | Einführungsorganisation | – | Lösungsanforderungen, Organisationsanforderungen | `dokumente/einfuehrungskonzept.md` |
| Migrationskonzept | Dokument | IT-Migration | – | Lösungsanforderungen | `dokumente/migrationskonzept.md` |
| Betriebskonzept | Dokument | IT-Betrieb | – | Lösungsanforderungen | `dokumente/betriebskonzept.md` |
| Service Level Agreement (SLA) | Dokument | IT-Betrieb | – | Betriebskonzept | `dokumente/service_level_agreement.md` |
| ISDS-Konzept | Dokument | ISDS | ISDS-Konzept | Lösungsanforderungen, Schutzbedarfsanalyse* | `dokumente/isds_konzept.md` |
| Datenschutzkonzept | CSI-Erweiterung | ISDS | – | Schutzbedarfsanalyse* | `dokumente/datenschutzkonzept.md` |
| Sicherheitskonzept | CSI-Erweiterung | ISDS | – | Lösungsarchitektur* | `dokumente/sicherheitskonzept.md` |
| Berechtigungskonzept | CSI-Erweiterung | ISDS | – | Lösungsarchitektur*, ISDS-Konzept* | `dokumente/berechtigungskonzept.md` |
| Schulungskonzept | CSI-Erweiterung | Einführungsorganisation | – | Einführungskonzept* | `dokumente/schulungskonzept.md` |
| Supportkonzept | CSI-Erweiterung | IT-Betrieb | – | Betriebskonzept* | `dokumente/supportkonzept.md` |

## Realisierung

| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |
|---|---|---|---|---|---|
| Detailspezifikation | Dokument | Produkt, IT-System, IT-Migration | – | Produktkonzept, Lösungsarchitektur, Integrationskonzept, Migrationskonzept | `dokumente/detailspezifikation.md` |
| Produkt entwickelt / angepasst | Zustand | Produkt | – | Detailspezifikation | – |
| System entwickelt / parametrisiert | Zustand | IT-System | – | Detailspezifikation | – |
| Schnittstellen realisiert | Zustand | IT-System | – | Detailspezifikation | – |
| Anwendungshandbuch | Dokument | Produkt, IT-System | – | Produkt entwickelt / angepasst, System entwickelt / parametrisiert | `dokumente/anwendungshandbuch.md` |
| Integrations- und Installationsanleitung | Dokument | IT-System | – | Schnittstellen realisiert | `dokumente/integrations_installationsanleitung.md` |
| Organisation umgesetzt | Zustand | Organisation | – | Prozessbeschreibung, Organisationsbeschreibung | – |
| Testinfrastruktur realisiert | Zustand | Testen | – | Testkonzept | – |
| Testprotokoll | Dokument | Testen | – | Testinfrastruktur realisiert | `dokumente/testprotokoll.md` |
| Einführungsmassnahmen realisiert | Zustand | Einführungsorganisation | – | Einführungskonzept | – |
| Migrationsverfahren realisiert | Zustand | IT-Migration | – | Detailspezifikation | – |
| Betriebsinfrastruktur realisiert | Zustand | IT-Betrieb | – | Service Level Agreement | – |
| System integriert | Zustand | IT-Betrieb | – | Betriebsinfrastruktur realisiert | – |
| Betriebshandbuch | Dokument | IT-Betrieb | – | Service Level Agreement | `dokumente/betriebshandbuch.md` |
| Betriebsorganisation realisiert | Zustand | IT-Betrieb | – | Betriebshandbuch | – |
| ISDS-Massnahmen realisiert | Zustand | ISDS | – | ISDS-Konzept | – |
| Abnahmeprotokoll · Vorabnahme | Dokument | Einführungsorganisation | Vorabnahme | Organisation umgesetzt, Anwendungshandbuch, Integrations- und Installationsanleitung, Testprotokoll, Einführungsmassnahmen realisiert, Migrationsverfahren realisiert, System integriert, Betriebsorganisation realisiert, ISDS-Massnahmen realisiert | `dokumente/abnahmeprotokoll_vorabnahme.md` |

## Einführung

| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |
|---|---|---|---|---|---|
| Organisation aktiviert | Zustand | Organisation | – | Abnahmeprotokoll · Vorabnahme | – |
| Produkt aktiviert | Zustand | Produkt | – | Abnahmeprotokoll · Vorabnahme | – |
| System aktiviert | Zustand | IT-System | – | Abnahmeprotokoll · Vorabnahme | – |
| Einführungsmassnahmen durchgeführt | Zustand | Einführungsorganisation | – | Abnahmeprotokoll · Vorabnahme | – |
| Migration durchgeführt | Zustand | IT-Migration | – | Abnahmeprotokoll · Vorabnahme | – |
| Betrieb aktiviert | Zustand | IT-Betrieb | – | Abnahmeprotokoll · Vorabnahme | – |
| ISDS-Konzept überführt | Zustand | ISDS | – | Abnahmeprotokoll · Vorabnahme | – |
| Abnahmeprotokoll · Abnahme | Dokument | Einführungsorganisation | Abnahme | Organisation aktiviert, Produkt aktiviert, System aktiviert, Einführungsmassnahmen durchgeführt, Migration durchgeführt, Betrieb aktiviert, ISDS-Konzept überführt | `dokumente/abnahmeprotokoll_abnahme.md` |

## Abschluss

| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |
|---|---|---|---|---|---|
| Altsystem entfernt | Zustand | IT-Migration | – | Migration durchgeführt | – |
| Testinfrastruktur überführt | Zustand | Testen | – | Testkonzept, Abnahmeprotokoll · Abnahme* | – |
| Projektschlussbeurteilung | Dokument | Projektsteuerung · Projektführung | Projektabschluss | Projekterfahrungen, Phasenbericht*, Abnahmeprotokoll · Abnahme* | `dokumente/projektschlussbeurteilung.md` |

## Phasenunabhängig

| Ergebnis | Typ | Module | Entscheid | Voraussetzungen | Datei |
|---|---|---|---|---|---|
| Projektstatusbericht | Dokument | Projektsteuerung · Projektführung | – | Projektmanagementplan | `dokumente/projektstatusbericht.md` |
| Phasenbericht | Dokument | Projektsteuerung · Projektführung | Phasenfreigabe | Projektstatusbericht* | `dokumente/phasenbericht.md` |
| Releasebericht | Dokument | Projektsteuerung · Projektführung | Releasefreigabe | Projektmanagementplan | `dokumente/releasebericht.md` |
| QS- und Risikobericht | Dokument | Projektsteuerung · Projektführung | – | Projektmanagementplan* | `dokumente/qs_risikobericht.md` |
| Änderungsantrag | Dokument | Projektsteuerung · Projektführung | – | Durchführungsauftrag* | `dokumente/aenderungsantrag.md` |
| Änderungsstatusliste | Dokument | Projektsteuerung · Projektführung | – | Änderungsantrag* | `dokumente/aenderungsstatusliste.md` |
| Projektentscheide | Dokument | Projektsteuerung · Projektführung | – | – | `dokumente/projektentscheide.md` |
| Projekterfahrungen | Dokument | Projektsteuerung · Projektführung | – | – | `dokumente/projekterfahrungen.md` |
| Protokoll | Vorlage | Projektsteuerung · Projektführung | – | – | `dokumente/protokoll.md` |
| Arbeitsauftrag | Vorlage | Projektsteuerung · Projektführung | – | Projektmanagementplan* | `dokumente/arbeitsauftrag.md` |

\* Pipeline-Annahme, nicht Teil des HERMES-Phasenmodells.
