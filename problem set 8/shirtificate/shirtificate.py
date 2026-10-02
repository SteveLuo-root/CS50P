from fpdf import FPDF

def main():
    pdf = FPDF(orientation = "P", format = "A4")
    pdf.add_page()
    pdf.set_auto_page_break(False)

    pdf.set_font("Helvetica", "B", 30)
    pdf.cell(0, 20, "CS50 Shirtificate", align = "C")

    shirt_width = 180
    x = (pdf.w - shirt_width) / 2
    pdf.image("shirtificate.png", x = x, y = 60, w = shirt_width)

    name = input("Name: ")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_y(110)
    pdf.cell(0, 10, f"{name} took CS50", align = "C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
