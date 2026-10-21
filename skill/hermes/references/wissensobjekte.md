<!-- Generiert aus model/hermes.yaml mit scripts/build_skill_refs.py. Nicht von Hand bearbeiten. -->

# Wissensobjekte — wer erzeugt, ergänzt und liest was


## Kern

| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |
|---|---|---|---|---|
| Stakeholder & Rollen (Querschnitt) | `stakeholder` | Projektinitialisierungsauftrag | Stakeholderliste, Projektmanagementplan, Organisationsbeschreibung | Studie, Beschaffungsanalyse, Durchführungsauftrag, Situationsanalyse, Evaluationsbericht, Einführungskonzept, Betriebskonzept, Service Level Agreement, Abnahmeprotokoll · Vorabnahme, Abnahmeprotokoll · Abnahme, Projektstatusbericht, Projektentscheide, Protokoll |
| Termine & Meilensteine | `phase_execution` | Projektinitialisierungsauftrag | Studie, Beschaffungsanalyse, Projektmanagementplan, Projektstatusbericht, Änderungsantrag | Durchführungsauftrag, Ausschreibungsunterlagen, Projektschlussbeurteilung, Phasenbericht, QS- und Risikobericht, Arbeitsauftrag |
| Kosten & Budget | `kosten` | Projektinitialisierungsauftrag | Studie, Beschaffungsanalyse, Projektmanagementplan, Durchführungsauftrag, Situationsanalyse, Projektstatusbericht, Änderungsantrag | Ausschreibungsunterlagen, Evaluationsbericht, Vereinbarung, Service Level Agreement, Projektschlussbeurteilung, Phasenbericht, Releasebericht, QS- und Risikobericht |

## Geschäftskontext

| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |
|---|---|---|---|---|
| Ausgangslage (Querschnitt) | `ausgangslage` | Projektinitialisierungsauftrag | Studie, Situationsanalyse | Stakeholderliste, Rechtsgrundlagenanalyse, Schutzbedarfsanalyse, Beschaffungsanalyse, Projektmanagementplan, Durchführungsauftrag, Organisationsanforderungen, Ausschreibungsunterlagen, Projektschlussbeurteilung, Phasenbericht, Releasebericht |
| Ziele | `ziel` | Studie | Durchführungsauftrag | Projektmanagementplan, Situationsanalyse, Organisationsanforderungen, Organisationskonzept, Geschäftsmodellbeschreibung, Lösungsanforderungen, Produktkonzept, Projektschlussbeurteilung, Projektstatusbericht, Phasenbericht, Änderungsantrag, Arbeitsauftrag |
| Rahmenbedingungen | `rahmenbedingung` | Projektinitialisierungsauftrag | Studie | Rechtsgrundlagenanalyse, Projektmanagementplan, Durchführungsauftrag, Lösungsarchitektur |
| Anforderungen | `anforderung` | Studie | Organisationsanforderungen, Lösungsanforderungen, Ausschreibungsunterlagen, Detailspezifikation, Änderungsantrag | Durchführungsauftrag, Organisationskonzept, Geschäftsmodellbeschreibung, Prozessbeschreibung, Organisationsbeschreibung, Produktkonzept, Systemkonzept, Lösungsarchitektur, Evaluationsbericht, Vereinbarung, Testkonzept, Einführungskonzept, Anwendungshandbuch, Testprotokoll, Abnahmeprotokoll · Vorabnahme, Abnahmeprotokoll · Abnahme, Releasebericht, QS- und Risikobericht, Arbeitsauftrag |
| Lösungsvariante & Szenario | `loesungsvariante` | Studie | – | Projektmanagementplan, Durchführungsauftrag, Lösungsanforderungen, Systemkonzept, Lösungsarchitektur, Ausschreibungsunterlagen |
| Entscheide | `entscheid` | Studie, Durchführungsauftrag, Produktkonzept, Lösungsarchitektur, Evaluationsbericht, ISDS-Konzept, Abnahmeprotokoll · Vorabnahme, Abnahmeprotokoll · Abnahme, Phasenbericht, Änderungsantrag, Projektentscheide, Protokoll | – | Projektschlussbeurteilung, Projektstatusbericht, QS- und Risikobericht, Änderungsstatusliste |
| Rechtliche Grundlagen | `rechtl_grundlage` | Rechtsgrundlagenanalyse | Durchführungsauftrag | Studie, Schutzbedarfsanalyse, Beschaffungsanalyse, Lösungsanforderungen, Ausschreibungsunterlagen, ISDS-Konzept, Datenschutzkonzept, Phasenbericht |

## Beschaffung

| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |
|---|---|---|---|---|
| Beschaffungsgegenstand | `beschaffungsgegenstand` | Beschaffungsanalyse | Ausschreibungsunterlagen | Evaluationsbericht |
| Anbieter | `anbieter` | Beschaffungsanalyse | Evaluationsbericht | Vereinbarung |
| Zuschlag | `zuschlag` | Evaluationsbericht | – | Vereinbarung |
| Vertrag | `vertrag` | Vereinbarung | – | Abnahmeprotokoll · Vorabnahme, Abnahmeprotokoll · Abnahme |

## Technik

| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |
|---|---|---|---|---|
| Systemkomponenten | `systemkomponente` | Studie | Situationsanalyse, Systemkonzept, Lösungsarchitektur, Detailspezifikation | Lösungsanforderungen, Integrationskonzept, Ausschreibungsunterlagen, Testkonzept, Migrationskonzept, Betriebskonzept, Service Level Agreement, ISDS-Konzept, Sicherheitskonzept, Berechtigungskonzept, Schulungskonzept, Supportkonzept, Anwendungshandbuch, Integrations- und Installationsanleitung, Betriebshandbuch |
| Schnittstellen | `schnittstelle` | Situationsanalyse | Systemkonzept, Lösungsarchitektur, Integrationskonzept, Detailspezifikation | Lösungsanforderungen, Migrationskonzept, Betriebskonzept, ISDS-Konzept, Datenschutzkonzept, Sicherheitskonzept, Integrations- und Installationsanleitung |
| Datenkategorien | `datenkategorie` | Schutzbedarfsanalyse | Studie, ISDS-Konzept, Datenschutzkonzept | Migrationskonzept, Berechtigungskonzept |
| Benutzergruppen & Organisation | `benutzergruppe` | Situationsanalyse | Organisationsanforderungen, Organisationskonzept, Prozessbeschreibung, Organisationsbeschreibung, Einführungskonzept | Geschäftsmodellbeschreibung, Lösungsanforderungen, Produktkonzept, ISDS-Konzept, Datenschutzkonzept, Berechtigungskonzept, Schulungskonzept, Supportkonzept, Anwendungshandbuch |
| Betriebsumgebung | `betriebsumgebung` | Lösungsarchitektur | Betriebskonzept | Integrationskonzept, Migrationskonzept, Service Level Agreement, Sicherheitskonzept, Integrations- und Installationsanleitung, Betriebshandbuch |
| Technische Anforderungen | `technische_anforderung` | Lösungsarchitektur | Sicherheitskonzept | Testkonzept, Detailspezifikation |

## Betrieb & Einführung

| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |
|---|---|---|---|---|
| Support & Service Levels | `supportprozess` | Betriebskonzept | Service Level Agreement, Supportkonzept, Betriebshandbuch | – |
| Backup & Recovery | `backup_konzept` | Betriebskonzept | Betriebshandbuch | – |
| Berechtigungsrollen | `berechtigungsrolle` | Berechtigungskonzept | – | Betriebshandbuch |
| Testfälle | `testfall` | Testkonzept | Testprotokoll | Abnahmeprotokoll · Vorabnahme, Abnahmeprotokoll · Abnahme |
| Migrationsschritte | `migrationsschritt` | Migrationskonzept | Detailspezifikation | Einführungskonzept |
| Schulungseinheiten | `schulungseinheit` | Einführungskonzept | Schulungskonzept | – |

## Risiko & Compliance

| Wissensobjekt | ID | Erzeugt von | Ergänzt von | Gelesen von |
|---|---|---|---|---|
| Risiken (Querschnitt) | `risiko` | Projektinitialisierungsauftrag | Studie, Schutzbedarfsanalyse, Durchführungsauftrag, Testkonzept, Einführungskonzept, Migrationskonzept, Betriebskonzept, ISDS-Konzept, Projektstatusbericht, Phasenbericht, Releasebericht, QS- und Risikobericht, Änderungsantrag | – |
| Datenschutzanforderungen | `datenschutz_anforderung` | ISDS-Konzept | Datenschutzkonzept | Vereinbarung |
| Sicherheitsanforderungen | `sicherheitsanforderung` | ISDS-Konzept | Sicherheitskonzept, Berechtigungskonzept | Betriebskonzept |
| Offene Punkte & Pendenzen (Querschnitt) | `offener_punkt` | Testprotokoll, Abnahmeprotokoll · Vorabnahme, Abnahmeprotokoll · Abnahme, Projektstatusbericht, Releasebericht, Protokoll | – | Projektschlussbeurteilung, Phasenbericht |
| Projekterfahrungen | `erfahrung` | Projekterfahrungen | – | Projektschlussbeurteilung |
