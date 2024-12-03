import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("text_files/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    df = pd.read_csv(filepath)

    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    text_name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=text_name, ln=1)

    # Get the content of each text file
    # OR USE: with open(filepath, "r") as file:
    file = open(filepath, 'r')
    content = file.read()
    # Add the text file content to the PDf
    pdf.set_font(family="Times", size=16)
    pdf.multi_cell(w=0, h=8, txt=content)

# Produce the PDF
pdf.output("output.pdf")