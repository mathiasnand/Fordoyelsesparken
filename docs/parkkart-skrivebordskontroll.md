# Skrivebordskontroll: Fordøyelsesparkens parkkart

Kontrolldato: 1. august 2026

## Formål og grunnlag

Denne kontrollen vurderer den foreløpige strukturen for bokas kartoppslag mot
Parkatlas, Faktabibelen, Designbibelen og Bokbibelen. Kontrollen gjelder
rekkefølge, innholdshierarki, sidefordeling og planlagt funksjon. Den gjelder
ikke ferdig illustrasjon, endelig typografi, fargegjengivelse, trykk eller
brukertest.

Kontrollgrunnlaget er:

- `docs/parkkart-konseptnotat.md`
- Parkatlas side 006, 008, 020 og 021
- Faktabibelen side 007 og 019
- Designbibelen side 009, 012, 014, 020 og 031
- Bokbibelen side 008 og 009

## Samlet resultat

**Resultat: Strukturen består skrivebordskontrollen med forbehold.**

Kartgrunnlaget kan videreføres til en visuelt utformet prototype. Produktet
skal likevel beholde status «Til vurdering» fordi brukstest, endelig
designkontroll, navngitt ansvar og nødvendige illustrasjonsressurser ikke er
dokumentert.

Kontrollen godkjenner ikke nye steder, nye forbindelser, ferdige ikoner eller
en selvstendig produktutgivelse.

## Kontroll mot Parkatlas

| Kontrollpunkt | Resultat | Vurdering |
| --- | --- | --- |
| Sju hovedområder | Bestått | Alle områdene i masterplanen er representert. |
| Rekkefølge | Bestått | Ruten følger Munnporten og Tannlandet, Spiserørsekspressen, Magesyrefjellet, Enzymlaboratoriet, Tynntarmslabyrinten, Gassgrottene og Tykktarmsstien, deretter Nødutgangen. |
| Én hovedrute | Bestått | En tykk, sammenhengende linje er kartets tydeligste forbindelse. |
| Parktorget | Bestått | Parktorget er vist som landemerke ved inngangen og holdes utenfor den nummererte hovedreisen. |
| Fordøyelsestreet | Bestått | Landemerket er knyttet til Parktorget og brukes til orientering. |
| Perspektiv | Bestått for struktur | Oversiktsnivået og fortellende skalaen samsvarer med atlasets regler. Endelig perspektiv må kontrolleres i illustrasjonen. |
| Kartsymboler | Delvis | Rutehierarkiet er riktig, men offisielle symboler finnes ennå ikke og må utvikles eller godkjennes før ferdig design. |

Det er ikke funnet geografiske motsetninger i den foreløpige strukturen.

## Kontroll mot Faktabibelen

| Kontrollpunkt | Resultat | Vurdering |
| --- | --- | --- |
| Biologisk retning | Bestått | Kartet går fra munn til utgang uten omveier eller omvendte forbindelser. |
| Oversettelse til parksteder | Bestått | De sju reiseleddene følger Faktabibelens etablerte oversettelse. |
| Enzymlaboratoriets plass | Bestått | Området ligger mellom Magesyrefjellet og Tynntarmslabyrinten. |
| Tykktarm og avslutning | Bestått | Gassgrottene og Tykktarmsstien kommer før Nødutgangen. |
| Fantasi og funksjon | Bestått for struktur | Kartet endrer ikke biologisk funksjon. Visuelle attraksjoner må kontrolleres når de er tegnet. |

Den foreløpige ruten kan brukes videre som faglig struktur. Faktatekster og
illustrerte hendelser må få en ny faglig kontroll i neste prototype.

## Kontroll mot Designbibelen

| Kontrollpunkt | Resultat | Vurdering |
| --- | --- | --- |
| Oppslagsformat | Bestått som prototype | To stående A4-sider danner et liggende A3-oppslag. Endelig bokformat er fortsatt ikke låst. |
| Trygge marger | Bestått for struktur | Skissen reserverer 22 mm rundt innholdet. Endelige mål må kontrolleres i produksjonsfilen. |
| Midtfals | Bestått | Ruten krysser falsen én gang mellom etappe 3 og 4. Ingen stedsnavn eller figurer er planlagt i risikosonen. |
| Visuelt hierarki | Bestått for struktur | Hovedruten er viktigst, deretter områder, navn og landemerker. |
| Typografi | Ikke kontrollert | Den endelige typografien er ikke satt. Georgia og Segoe UI skal brukes etter gjeldende roller. |
| Farger og logo | Ikke kontrollert | Strukturskissen fastsetter ikke ferdig palett eller logoplassering. |
| Ikoner | Ikke kontrollert | `assets/icons/` og et godkjent ikonsett mangler. Plassholdersymboler kan ikke publiseres. |
| Lesbarhet | Delvis | Hierarkiet er ryddig, men faktisk skriftstørrelse, kontrast og detaljtetthet må testes i utskrift. |

Designkontrollen er derfor bare strukturell. Den kan ikke brukes som endelig
visuell godkjenning.

## Kontroll mot Bokbibelen

| Kontrollpunkt | Resultat | Vurdering |
| --- | --- | --- |
| Funksjon i hovedboka | Bestått | Kartet viser hvordan områdene og hovedreisen henger sammen, slik Bokbibelen krever. |
| Opplevelse før pugging | Bestått for struktur | Kartet framstår som parkorientering og bruker bare korte ledetekster. |
| Basse som vert | Delvis | Det er avsatt plass til Basse og en kort velkomst, men figur, positur og replikk er ikke utviklet. |
| Illustrasjonen leder | Delvis | Kartflaten er dominerende, men dette må bekreftes når faktiske illustrasjoner og tekst er satt inn. |
| Forhold til selvstendig produkt | Avklart foreløpig | Kartet utvikles først som bokoppslag. En egen brettkartvariant vurderes senere fra samme kartgrunnlag. |

Den anbefalte boktilknytningen er dermed sterk nok til å styre neste
prototype, men er ikke en beslutning om et selvstendig kartprodukt.

## Gjenstående sperrer

Følgende må dokumenteres før produktet kan flyttes til «Under utvikling»:

1. En enkel brukstest med representanter for primærmålgruppen må bekrefte at
   start, retning og slutt forstås uten forklaring.
2. Ansvarlig for neste prototype og relevante faglige medeiere må navngis.
3. Nødvendige illustrasjonsressurser må listes, inkludert områdemotiver,
   Basse-positur, landemerker og symboler.
4. En visuelt utformet prototype må kontrolleres for typografi, kontrast,
   detaljtetthet, marger og midtfals i faktisk størrelse.
5. Endelig bokformat må bekreftes eller A4-oppslaget må eksplisitt beholdes
   som midlertidig arbeidsformat.

## Neste leveranse

Illustrasjonsbriefen for kartoppslaget er utarbeidet i
`docs/parkkart-illustrasjonsbrief.md`. Neste leveranse er en visuelt utformet
helhetsprototype og utskriftsprøve basert på briefen.
