from tkinter import *
from widget_registry import get_widget
from fpdf import FPDF
from file_functions import font_name,font_size
from tkinter.filedialog import askopenfilename
from file_functions import close_window,notification
from pathlib import Path

def convert_to_pdf(event=None):
    def get_values():
        destination=destination_var.get()
        file_name=file_name_var.get()
        print(destination)
        print(file_name)
        # file_save_path=destination+"/"+file_name+".pdf"
        file_save_path=str(Path(destination).joinpath(file_name))
        pdf.output(file_save_path+".pdf")
        # file_save_path=str(file_save_path)+".pdf"
        # print(file_save_path)
        notification("file saved successfully at "+file_save_path,1500)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=font_size)
    T=get_widget("text_widget")
    info=T.get("1.0",END).strip()
    pdf.multi_cell(0, 10, txt=info, align='L')

    root_browse=Tk()
    root_browse.title("Browse")
    root_browse.geometry("300x300")

    Label(root_browse,text="Generate PDF",bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)
    Label(root_browse,text="Paste the destination link :",bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)
    destination_var=StringVar(root_browse)
    get_file_dest=Entry(root_browse,textvariable=destination_var,font=('calibre',10,'normal'))
    get_file_dest.focus_set()
    get_file_dest.pack(pady=5)

    Label(root_browse,text="Enter File Name :",bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)
    file_name_var=StringVar(root_browse)
    get_file_name=Entry(root_browse,textvariable=file_name_var,font=('calibre',10,'normal'))
    get_file_name.pack()

    button_frame = Frame(root_browse, bg="#f0f0f0")
    button_frame.pack(pady=10)

    find_button = Button(button_frame, text="Browse", font=("Helvetica", 10), bg="#2196f3", fg="white",command=askopenfilename)
    find_button.pack(side="left", padx=5)

    replace_button = Button(button_frame, text="Submit", font=("Helvetica", 10), bg="#2196f3", fg="white",command=get_values)
    replace_button.pack(side="left", padx=5)

    exit_button = Button(button_frame, text="Exit", command=lambda: close_window(root_browse), font=("Helvetica", 10), bg='#f44336', fg='white')
    exit_button.pack(side="left", padx=5)

    root_browse.mainloop()

    