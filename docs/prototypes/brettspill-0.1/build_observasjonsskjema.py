import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(os.environ.get(
    "FP_OUTPUT",
    ROOT / "output" / "pdf" / "fordoyelsesparken-spilltest-0.1-observasjonsskjema.pdf",
))

PAPER = colors.HexColor("#FBF8F0")
WHITE = colors.HexColor("#FFFDF8")
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#66717C")
LINE = colors.HexColor("#D8D2C5")
TEAL = colors.HexColor("#147F8A")
TEAL_DARK = colors.HexColor("#0E5961")
TEAL_SOFT = colors.HexColor("#E4F2F3")
BURGUNDY = colors.HexColor("#7D2839")
GREEN = colors.HexColor("#2F6B4F")
ORANGE = colors.HexColor("#D9822B")
GOLD_SOFT = colors.HexColor("#FFF3D4")

FONT = "Helvetica"
BOLD = "Helvetica-Bold"
DISPLAY = "Times-Bold"

styles = getSampleStyleSheet()
BODY = ParagraphStyle("body", parent=styles["BodyText"], fontName=FONT,
                      fontSize=8.5, leading=11, textColor=INK)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=7.2, leading=9)


def paragraph(c, text, x, top, width, style=BODY):
    p = Paragraph(text, style)
    _, height = p.wrap(width, 100 * mm)
    p.drawOn(c, x, top - height)
    return top - height


def background(c, page_no, label):
    w, h = A4
    c.setFillColor(PAPER)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, h - 11 * mm, w, 11 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(BOLD, 8)
    c.drawString(14 * mm, h - 7.1 * mm, "FORDØYELSESPARKEN")
    c.drawRightString(w - 14 * mm, h - 7.1 * mm, label.upper())
    c.setStrokeColor(LINE)
    c.line(14 * mm, 12 * mm, w - 14 * mm, 12 * mm)
    c.setFillColor(MUTED)
    c.setFont(FONT, 7.2)
    c.drawString(14 * mm, 7.5 * mm, "Prototype 0.1 · Observasjon, ikke prestasjonsmåling")
    c.drawRightString(w - 14 * mm, 7.5 * mm, str(page_no))


def title(c, text, y):
    c.setFillColor(BURGUNDY)
    c.setFont(DISPLAY, 22)
    c.drawString(14 * mm, y, text)


def field(c, label, x, y, width):
    c.setFillColor(INK)
    c.setFont(BOLD, 7.5)
    c.drawString(x, y, label)
    c.setStrokeColor(LINE)
    c.line(x, y - 4 * mm, x + width, y - 4 * mm)


def checkbox(c, x, y, label, checked=False):
    c.setStrokeColor(INK)
    c.setFillColor(WHITE)
    c.rect(x, y - 3 * mm, 3 * mm, 3 * mm, fill=1, stroke=1)
    if checked:
        c.setFont(BOLD, 8)
        c.setFillColor(TEAL_DARK)
        c.drawString(x + 0.4 * mm, y - 2.7 * mm, "X")
    c.setFont(FONT, 7.5)
    c.setFillColor(INK)
    c.drawString(x + 5 * mm, y - 2.5 * mm, label)


def box(c, x, y, w, h, heading, accent=TEAL, note=None):
    c.setFillColor(WHITE)
    c.setStrokeColor(LINE)
    c.roundRect(x, y, w, h, 3 * mm, fill=1, stroke=1)
    c.setFillColor(accent)
    c.roundRect(x, y + h - 10 * mm, w, 10 * mm, 3 * mm, fill=1, stroke=0)
    c.rect(x, y + h - 10 * mm, w, 3 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(BOLD, 8.5)
    c.drawString(x + 4 * mm, y + h - 6.5 * mm, heading)
    if note:
        paragraph(c, note, x + 4 * mm, y + h - 14 * mm, w - 8 * mm, SMALL)


def ruled_area(c, x, y, w, h, spacing=7 * mm):
    c.setStrokeColor(LINE)
    line_y = y + h - spacing
    while line_y > y + 2 * mm:
        c.line(x, line_y, x + w, line_y)
        line_y -= spacing


def page_live(c):
    w, h = A4
    background(c, 1, "Spilltest 0.1")
    title(c, "OBSERVASJON UNDER SPILLET", h - 27 * mm)
    paragraph(c, "Noter det som faktisk skjer. Ikke hjelp med strategi, og ikke rett reglene underveis. "
              "Skriv gjerne spillerens egne ord.", 14 * mm, h - 36 * mm, w - 28 * mm,
              ParagraphStyle("lead", parent=BODY, fontSize=9.5, leading=12))

    field(c, "DATO", 14 * mm, h - 51 * mm, 36 * mm)
    field(c, "TESTLEDER", 56 * mm, h - 51 * mm, 58 * mm)
    field(c, "ANTALL SPILLERE", 120 * mm, h - 51 * mm, 28 * mm)
    field(c, "ALDER", 154 * mm, h - 51 * mm, 42 * mm)
    field(c, "STARTTID", 14 * mm, h - 64 * mm, 36 * mm)
    field(c, "SLUTTID", 56 * mm, h - 64 * mm, 36 * mm)
    field(c, "STARTPULS", 98 * mm, h - 64 * mm, 36 * mm)
    field(c, "SLUTTPULS", 140 * mm, h - 64 * mm, 56 * mm)

    box(c, 14 * mm, h - 128 * mm, 182 * mm, 48 * mm, "LØPENDE OBSERVASJONER", TEAL,
        "Tidspunkt · sted i parken · hva spilleren gjorde eller sa · mulig årsak")
    ruled_area(c, 19 * mm, h - 123 * mm, 172 * mm, 27 * mm, 7 * mm)

    c.setFillColor(BURGUNDY)
    c.setFont(DISPLAY, 15)
    c.drawString(14 * mm, h - 142 * mm, "STOPP, SPØRSMÅL OG FEIL")
    rows = [
        ("Regel eller sted", "Hva skjedde?", "Én gang", "Flere"),
        ("", "", "", ""), ("", "", "", ""), ("", "", "", "")
    ]
    x0, top = 14 * mm, h - 150 * mm
    widths = [38 * mm, 105 * mm, 19 * mm, 20 * mm]
    row_h = 11 * mm
    for r, values in enumerate(rows):
        x = x0
        for col, (value, width) in enumerate(zip(values, widths)):
            c.setFillColor(TEAL_SOFT if r == 0 else WHITE)
            c.setStrokeColor(LINE)
            c.rect(x, top - (r + 1) * row_h, width, row_h, fill=1, stroke=1)
            c.setFillColor(TEAL_DARK if r == 0 else INK)
            c.setFont(BOLD if r == 0 else FONT, 7)
            c.drawString(x + 2 * mm, top - r * row_h - 7 * mm, value)
            x += width

    y = 62 * mm
    box(c, 14 * mm, y, 88 * mm, 38 * mm, "SAMARBEID", GREEN,
        "Når planla spillerne sammen? Når gjorde de bare hver sin ting?")
    ruled_area(c, 19 * mm, y + 3 * mm, 78 * mm, 19 * mm, 6 * mm)
    box(c, 108 * mm, y, 88 * mm, 38 * mm, "LATTER OG ENGASJEMENT", ORANGE,
        "Hva skapte latter, spenning, overraskelse eller venting?")
    ruled_area(c, 113 * mm, y + 3 * mm, 78 * mm, 19 * mm, 6 * mm)

    c.setFillColor(GOLD_SOFT)
    c.setStrokeColor(colors.HexColor("#B89545"))
    c.roundRect(14 * mm, 20 * mm, 182 * mm, 32 * mm, 3 * mm, fill=1, stroke=1)
    c.setFillColor(BURGUNDY)
    c.setFont(BOLD, 8.5)
    c.drawString(19 * mm, 44 * mm, "HURTIG SLUTTSTATUS")
    checkbox(c, 19 * mm, 37 * mm, "Alle nådde Nødutgangen")
    checkbox(c, 72 * mm, 37 * mm, "Parken i toppform")
    checkbox(c, 122 * mm, 37 * mm, "Parkpulsen gikk tom")
    checkbox(c, 19 * mm, 28 * mm, "Fire prompeskyer")
    field(c, "NÆRING", 72 * mm, 30 * mm, 26 * mm)
    field(c, "VANN", 105 * mm, 30 * mm, 22 * mm)
    field(c, "SPILLETID", 134 * mm, 30 * mm, 55 * mm)
    c.showPage()


def scale_row(c, y, prompt, radius=3.4 * mm):
    c.setFillColor(INK)
    c.setFont(FONT, 8)
    c.drawString(18 * mm, y, prompt)
    labels = ["1", "2", "3", "4", "5"]
    start = 137 * mm
    for i, label in enumerate(labels):
        x = start + i * 11 * mm
        c.setFillColor(WHITE)
        c.setStrokeColor(TEAL)
        c.circle(x, y + 1 * mm, radius, fill=1, stroke=1)
        c.setFillColor(TEAL_DARK)
        c.setFont(BOLD, 7)
        c.drawCentredString(x, y - 1.2 * mm, label)


def page_after(c):
    w, h = A4
    background(c, 2, "Spilltest 0.1")
    title(c, "ETTER SPILLET", h - 27 * mm)
    paragraph(c, "Spør spillerne først. Fyll deretter ut testlederens vurdering. "
              "Skala: 1 = ikke i det hele tatt, 5 = svært tydelig.",
              14 * mm, h - 36 * mm, w - 28 * mm,
              ParagraphStyle("lead2", parent=BODY, fontSize=9.5, leading=12))

    c.setFillColor(TEAL_SOFT)
    c.setStrokeColor(TEAL)
    c.roundRect(14 * mm, h - 115 * mm, 182 * mm, 62 * mm, 3 * mm, fill=1, stroke=1)
    c.setFillColor(TEAL_DARK)
    c.setFont(BOLD, 9)
    c.drawString(19 * mm, h - 61 * mm, "SPILLERNES OPPLEVELSE")
    prompts = [
        "Det var tydelig hva vi kunne gjøre.",
        "Vi måtte samarbeide.",
        "Parkpulsen skapte passe spenning.",
        "Hendelseskortene gjorde spillet morsommere.",
        "Vi forstod mer av hva kroppen gjør.",
    ]
    for i, prompt in enumerate(prompts):
        scale_row(c, h - (72 + i * 9) * mm, prompt)

    y = h - 128 * mm
    questions = [
        "Morsomste øyeblikk eller område:",
        "Mest uklare eller trege øyeblikk:",
        "Én ting spillerne ville hatt mer av:",
    ]
    for prompt in questions:
        c.setFillColor(BURGUNDY)
        c.setFont(BOLD, 8.5)
        c.drawString(14 * mm, y, prompt)
        c.setStrokeColor(LINE)
        c.line(14 * mm, y - 7 * mm, 196 * mm, y - 7 * mm)
        c.line(14 * mm, y - 14 * mm, 196 * mm, y - 14 * mm)
        y -= 25 * mm

    c.setFillColor(BURGUNDY)
    c.setFont(DISPLAY, 15)
    c.drawString(14 * mm, y + 3 * mm, "TESTLEDERENS VURDERING")
    ratings = [
        "Valgene var interessante.",
        "Spillerne var avhengige av hverandre.",
        "Spillet fløt uten mye forklaring.",
        "Biologien kom fram gjennom handlingene.",
    ]
    for i, prompt in enumerate(ratings):
        scale_row(c, y - 5 * mm - i * 5.5 * mm, prompt, 2.5 * mm)
    y -= 43 * mm

    box(c, 14 * mm, 45 * mm, 88 * mm, 24 * mm, "BEHOLD I 0.2", GREEN)
    ruled_area(c, 19 * mm, 48 * mm, 78 * mm, 9 * mm, 6 * mm)
    box(c, 108 * mm, 45 * mm, 88 * mm, 24 * mm, "ENDRE I 0.2", BURGUNDY)
    ruled_area(c, 113 * mm, 48 * mm, 78 * mm, 9 * mm, 6 * mm)

    c.setFillColor(GOLD_SOFT)
    c.setStrokeColor(colors.HexColor("#B89545"))
    c.roundRect(14 * mm, 16 * mm, 182 * mm, 27 * mm, 3 * mm, fill=1, stroke=1)
    c.setFillColor(BURGUNDY)
    c.setFont(BOLD, 8.5)
    c.drawString(19 * mm, 37 * mm, "FORELØPIG BESLUTNING")
    checkbox(c, 19 * mm, 30 * mm, "Test på nytt uten endring")
    checkbox(c, 77 * mm, 30 * mm, "Juster balansen")
    checkbox(c, 126 * mm, 30 * mm, "Endre en regel")
    checkbox(c, 19 * mm, 22 * mm, "Styrk samarbeidet")
    checkbox(c, 77 * mm, 22 * mm, "Forenkle flyten")
    checkbox(c, 126 * mm, 22 * mm, "Avklar biologien")
    c.showPage()


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
    c.setTitle("Fordøyelsesparken - Spilltest 0.1 observasjonsskjema")
    c.setAuthor("Fordøyelsesparken")
    c.setSubject("Observasjon og evaluering av brettspillprototype 0.1")
    page_live(c)
    page_after(c)
    c.save()
    print(OUT)


if __name__ == "__main__":
    build()
