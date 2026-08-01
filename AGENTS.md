# Arbeidsregler for Fordøyelsesparken

## Formål

Disse reglene gjelder for alt arbeid i prosjektet. Målet er å videreutvikle
Fordøyelsesparken kontrollert, uten å bryte kanon, visuell identitet eller
ansvarsdelingen mellom publikasjonene.

`PROSJEKTSTATUS.md` er prosjektets korte overleveringspunkt og skal leses
sammen med de relevante eierdokumentene før nytt arbeid starter. Statusfilen
erstatter ikke beslutninger som er dokumentert i publikasjonene.

## Faste arbeidsregler

1. Les relevante eksisterende filer før du foreslår eller gjør endringer.
2. Behandle ett tydelig avgrenset område om gangen. Ikke kombiner innhold,
   design, filopprydding og strukturendringer i samme arbeidsøkt med mindre
   oppgaven uttrykkelig krever det.
3. Endre bare filer som er nødvendige for det avgrensede området. Bevar øvrige
   filer, også når de inneholder mulige feil eller forbedringsmuligheter.
4. Gjenbruk eksisterende maler, CSS-komponenter, navn og ressurser før nye
   varianter opprettes.
5. Kontroller resultatet mot relevante bibler og felles stilark. Ved arbeid med
   eksportfiler skal både kildesidene og eksportrekkefølgen vurderes.
6. Dokumenter beslutninger i publikasjonen som eier området. Beslutninger som
   påvirker flere publikasjoner skal avklares og dokumenteres i
   Universbibelen før de innføres bredt.
7. Ikke behandle idéfrø, planlagte versjoner eller arbeidstitler som godkjente
   eller publiserte beslutninger.
8. Rapporter oppdagede avvik uten å rette dem dersom de ligger utenfor den
   avtalte oppgaven.

## Språk og navngiving

- Arbeidsspråket og publikasjonsspråket er norsk.
- Bruk de offisielle publikasjonstitlene: Universbibelen, Designbibelen,
  Karakterbibelen, Parkatlas, Bokbibelen, Faktabibelen og Digitalbibelen.
- Tekst skal være tydelig, varm og egnet for universets norske målgruppe.
  Norske navn, norske ordspill og trygg kroppslig humor er standard.
- Tekniske filnavn skal bruke små bokstaver, bindestrek og ASCII-tegn uten
  `æ`, `ø` og `å`.
- Bevar eksisterende formatering, innrykk og navnemønster i filer som endres.

## Filstruktur

- `books/`: én mappe per offisiell publikasjon; normalt én HTML-fil per A4-side
  samt omslag, bakside og eksportfil.
- `assets/logo/`: godkjente publikasjonsspesifikke logoer.
- `assets/icons/`, `assets/images/`, `assets/illustrations/`: grafiske
  ressurser når slike mapper finnes eller opprettes etter godkjent behov.
- `css/fordoyelsesparken.css`: felles stil, layout, farger og komponenter.
- `templates/`: gjenbrukbare sidemaler.
- `docs/`: prosjektregler, planer, designprinsipper og endringshistorikk.
- Prosjektroten skal holdes ryddig og bare inneholde overordnede prosjektfiler
  og uttrykkelig godkjente eksport- eller testfiler.

## Dokumenthierarki

Universbibelen står øverst og styrer helheten og kanon. Deretter eier:

- Designbibelen visuell identitet, typografi, farger, layout og illustrasjon.
- Karakterbibelen figurer, roller, stemmer, utseende og samspill.
- Parkatlas geografi, stedsnavn, hovedreise og drift.
- Bokbibelen historier, bokformat, leseropplevelse og utgivelsesstatus.
- Faktabibelen biologiske fakta, faglig kontroll og kilder.
- Digitalbibelen interaktive opplevelser, brukerreiser, digitale produkter,
  navigasjon, interaksjon, progresjon, tilgjengelighet og digital trygghet.

Ved overlapp brukes først publikasjonen som eier detaljen, deretter
Universbibelen for kontroll mot helheten.

## Låste beslutninger

Låste beslutninger skal bevares. De kan ikke endres som en lokal forbedring i
én fil eller publikasjon. Gjeldende låste grunnbeslutninger er:

- Fordøyelsesparken er en levende park inne i fordøyelsessystemet.
- Matens hovedreise følger kroppens reelle rekkefølge fra munn til utgang.
- Leseren er gjest i parken, ikke elev eller ekstern tilskuer.
- Basse Bakterie er parkens offisielle guide og en trygg, varm vert.
- Fantasien kan overdrive, men skal ikke motsi biologisk funksjon.
- Norske navn, ordspill og trygg kroppslig humor er standard.
- Den offisielle logoen er fast; bare godkjente publikasjonsspesifikke
  kjernefarger varierer.

En låst beslutning kan bare revideres når endringen er bevisst, forbedrer hele
universet på lang sikt og dokumenteres i Universbibelens versjonshistorikk
samt i alle berørte publikasjoner.

## Avgrensing før arbeid

Før en endring skal området kunne beskrives med én kort setning, for eksempel
«oppdatere Faktabibelens kildeoversikt» eller «rette toppteksten i
Designbibelen». Hvis oppgaven krever flere uavhengige områder, fullfør og
kontroller ett område før det neste påbegynnes.
