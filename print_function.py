from tkinter import *
from widget_registry import get_widget
from fpdf import FPDF
from file_functions import font_name,font_size
from tkinter.filedialog import askopenfilename

def convert_to_pdf():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=font_size)
    T=get_widget("text_widget")
    info=T.get("1.0",END).strip()
    pdf.multi_cell(0, 10, txt=info, align='L')

    root_browse=Tk()
    root_browse.title("Browse")
    root_browse.geometry("300x300")

    destination_var=StringVar()
    file_name_var=StringVar()

    get_file_dest=Entry(root_browse,textvariable=destination_var,font=('calibre',10,'normal'))
    get_file_dest.pack()

    get_file_name=Entry(root_browse,textvariable=file_name_var,font=('calibre',10,'normal'))
    get_file_name.pack()

    # browse, submit, exit

    root_browse.mainloop()
    # askopenfilename()

    
    pdf.output("mypdf1.pdf")