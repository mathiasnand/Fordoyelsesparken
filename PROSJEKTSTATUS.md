# Prosjektstatus for Fordøyelsesparken

Sist kontrollert: 31. juli 2026

## Kort status

Prosjektet har en etablert HTML/CSS-struktur og sju
referansepublikasjoner. De seks opprinnelige publikasjonene har egne
sidemapper, omslag, bakside og samlet HTML-eksport. Digitalbibelen er etablert
som konseptutgave med omslag, bakside, 22 nummererte sider og samlet
HTML-eksport. Del I–IV er utarbeidet.
Dette dokumenterer eksisterende arbeidsutgaver, ikke at de er ferdig
publisert. Fire publikasjoner oppgir versjon 1.0 som gjeldende;
Universbibelen oppgir versjon 1.1, Designbibelen versjon 1.2 og
Digitalbibelen versjon 1.0. Det finnes én PDF-test av side 003 i
Designbibelen, men ingen øvrige ferdige PDF-utgivelser i prosjektroten.

Et operativt produktregister er etablert i `docs/produktregister.md`. Det
samler og prioriterer mulige produkter, men er ikke en åttende
styringspublikasjon og innfører ikke ny logo, kjernefarge eller kanon.

`docs/roadmap.md` beskriver fortsatt en tidlig oppbyggingsfase og er ikke
oppdatert i takt med innholdet som nå finnes. `docs/project-rules.md` og
`docs/changelog.md` er tomme.

## Eksisterende publikasjoner

| Publikasjon | Omfang og rolle | Registrert status |
| --- | --- | --- |
| Universbibelen | 22 nummererte sider, omslag, bakside og eksport. Styrer kanon, identitet, dokumenthierarki og felles beslutninger. | Versjon 1.1 er gjeldende; Digitalbibelen er innført i hierarkiet (2026). |
| Designbibelen | 34 nummererte sider, omslag, bakside og eksport. Styrer logo, farger, typografi, layout, illustrasjon og ressurser. | Versjon 1.2 er gjeldende; Digitalbibelens koboltblå farge og logo er innført (2026). |
| Karakterbibelen | 24 nummererte sider, omslag, bakside og eksport. Styrer figurer, roller, stemme, utseende og samspill. | Versjon 1.0 er gjeldende; 1.1–1.3 er planlagt. |
| Parkatlas | 24 nummererte sider, omslag, bakside og eksport. Styrer geografi, steder, hovedreise og drift. | Versjon 1.0 er grunnlaget; senere versjoner er ikke fastsatt. |
| Bokbibelen | 22 nummererte sider, omslag, bakside og eksport. Styrer bokformat, historier, leseropplevelse og utgivelser. | Versjon 1.0 er grunnlaget; senere versjoner er ikke fastsatt. |
| Faktabibelen | 22 nummererte sider, omslag, bakside og eksport. Styrer biologiske fakta, faglige prinsipper og kilder. | Versjon 1.0, datert 27. juli 2026. |
| Digitalbibelen | 22 nummererte sider, omslag, bakside og eksport. Styrer interaktive opplevelser, brukerreiser, digitale produkter og interaksjon. | Versjon 1.0, del I–IV utarbeidet som konseptgrunnlag. |

## Låste beslutninger

Følgende er eksplisitt låst i Universbibelen:

- Fordøyelsesparken er en levende park inne i fordøyelsessystemet.
- Matens reise følger kroppens reelle rekkefølge fra munn til utgang.
- Leseren er gjesten, ikke eleven eller en tilskuer utenfor parken.
- Basse Bakterie er parkens offisielle guide og en trygg, varm vert.
- Fantasien kan overdrive, men skal ikke motsi biologisk funksjon.
- Universet bruker norske navn, norske ordspill og trygg kroppslig humor.
- Den offisielle logoen er fast; bare godkjente kjernefarger varierer.
- Universbibelen har erstattet Masterbibelen som overordnet referanse.
- Universbibelen bruker burgunder som fast kjernefarge.
- Digitalbibelen er den sjuende styringspublikasjonen og bruker koboltblå
  som fast kjernefarge.

Endringer som påvirker flere publikasjoner skal avgjøres og dokumenteres i
Universbibelen. Låste beslutninger skal ikke endres lokalt i én publikasjon.

## Pågående arbeid

- Den offisielle boka om Fordøyelsesparken er kjerneutgivelsen under aktiv
  utvikling. Neste registrerte behov er å låse bokplan, tekst og
  illustrasjonsbehov.
- «En dag i Fordøyelsesparken» er i konseptutvikling og trenger konkret
  handling og sideplan.
- Karakterbibelen planlegger modellark for Basse Bakterie, illustrerte
  profilark for faste ansatte og senere nye godkjente karakterer.
- Digitalbibelen er under konseptutvikling. Publikasjonsskjelett,
  kapittelstruktur, koboltblå logo og forholdet til dokumenthierarkiet er
  etablert. Del I–IV og samlet HTML-eksport er utarbeidet.
  Neste behov er helhetlig kvalitetssikring og beslutning om godkjenning.
- Designbibelen er oppdatert til versjon 1.2 med Digitalbibelens farge og logo.

## Idébank og framtidige muligheter

- «Tacofredag!», «Den store pizzakatastrofen» og «Jakten på den forsvunne
  fiberen» er idéfrø, ikke låste utgivelser.
- Fordøyelsesparkens aktivitetsbok er en framtidig mulighet.
- Flere fortellingsbøker er en idébank uten fast publiseringsrekkefølge.
- `docs/produktregister.md` inneholder en prioritert startportefølje og en
  øvrig idébank. Produktene er ikke godkjent for utvikling eller lansering.

## Åpne spørsmål og registrerte avvik

1. **Eldre fargedokumentasjon:** Universbibelen og Designbibelen er samordnet
   om Faktabibelens oransje kjernefarge. Det eldre `docs/design-charter.md`
   angir fortsatt turkis og har også eldre fargeangivelser for flere andre
   publikasjoner. Charterets videre status må avklares.
2. **Ugyldig innledning i en HTML-side:**
   `books/designbibelen/032-versjonshistorikk.html` begynner med teksten
   «Erstatt hele … med dette:» før `<!DOCTYPE html>`. Dette er et
   kvalitetsavvik og kan påvirke eksport eller rendering.
3. **Veikartet er foreldet:** `docs/roadmap.md` har uferdige punkter for
   design-system og Bokbibelen selv om prosjektet allerede inneholder langt
   mer. Det er uklart om veikartet fortsatt skal være styrende.
4. **Tomme styringsfiler:** `docs/project-rules.md` og `docs/changelog.md` er
   tomme. Det bør avgjøres om de skal tas i bruk, erstattes eller beholdes som
   plassholdere.
5. **PDF-status:** Bare `designbibelen-side-003-test.pdf` finnes som PDF.
   Det er ikke dokumentert om de seks samlede HTML-eksportene er visuelt
   kontrollert og godkjent for endelig PDF-produksjon.
6. **Mangler i ressursstrukturen:** Dokumentasjonen omtaler
   `assets/icons/`, `assets/images/` og `assets/illustrations/`, men ved siste
   kontroll var bare `assets/logo/` til stede under `assets/`.

## Sist relevante filer

Listen viser de senest endrede prosjektfilene som er relevante for videre
innholdsarbeid; den er ikke en godkjenningslogg.

Sist endret 28. juli 2026:

- `books/designbibelen/export-designbibelen.html`
- `books/designbibelen/034-tom-side.html`
- `books/designbibelen/back-cover.html`
- `books/designbibelen/002-kolofon.html`
- `books/designbibelen/001-tittelside.html`
- `books/designbibelen/cover.html`
- `books/designbibelen/033-sprak-og-navngiving.html`
- `books/designbibelen/032-versjonshistorikk.html`
- `books/designbibelen/030-filer-og-ressurser.html`
- `books/designbibelen/025-praktisk-bruk.html`
- `books/designbibelen/009-farge-system.html`
- `books/designbibelen/006-logo-varianter.html`

Sist endret 27. juli 2026:

- `books/faktabibelen/export-faktabibelen.html`
- `books/faktabibelen/back-cover.html`
- `books/faktabibelen/003-innholdsfortegnelse.html`

## Anbefalt neste steg

Gjennomfør en helhetlig innholds- og eksportkontroll av Digitalbibelen
versjon 1.0, og avgjør deretter hvilke deler som kan godkjennes som
styrende føringer.
