from widget_registry import get_widget
from tkinter import *
from file_functions import close_window
from tkinter import colorchooser

def Sel_font_style():
    T=get_widget('text_widget')
    def fetch_font_style():
        global font_name
        font_name=var.get()
        print(font_name)
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

    root_font_style = Tk()
    root_font_style.geometry("350x400")
    root_font_style.title("Font Styles")
    root_font_style.configure(bg='#f0f0f0')

    Label(root_font_style,text="Select Font Size:",bg="#f0f0f0",font=("Helvetica",12,"bold")).pack(pady=10)

    var = StringVar(root_font_style,"1")

    fonts = ["Arial", "Times New Roman", "Helvetica", "Verdana", "Courier New", "Georgia", "Tahoma", "Garamond", "Comic Sans MS","Lucida Console"]

    for i in fonts:
        Radiobutton(root_font_style, text=i, variable=var, value=i, command=fetch_font_style).pack(anchor=W)

    ok_button=Button(root_font_style,text="OK",command = lambda: close_window(root_font_style),font=("Helvetica", 10), bg='#4caf50', fg='white')
    ok_button.pack(side=LEFT,padx=10)

    Exit_button=Button(root_font_style,text="Exit",command = lambda: close_window(root_font_style),font=("Helvetica", 10), bg='#f44336', fg='white')
    Exit_button.pack(side=RIGHT,padx=10)
    
    root_font_style.mainloop()

def Set_font_size():
    T=get_widget('text_widget')
    
    def Get_font_size():
        global font_size
        font_size=font_fetch.get()
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
        print(font_size)

    root_font_size=Tk()
    root_font_size.title("Size")
    root_font_size.geometry("200x200")
    root_font_size.configure(bg='#f0f0f0')

    Label(root_font_size,text="Enter Font Size:",bg="#f0f0f0",font=("Helvetica",12,"bold")).pack(pady=10)

    name_var=IntVar(root_font_size,15)
    font_fetch=Entry(root_font_size,textvariable=name_var,justify=CENTER,font=("Helvetica", 12))
    font_fetch.pack(pady=5)

    button_frame=Frame(root_font_size,bg='#f0f0f0')
    button_frame.pack(pady=10)

    ok_button=Button(root_font_size,text="OK",command=Get_font_size,font=("Helvetica", 10), bg='#4caf50', fg='white')
    ok_button.pack(side=LEFT,padx=10)

    Exit_button=Button(root_font_size,text="Exit",command = lambda: close_window(root_font_size),font=("Helvetica", 10), bg='#f44336', fg='white')
    Exit_button.pack(side=RIGHT,padx=10)

    root_font_size.mainloop()

def Sel_bg_color():
    T=get_widget('text_widget')
    
    def choose_color():
        global color_hex_bg_code

        color_code=colorchooser.askcolor(title="Choose color")
        color_hex_bg_code=color_code[1]

        print(color_hex_bg_code)

        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

        print(color_hex_fg_code)

    root_bg_color=Tk()
    root_bg_color.title("BG")
    root_bg_color.geometry('200x200')
    root_bg_color.configure(background='#f0f0f0')

    Label(root_bg_color,text="Choose Background Color:",bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)

    button=Button(root_bg_color,text="Select Color",command=choose_color,font=("Helvetica",10),bg="#2196f3",fg="white")
    button.pack(pady=10)

    button=Button(root_bg_color,text="Exit",command = lambda: close_window(root_bg_color),font=("Helvetica", 10), bg='#f44336', fg='white')
    button.pack(pady=10)
    root_bg_color.mainloop()

def Sel_fg_color():
    T=get_widget('text_widget')
    def choose_color():
        global color_hex_fg_code

        color_code=colorchooser.askcolor(title="Choose color")
        color_hex_fg_code=color_code[1]

        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

        print(color_hex_fg_code)

    root_fg_color=Tk()
    root_fg_color.title("FG")
    root_fg_color.geometry('200x200')
    root_fg_color.configure(background='#f0f0f0')

    Label(root_fg_color,text="Choose Foreground Color:",bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)

    button=Button(root_fg_color,text="Choose Color",command=choose_color,font=("Helvetica",10),bg="#2196f3",fg="white")
    button.pack(pady=10)

    button=Button(root_fg_color,text="Exit",command = lambda: close_window(root_fg_color),font=("Helvetica", 10), bg='#f44336', fg='white')
    button.pack(pady=10)

    root_fg_color.mainloop()