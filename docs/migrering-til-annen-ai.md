# Overlevering til en annen AI-tjeneste

Sist oppdatert: 31. juli 2026

## Formål

Dette dokumentet gjør prosjektet flyttbart mellom Codex, DeepSeek og andre
kodeassistenter. Det erstatter ikke prosjektets eierdokumenter eller
`PROSJEKTSTATUS.md`.

## Dette skal flyttes

Flytt hele mappen `Fordoyelsesparken` samlet. Prosjektet består ved siste
kontroll av 217 filer, blant annet:

- 192 HTML-filer
- 16 Markdown-filer
- ett felles CSS-stilark
- én PDF-test
- logoer, fonter og øvrige ressurser under `assets/` og `fonts/`

Ikke flytt bare eksportfilene. De enkelte HTML-sidene, stilarket, ressursene,
styringsdokumentene og bokmappene er alle nødvendige for videre arbeid.

## Obligatorisk leserekkefølge for en ny assistent

1. `AGENTS.md`
2. `PROSJEKTSTATUS.md`
3. `docs/oppgaver.md`
4. Relevant eierdokument under `books/`
5. `css/fordoyelsesparken.css` og relevante maler ved designarbeid

Universbibelen styrer helheten og kanon. Designbibelen, Karakterbibelen,
Parkatlas, Bokbibelen, Faktabibelen og Digitalbibelen eier hvert sitt
fagområde slik det er beskrevet i `AGENTS.md`.

## Startprompt hos ny tjeneste

Bruk følgende tekst etter at hele prosjektmappen er gjort tilgjengelig:

> Du overtar prosjektet Fordøyelsesparken. Les først `AGENTS.md`,
> `PROSJEKTSTATUS.md`, `docs/oppgaver.md` og dette dokumentet. Oppsummer
> forståelsen din før du endrer filer. Behandle én avgrenset oppgave om
> gangen, bevar låste beslutninger og endre bare nødvendige filer. Ikke
> behandle idéfrø som godkjent kanon. Kontroller alltid resultatet mot
> publikasjonen som eier området.

## Teknisk arbeidsform

Prosjektet er et statisk HTML/CSS-prosjekt uten registrert byggesystem,
pakkehåndtering eller automatisert testkommando. De sju strukturerte
referansepublikasjonene har hver sin samlede HTML-eksport:

- `books/universbibelen/export-universbibelen.html`
- `books/designbibelen/export-designbibelen.html`
- `books/karakterbibelen/export-karakterbibelen.html`
- `books/parkatlas/export-parkatlas.html`
- `books/bokbibelen/export-bokbibelen.html`
- `books/faktabibelen/export-faktabibelen.html`
- `books/digitalbibelen/export-digitalbibelen.html`

Digitalbibelen er etablert som konseptutgave i `books/digitalbibelen/`.
Den har omslag, bakside, 22 nummererte sider og samlet HTML-eksport.
Del I–IV er utarbeidet.

Visuell kontroll må derfor gjøres ved å åpne relevante enkeltsider og
eksportfiler i en nettleser. Endelig PDF-produksjon er ikke dokumentert som
ferdig.

## Viktige begrensninger

- Git ble initialisert på grenen `main` 30. juli 2026. Repositoriet har ennå
  ingen commits, så versjonshistorikken begynner først når en kontrollert
  første commit opprettes.
- Chat-historikk er ikke prosjektets fasit. Beslutninger må hentes fra
  eierdokumentene og prosjektstatusen.
- `docs/roadmap.md` er foreldet og skal ikke brukes alene som status.
- `docs/project-rules.md` og `docs/changelog.md` er tomme plassholdere.
- Oppdagede avvik utenfor avtalt oppgave skal rapporteres, ikke rettes
  automatisk.

## Kontroll etter flytting

En ny tjeneste skal kunne:

1. Se alle 217 prosjektfiler.
2. Lese norske filnavn og UTF-8-innhold korrekt.
3. Finne de sju komplette eksportfilene ovenfor.
4. Gjengi de låste beslutningene i `AGENTS.md` uten motstrid.
5. Beskrive anbefalt neste steg fra `PROSJEKTSTATUS.md`.
6. Bekrefte at ingen filer ble endret bare ved import.

Først når disse punktene er bekreftet, bør nytt innholds- eller designarbeid
starte.
