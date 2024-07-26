from tkinter import *
from widget_registry import get_widget
from fpdf import FPDF
from file_functions import font_name,font_size

def convert_to_pdf():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=font_size)
    T=get_widget("text_widget")
    info=T.get("1.0",END).strip()
    pdf.multi_cell(0, 10, txt=info, align='L')
    pdf.output("mypdf1.pdf")