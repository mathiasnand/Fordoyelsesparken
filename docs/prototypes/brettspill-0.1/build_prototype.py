import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A3, A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(os.environ.get(
    "FP_OUTPUT",
    ROOT / "output" / "pdf" / "fordoyelsesparken-brettspill-prototype-0.1.pdf",
))

PAPER = colors.HexColor("#FBF8F0")
PAPER_WHITE = colors.HexColor("#FFFDF8")
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#66717C")
LINE = colors.HexColor("#D8D2C5")
GOLD = colors.HexColor("#B89545")
GOLD_LIGHT = colors.HexColor("#DFC67E")
TEAL = colors.HexColor("#147F8A")
TEAL_DARK = colors.HexColor("#0E5961")
TEAL_SOFT = colors.HexColor("#E4F2F3")
BURGUNDY = colors.HexColor("#7D2839")
GREEN = colors.HexColor("#2F6B4F")
ORANGE = colors.HexColor("#D9822B")
BLUE = colors.HexColor("#315DA8")
PURPLE = colors.HexColor("#70458A")

FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_DISPLAY = "Times-Bold"

styles = getSampleStyleSheet()
BODY = ParagraphStyle("body", parent=styles["BodyText"], fontName=FONT, fontSize=9.2,
                      leading=12, textColor=INK, spaceAfter=4)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=7.4, leading=9.2)
CARD_TITLE = ParagraphStyle("cardtitle", parent=BODY, fontName=FONT_BOLD, fontSize=10.5,
                            leading=12, textColor=TEAL_DARK, alignment=TA_CENTER)
CARD_BODY = ParagraphStyle("cardbody", parent=SMALL, fontSize=7.8, leading=9.6,
                           alignment=TA_CENTER)


def page_bg(c, size, label, page_no=None):
    c.setPageSize(size)
    w, h = size
    c.setFillColor(PAPER)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, h - 11 * mm, w, 11 * mm, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 8)
    c.setFillColor(colors.white)
    c.drawString(14 * mm, h - 7.1 * mm, "FORDØYELSESPARKEN")
    c.drawRightString(w - 14 * mm, h - 7.1 * mm, label.upper())
    c.setStrokeColor(LINE)
    c.line(14 * mm, 12 * mm, w - 14 * mm, 12 * mm)
    c.setFillColor(MUTED)
    c.setFont(FONT, 7.5)
    c.drawString(14 * mm, 7.5 * mm, "Prototype 0.1 · Spilltest · Ikke endelig design")
    if page_no:
        c.drawRightString(w - 14 * mm, 7.5 * mm, str(page_no))


def title(c, text, x, y, size=24, color=BURGUNDY):
    c.setFont(FONT_DISPLAY, size)
    c.setFillColor(color)
    c.drawString(x, y, text)


def para(c, text, x, y, width, style=BODY):
    p = Paragraph(text, style)
    _, h = p.wrap(width, 200 * mm)
    p.drawOn(c, x, y - h)
    return y - h


def rounded_box(c, x, y, w, h, fill=PAPER_WHITE, stroke=LINE, radius=4 * mm):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def section_box(c, heading, body, x, top, w, h, color=TEAL):
    rounded_box(c, x, top - h, w, h)
    c.setFillColor(color)
    c.roundRect(x, top - 12 * mm, w, 12 * mm, 4 * mm, fill=1, stroke=0)
    c.rect(x, top - 12 * mm, w, 4 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(FONT_BOLD, 11)
    c.drawString(x + 5 * mm, top - 8 * mm, heading)
    para(c, body, x + 5 * mm, top - 16 * mm, w - 10 * mm, BODY)


def cover(c):
    w, h = A4
    c.setFillColor(PAPER)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, h - 62 * mm, w, 62 * mm, fill=1, stroke=0)
    c.setFillColor(GOLD_LIGHT)
    c.circle(w - 26 * mm, h - 31 * mm, 15 * mm, fill=1, stroke=0)
    c.setFillColor(BURGUNDY)
    c.circle(24 * mm, 30 * mm, 20 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(FONT_BOLD, 11)
    c.drawString(18 * mm, h - 18 * mm, "FORDØYELSESPARKEN")
    c.setFont(FONT_DISPLAY, 31)
    c.drawString(18 * mm, h - 38 * mm, "FULL FART GJENNOM")
    c.drawString(18 * mm, h - 51 * mm, "FORDØYELSESPARKEN")
    c.setFillColor(BURGUNDY)
    c.setFont(FONT_DISPLAY, 20)
    c.drawString(18 * mm, h - 86 * mm, "Et samarbeidsspill fra munn til utgang")
    c.setFillColor(INK)
    c.setFont(FONT, 12)
    c.drawString(18 * mm, h - 100 * mm, "1-4 spillere · ca. 25 minutter · fra 6 år")
    # Stylized route
    y = h - 135 * mm
    stops = [
        ("MUNN", ORANGE), ("SPISERØR", BLUE), ("MAGE", BURGUNDY),
        ("ENZYMER", PURPLE), ("TYNNTARM", GREEN), ("TYKKTARM", TEAL)
    ]
    xs = [25, 57, 89, 121, 153, 185]
    c.setStrokeColor(GOLD)
    c.setLineWidth(5)
    c.line(xs[0] * mm, y, xs[-1] * mm, y)
    for (label, col), x in zip(stops, xs):
        c.setFillColor(col)
        c.circle(x * mm, y, 8 * mm, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont(FONT_BOLD, 6.5)
        c.drawCentredString(x * mm, y - 14 * mm, label)
    rounded_box(c, 18 * mm, 45 * mm, w - 36 * mm, 43 * mm, TEAL_SOFT, TEAL)
    c.setFillColor(TEAL_DARK)
    c.setFont(FONT_DISPLAY, 16)
    c.drawString(25 * mm, 75 * mm, "Velkommen inn!")
    para(c, "Hjelp matgjestene gjennom parkens arbeidsstasjoner. Tygg, elt, løs opp, "
            "samle næring og hent tilbake vann før Parkpulsen går tom.",
         25 * mm, 68 * mm, w - 50 * mm, ParagraphStyle("coverbody", parent=BODY, fontSize=11, leading=15))
    c.setFillColor(colors.white)
    c.setFont(FONT_BOLD, 9)
    c.drawCentredString(24 * mm, 28 * mm, "0.1")
    c.showPage()


def rules_one(c):
    w, h = A4
    page_bg(c, A4, "Regler", 2)
    title(c, "KOM I GANG", 14 * mm, h - 27 * mm)
    para(c, "Basse Bakterie trenger hjelp med frokostrushen. Alle spillerne er æresgjester "
            "som samarbeider om å få matgjestene gjennom parken og levere det kroppen trenger.",
         14 * mm, h - 36 * mm, w - 28 * mm,
         ParagraphStyle("lead", parent=BODY, fontSize=11, leading=15))
    section_box(c, "MÅLET", "Få alle fire matgjestene til Nødutgangen før Parkpulsen når null. "
                "For full seier må dere også levere minst <b>6 næring</b> og <b>3 vann</b> til kroppen.",
                14 * mm, h - 60 * mm, 86 * mm, 48 * mm, BURGUNDY)
    section_box(c, "I PAKKEN", "1 A3-brett · 12 matkort · 18 hendelseskort · 4 gjestebrikker · "
                "8 matgjestebrikker · arbeidsbrikker · næring · vann · prompeskyer · Parkpulsmarkør.",
                110 * mm, h - 60 * mm, 86 * mm, 48 * mm, GREEN)
    title(c, "OPPSETT", 14 * mm, h - 123 * mm, 18)
    setup = [
        "1. Legg A3-brettet midt på bordet.",
        "2. Still Parkpulsen etter antall spillere: 1 spiller = 18, 2 = 12, 3 = 9, 4 = 7.",
        "3. Legg næring, vann, arbeidsbrikker og prompeskyer ved brettet.",
        "4. Finn matkortene Eplebit, Brødbit, Ostebit og Vann. Legg dem åpne ved Munnporten.",
        "5. Legg én matgjestebrikke på hvert av de fire kortene.",
        "6. Stokk hendelseskortene. Hver spiller velger en gjestebrikke.",
        "7. Den som sist spiste noe, blir startspiller."
    ]
    y = h - 134 * mm
    for i, item in enumerate(setup, 1):
        c.setFillColor(TEAL)
        c.circle(19 * mm, y - 2 * mm, 4 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(FONT_BOLD, 8)
        c.drawCentredString(19 * mm, y - 4.3 * mm, str(i))
        y = para(c, item, 27 * mm, y + 1 * mm, 164 * mm, BODY) - 5 * mm
    rounded_box(c, 14 * mm, 22 * mm, w - 28 * mm, 34 * mm, colors.HexColor("#FFF3D4"), GOLD)
    c.setFillColor(BURGUNDY)
    c.setFont(FONT_BOLD, 10)
    c.drawString(20 * mm, 47 * mm, "FØR FØRSTE TEST")
    para(c, "Klipp ut kort og brikker. Brettet er side 4 og skal skrives ut på A3 liggende. "
            "Kortark og brikker kan skrives ut på vanlig A4. Bruk gjerne mynter som markører.",
         20 * mm, 41 * mm, w - 40 * mm, SMALL)
    c.showPage()


def rules_two(c):
    w, h = A4
    page_bg(c, A4, "Regler", 3)
    title(c, "SLIK SPILLER DERE", 14 * mm, h - 27 * mm)
    intro = "På turen gjør spilleren <b>to parkhandlinger</b> og trekker ett hendelseskort. Når alle har hatt tur, er runden ferdig og Parkpulsen går ned med én."
    para(c, intro, 14 * mm, h - 37 * mm, w - 28 * mm,
         ParagraphStyle("lead2", parent=BODY, fontSize=11, leading=15))
    actions = [
        ("JOBB", "Legg én arbeidsbrikke på en matgjest i området der gjestebrikken din står."),
        ("FLYTT DEG", "Flytt gjestebrikken til neste eller forrige parkområde."),
        ("SAMARBEID", "Er to gjester i samme område, kan én handling legge ut to like arbeidsbrikker."),
        ("RYDD GASS", "Fjern én prompesky fra Gassgrottene. Dette krever én handling."),
        ("BASSEHJELP", "Legg to like brikker tilbake i lageret og legg ut én valgfri brikke.")
    ]
    y = h - 55 * mm
    for name, desc in actions:
        rounded_box(c, 14 * mm, y - 18 * mm, 182 * mm, 15 * mm, PAPER_WHITE, LINE, 2 * mm)
        c.setFillColor(TEAL_DARK)
        c.setFont(FONT_BOLD, 9)
        c.drawString(19 * mm, y - 9 * mm, name)
        para(c, desc, 50 * mm, y - 5.5 * mm, 139 * mm, SMALL)
        y -= 20 * mm
    title(c, "NÅR ET OMRÅDE ER FERDIG", 14 * mm, y - 8 * mm, 16)
    para(c, "Når matkortets krav er oppfylt, flyttes matgjesten automatisk til neste område. "
            "Fjern brukte arbeidsbrikker. Ta næring eller vann når kortet ber om det.",
         14 * mm, y - 16 * mm, w - 28 * mm, BODY)
    y -= 33 * mm
    rounded_box(c, 14 * mm, y - 22 * mm, w - 28 * mm, 20 * mm, TEAL_SOFT, TEAL, 2 * mm)
    para(c, "<b>Fast reise:</b> Spiserøret krever 1 bølge. Tynntarmen leverer kortets næring. "
            "Fiber lager 1 prompesky i Gassgrottene. Tykktarmen leverer kortets vann.",
         19 * mm, y - 7 * mm, w - 38 * mm, SMALL)
    y -= 29 * mm
    section_box(c, "SEIER", "Alle matgjestene når Nødutgangen før Parkpulsen går tom. "
                "6 næring + 3 vann gir <b>Parken i toppform</b>. Ellers har dere fullført reisen.",
                14 * mm, y, 86 * mm, 43 * mm, GREEN)
    section_box(c, "PAUSE I PARKDRIFTEN", "Dere taper hvis Parkpulsen når null, eller hvis en fjerde "
                "prompesky skal legges i Gassgrottene. Nullstill og prøv igjen med Parkpulsen på 14.",
                110 * mm, y, 86 * mm, 43 * mm, BURGUNDY)
    c.showPage()


AREAS = [
    ("1", "MUNNPORTEN", "Start", ORANGE),
    ("2", "TANNLANDET", "2 tygg + 1 spytt", GOLD),
    ("3", "SPISERØRSEKSPRESSEN", "1 bølge", BLUE),
    ("4", "MAGESYREFJELLET", "2 elt + 1 magesaft", BURGUNDY),
    ("5", "ENZYMLABORATORIET", "Match matkortets symbol", PURPLE),
    ("6", "TYNNTARMSLABYRINTEN", "Hent næring", GREEN),
    ("7", "GASSGROTTENE", "Fiber kan gi gass", colors.HexColor("#8A6A9B")),
    ("8", "TYKKTARMSSTIEN", "Hent vann", TEAL),
    ("9", "NØDUTGANGEN", "Reisen er ferdig", colors.HexColor("#4F5963")),
]


def board(c):
    size = landscape(A3)
    w, h = size
    page_bg(c, size, "A3-spillebrett", 4)
    title(c, "PARKENS HOVEDREISE", 15 * mm, h - 25 * mm, 22)
    c.setFillColor(MUTED)
    c.setFont(FONT, 9)
    c.drawRightString(w - 15 * mm, h - 25 * mm, "Matgjestene følger pilene · ansatte kan bevege seg begge veier")
    # Park pulse
    px, py = 18 * mm, 20 * mm
    rounded_box(c, px, py, 55 * mm, 47 * mm, colors.HexColor("#FFF3D4"), GOLD)
    c.setFillColor(BURGUNDY)
    c.setFont(FONT_BOLD, 11)
    c.drawString(px + 5 * mm, py + 38 * mm, "PARKPULS")
    for i in range(12):
        xx = px + 7 * mm + (i % 6) * 7.5 * mm
        yy = py + 25 * mm - (i // 6) * 12 * mm
        c.setFillColor(colors.white if i else BURGUNDY)
        c.setStrokeColor(BURGUNDY)
        c.circle(xx, yy, 3 * mm, fill=1, stroke=1)
        c.setFillColor(BURGUNDY if i else colors.white)
        c.setFont(FONT_BOLD, 6)
        c.drawCentredString(xx, yy - 2, str(12 - i))
    # Body bank
    bx = w - 71 * mm
    rounded_box(c, bx, py, 53 * mm, 47 * mm, TEAL_SOFT, TEAL)
    c.setFillColor(TEAL_DARK)
    c.setFont(FONT_BOLD, 11)
    c.drawString(bx + 5 * mm, py + 38 * mm, "LEVERT TIL KROPPEN")
    c.setFont(FONT_BOLD, 9)
    c.setFillColor(GREEN)
    c.drawString(bx + 6 * mm, py + 25 * mm, "NÆRING:  0 1 2 3 4 5 6+")
    c.setFillColor(BLUE)
    c.drawString(bx + 6 * mm, py + 13 * mm, "VANN:      0 1 2 3+")
    # Route 5 top, 4 bottom
    card_w, card_h = 67 * mm, 54 * mm
    top_y, bot_y = 113, 48
    top_xs = [15, 91, 167, 243, 319]
    bot_xs = [281, 205, 129, 53]
    positions = [(x * mm, top_y * mm) for x in top_xs] + [(x * mm, bot_y * mm) for x in bot_xs]
    # connecting arrows first
    c.setStrokeColor(GOLD)
    c.setFillColor(GOLD)
    c.setLineWidth(5)
    centers = [(x + card_w / 2, y + card_h / 2) for x, y in positions]
    for (x1, y1), (x2, y2) in zip(centers, centers[1:]):
        c.line(x1, y1, x2, y2)
    for (num, name, req, col), (x, y) in zip(AREAS, positions):
        rounded_box(c, x, y, card_w, card_h, PAPER_WHITE, col, 5 * mm)
        c.setFillColor(col)
        c.roundRect(x, y + card_h - 16 * mm, card_w, 16 * mm, 5 * mm, fill=1, stroke=0)
        c.rect(x, y + card_h - 16 * mm, card_w, 5 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.circle(x + 9 * mm, y + card_h - 8 * mm, 5 * mm, fill=0, stroke=1)
        c.setFont(FONT_BOLD, 10)
        c.drawCentredString(x + 9 * mm, y + card_h - 11 * mm, num)
        c.setFont(FONT_BOLD, 9.5 if len(name) < 18 else 7.8)
        c.drawString(x + 17 * mm, y + card_h - 11 * mm, name)
        c.setFillColor(INK)
        c.setFont(FONT_BOLD, 9)
        c.drawCentredString(x + card_w / 2, y + 22 * mm, req)
        c.setFillColor(MUTED)
        c.setFont(FONT, 7)
        c.drawCentredString(x + card_w / 2, y + 10 * mm, "Plass for matgjester og ansatte")
    c.showPage()


FOODS = [
    ("EPLEBIT", "Tygg 2 · Spytt 1", "Enzym: karbo", "Næring 2 · Fiber · Vann 1"),
    ("BRØDBIT", "Tygg 2 · Spytt 1", "Enzym: karbo", "Næring 2 · Fiber"),
    ("OSTEBIT", "Tygg 2 · Spytt 1", "Enzym: fett", "Næring 2"),
    ("VANN", "Ingen tygging", "Ingen enzym", "Vann 2 i tykktarmen"),
    ("GULROT", "Tygg 3 · Spytt 1", "Enzym: karbo", "Næring 1 · Fiber · Vann 1"),
    ("HAVREGRØT", "Tygg 1 · Spytt 1", "Enzym: karbo", "Næring 2 · Fiber"),
    ("FISKEKAKE", "Tygg 2 · Spytt 1", "Enzym: protein", "Næring 2"),
    ("PIZZABIT", "Tygg 3 · Spytt 1", "Enzym: fett eller karbo", "Næring 3"),
    ("TACOBIT", "Tygg 3 · Spytt 1", "Enzym: valgfritt", "Næring 2 · Fiber"),
    ("BANANBIT", "Tygg 1 · Spytt 1", "Enzym: karbo", "Næring 2 · Fiber"),
    ("POTETBIT", "Tygg 2 · Spytt 1", "Enzym: karbo", "Næring 2"),
    ("YOGHURTSKJE", "Ingen tygging", "Enzym: protein", "Næring 1 · Vann 1"),
]


def draw_card(c, x, y, w, h, title_text, lines, accent, kind):
    c.setDash(2, 2)
    c.setStrokeColor(MUTED)
    c.setFillColor(PAPER_WHITE)
    c.roundRect(x, y, w, h, 3 * mm, fill=1, stroke=1)
    c.setDash()
    c.setFillColor(accent)
    c.roundRect(x, y + h - 14 * mm, w, 14 * mm, 3 * mm, fill=1, stroke=0)
    c.rect(x, y + h - 14 * mm, w, 4 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(FONT_BOLD, 6.5)
    c.drawString(x + 4 * mm, y + h - 6 * mm, kind)
    c.setFont(FONT_BOLD, 10 if len(title_text) < 16 else 8.5)
    c.drawCentredString(x + w / 2, y + h - 11 * mm, title_text)
    yy = y + h - 21 * mm
    for line in lines:
        yy = para(c, line, x + 4 * mm, yy, w - 8 * mm, CARD_BODY) - 1.4 * mm


def food_cards(c):
    w, h = A4
    page_bg(c, A4, "Matkort", 5)
    title(c, "MATGJESTER", 14 * mm, h - 26 * mm, 20)
    c.setFillColor(MUTED)
    c.setFont(FONT, 8)
    c.drawRightString(w - 14 * mm, h - 26 * mm, "Klipp langs de stiplede linjene")
    cw, ch = 43 * mm, 55 * mm
    x0, y0 = 14 * mm, h - 91 * mm
    for i, (name, chew, enzyme, reward) in enumerate(FOODS):
        col, row = i % 4, i // 4
        x = x0 + col * 45.5 * mm
        y = y0 - row * 58 * mm
        lines = [f"<b>Tannlandet</b><br/>{chew}", "<b>Mage</b><br/>Elt 2 · Magesaft 1",
                 f"<b>Laboratoriet</b><br/>{enzyme}", f"<b>Utbytte</b><br/>{reward}"]
        draw_card(c, x, y, cw, ch, name, lines, ORANGE if i < 4 else TEAL, "MATKORT")
    c.showPage()


EVENTS = [
    ("EKSTRA GRUNDIG TYGGING", "Legg én tygg gratis på en matgjest i Tannlandet."),
    ("SPYTTFONTENEN SPRUTER", "Legg én spytt gratis på en matgjest i Tannlandet."),
    ("BØLGE I EKSPRESSEN", "Flytt én ferdig tygget matgjest rett til Magesyrefjellet."),
    ("MAGESYREFJELLET BOBLER", "Legg én elt eller magesaft gratis i magen."),
    ("ENZYMENE ER KLARE", "Legg ett valgfritt enzymsymbol i laboratoriet."),
    ("FULL FART I LABYRINTEN", "Lever én tilgjengelig næring til kroppen."),
    ("VANNRETUR", "Lever ett tilgjengelig vann til kroppen."),
    ("BASSE KJENNER EN VEI", "Flytt en valgfri gjestebrikke til et hvilket som helst område."),
    ("ALLE HJELPER TIL", "Alle spillere får én ekstra handling på neste tur."),
    ("LITEN PARKKØ", "Neste spiller har bare én parkhandling."),
    ("TRAVELT PÅ TYGGEBANEN", "En matgjest i Tannlandet trenger én ekstra tygg."),
    ("MAGESYREFJELLET TAR EN PAUSE", "Ingen gratisarbeid i magen denne runden."),
    ("BAKTERIEFEST", "Hvis en matgjest med fiber har nådd Gassgrottene: legg én prompesky."),
    ("POFF!", "Legg én prompesky i Gassgrottene."),
    ("HVEM ÅPNET DEN LUKA?", "Fjern én prompesky, men neste spiller må starte turen med å flytte seg."),
    ("FIN PARKFLYT", "Parkpulsen går ikke ned denne runden."),
    ("OI, DER VAR DET MYE!", "Flytt Parkpulsen ned én ekstra."),
    ("VELKOMMEN INN!", "Velg: én gratis arbeidsbrikke eller flytt én gjestebrikke."),
]


def event_cards(c, start, page_no):
    w, h = A4
    page_bg(c, A4, "Hendelseskort", page_no)
    title(c, "PARKHENDELSER", 14 * mm, h - 26 * mm, 20)
    cw, ch = 56 * mm, 68 * mm
    x0, y0 = 14 * mm, h - 105 * mm
    for j, (name, effect) in enumerate(EVENTS[start:start + 9]):
        col, row = j % 3, j // 3
        x = x0 + col * 60.5 * mm
        y = y0 - row * 72 * mm
        accent = GREEN if start == 0 else BURGUNDY
        draw_card(c, x, y, cw, ch, name, ["<b>Parkmelding</b>", effect,
                  "<font color='#66717C'>Legg kortet i bruktbunken.</font>"], accent, "HENDELSE")
    c.showPage()


def token(c, x, y, r, fill, label, sub=""):
    c.setFillColor(fill)
    c.setStrokeColor(INK)
    c.setLineWidth(0.8)
    c.circle(x, y, r, fill=1, stroke=1)
    c.setFillColor(colors.white if fill != GOLD_LIGHT else INK)
    c.setFont(FONT_BOLD, 7 if len(label) < 8 else 5.5)
    c.drawCentredString(x, y + 1, label)
    if sub:
        c.setFont(FONT, 5)
        c.drawCentredString(x, y - 5, sub)


def tokens(c):
    w, h = A4
    page_bg(c, A4, "Brikker", 8)
    title(c, "KLIPP UT BRIKKENE", 14 * mm, h - 26 * mm, 20)
    work_set = ([("TYGG", GOLD)] * 8 + [("SPYTT", BLUE)] * 4 + [("BØLGE", TEAL)] * 4
                + [("ELT", BURGUNDY)] * 6 + [("MAGESAFT", ORANGE)] * 4
                + [("KARBO", PURPLE)] * 4 + [("PROTEIN", GREEN)] * 3 + [("FETT", BURGUNDY)] * 3)
    groups = [
        ("ARBEID", work_set),
        ("LEVERANSER", [("NÆRING", GREEN)] * 12 + [("VANN", BLUE)] * 8),
        ("GASS", [("POFF!", PURPLE)] * 8),
    ]
    y = h - 42 * mm
    for heading, items in groups:
        c.setFillColor(TEAL_DARK)
        c.setFont(FONT_BOLD, 9)
        c.drawString(15 * mm, y, heading)
        y -= 10 * mm
        for i, (lab, col) in enumerate(items):
            xx = 20 * mm + (i % 9) * 21 * mm
            yy = y - (i // 9) * 18 * mm
            token(c, xx, yy, 7 * mm, col, lab)
        rows = (len(items) + 8) // 9
        y -= rows * 18 * mm + 7 * mm
    c.showPage()


def aids(c):
    w, h = A4
    page_bg(c, A4, "Spillerhjelp", 9)
    title(c, "SPILLERHJELP", 14 * mm, h - 26 * mm, 20)
    aid_text = [
        "<b>PÅ DIN TUR</b><br/>1. Gjør to parkhandlinger.<br/>2. Trekk én hendelse.<br/>Etter alles tur: senk Parkpulsen med én.",
        "<b>PARKHANDLINGER</b><br/>Jobb · Flytt deg · Samarbeid · Rydd gass · Bytt to like til én valgfri.",
        "<b>HUSK</b><br/>Mat følger pilene. Ansatte kan gå begge veier. Ferdige krav flytter maten automatisk.",
        "<b>SEIER</b><br/>Alle når Nødutgangen.<br/>Toppform: minst 6 næring og 3 vann."
    ]
    for i in range(4):
        col, row = i % 2, i // 2
        x = 14 * mm + col * 92 * mm
        y = h - 56 * mm - row * 76 * mm
        rounded_box(c, x, y - 62 * mm, 86 * mm, 62 * mm, PAPER_WHITE, TEAL, 4 * mm)
        c.setFillColor(TEAL)
        c.rect(x, y - 14 * mm, 86 * mm, 14 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(FONT_BOLD, 9)
        c.drawCentredString(x + 43 * mm, y - 9 * mm, f"ÆRESGJEST {i+1}")
        para(c, aid_text[i], x + 6 * mm, y - 23 * mm, 74 * mm,
             ParagraphStyle(f"aid{i}", parent=BODY, fontSize=10, leading=15, alignment=TA_LEFT))
    c.setFillColor(TEAL_DARK)
    c.setFont(FONT_BOLD, 9)
    c.drawString(15 * mm, 80 * mm, "GJESTER, MATGJESTER OG PARKPULS")
    guest_cols = [TEAL, BURGUNDY, GREEN, ORANGE]
    for i in range(4):
        token(c, (25 + i * 27) * mm, 64 * mm, 8 * mm, guest_cols[i], f"GJEST {i+1}")
    token(c, 151 * mm, 64 * mm, 8 * mm, BURGUNDY, "PULS")
    for i in range(8):
        token(c, (23 + i * 23) * mm, 38 * mm, 8 * mm, GOLD_LIGHT, "MAT", str(i + 1))
    c.showPage()


def mission(c):
    w, h = A4
    page_bg(c, A4, "Testoppdrag", 10)
    title(c, "OPPDRAG: FROKOSTRUSHET", 14 * mm, h - 27 * mm)
    para(c, "Basse har akkurat åpnet Munnporten, og fire matgjester står klare. "
            "Kan dere holde parken i gang helt fram til Nødutgangen?",
         14 * mm, h - 39 * mm, w - 28 * mm,
         ParagraphStyle("missionlead", parent=BODY, fontSize=11, leading=15))
    section_box(c, "MATGJESTER", "Eplebit · Brødbit · Ostebit · Vann", 14 * mm,
                h - 65 * mm, 86 * mm, 38 * mm, ORANGE)
    section_box(c, "INNSTILLING", "Parkpuls etter spillertall · Maks tre prompeskyer · 6 næring · 3 vann",
                110 * mm, h - 65 * mm, 86 * mm, 38 * mm, TEAL)
    title(c, "ETTER SPILLET", 14 * mm, h - 121 * mm, 18)
    questions = [
        "Var det tydelig hva dere kunne gjøre på turen?",
        "Måtte dere faktisk samarbeide?",
        "Hvilket parkområde var morsomst?",
        "Hvilket område var tregt eller uklart?",
        "Var Parkpulsen spennende, stressende eller ubetydelig?",
        "Forstod dere hva kroppen gjorde underveis?",
        "Hva ville dere hatt mer av neste gang?"
    ]
    y = h - 132 * mm
    for i, q in enumerate(questions, 1):
        c.setFillColor(TEAL)
        c.circle(19 * mm, y - 2 * mm, 4 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(FONT_BOLD, 8)
        c.drawCentredString(19 * mm, y - 4.3 * mm, str(i))
        c.setFillColor(INK)
        c.setFont(FONT, 9.5)
        c.drawString(27 * mm, y - 3 * mm, q)
        c.setStrokeColor(LINE)
        c.line(27 * mm, y - 10 * mm, 190 * mm, y - 10 * mm)
        y -= 16 * mm
    rounded_box(c, 14 * mm, 20 * mm, w - 28 * mm, 25 * mm, TEAL_SOFT, TEAL)
    c.setFillColor(TEAL_DARK)
    c.setFont(FONT_BOLD, 10)
    c.drawString(20 * mm, 38 * mm, "TESTLEDERENS VIKTIGSTE REGEL")
    para(c, "Ikke forklar strategien. Se hvor spillerne stopper, diskuterer, ler eller glemmer en regel. "
            "Det er prototypen som testes - ikke spillerne.", 20 * mm, 32 * mm, w - 40 * mm, SMALL)
    c.showPage()


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
    c.setTitle("Full fart gjennom Fordøyelsesparken - Prototype 0.1")
    c.setAuthor("Fordøyelsesparken")
    c.setSubject("Utskriftsklar papirprototype for samarbeidsspill")
    cover(c)
    rules_one(c)
    rules_two(c)
    board(c)
    food_cards(c)
    event_cards(c, 0, 6)
    event_cards(c, 9, 7)
    tokens(c)
    aids(c)
    mission(c)
    c.save()
    print(OUT)


if __name__ == "__main__":
    build()
