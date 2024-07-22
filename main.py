from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import colorchooser

root=Tk()
file_path=None
savelocation=None
font_name='Agave Nerd Font' #default font
font_size=14 #default font size
color_hex_bg_code='#e2c6f1' #default bg color
color_hex_fg_code='black' #default fg color

def new():
    print("opening a new file")
    main()

def close_window(window):
    window.destroy()

def open_file():
    print("opening an existing file")
    global file_path
    file_path = askopenfilename()
    if file_path:
        with open(file_path, "r") as fileobj:
            content = fileobj.read()
            print(content)
            T.delete("1.0",END)
            T.insert("1.0",content)

def saveAs():
    t=T.get("1.0","end-1c")
    global savelocation
    global file_path 
    print("Save As")
    savelocation=asksaveasfilename()
    if savelocation:
        with open(savelocation,"w+") as file1:
            file1.write(t)
    print(f"File saved to location: {savelocation}")
    file_path=savelocation
    
def save():
    global file_path
    print("Saving the file")
    if not file_path:
        saveAs()
    else:
        with open(file_path,"w") as file1:
            t = T.get("1.0",END)  
            file1.write(t)  
        print(f"File saved to location: {file_path}")

def Sel_Font_Style():
    def fetch_font_style():
        global font_name
        font_name=var.get()
        print(font_name)
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

    root_font_style = Tk()
    root_font_style.geometry("280x280")
    root_font_style.title("Font Styles")
    var = StringVar(root_font_style,"1")

    fonts = ["Arial", "Times New Roman", "Helvetica", "Verdana", "Courier New", "Georgia", "Tahoma", "Garamond", "Comic Sans MS","Lucida Console"]

    for i in fonts:
        Radiobutton(root_font_style, text=i, variable=var, value=i, command=fetch_font_style).pack(anchor=W)

    B=Button(root_font_style,text="OK",command = lambda: close_window(root_font_style))
    B.pack(side=LEFT)

    B1=Button(root_font_style,text="Cancel",command = lambda: close_window(root_font_style))
    B1.pack(side=LEFT)
    
    root_font_style.mainloop()

def Set_Font_Size():
    
    def Get_font_size():
        global font_size
        font_size=font_fetch.get()
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
        print(font_size)

    root2=Tk()
    root2.geometry("100x100")
    name_var=IntVar(root2,14)
    root2.title("Font Size")

    font_fetch=Entry(root2,textvariable=name_var,justify=CENTER)
    font_fetch.pack()

    ok_button=Button(root2,text="Ok",command=Get_font_size)
    
    ok_button.pack(side=LEFT)

    cancel_button=Button(root2,text="Cancel",command = lambda: close_window(root2))
    cancel_button.pack(side=RIGHT)

    root2.mainloop()

def Sel_bg_color():
    
    def choose_color():
        global color_hex_bg_code
        color_code=colorchooser.askcolor(title="Choose color")
        color_hex_bg_code=color_code[1]
        print(color_hex_bg_code)
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
        print(color_hex_fg_code)

    root_bg_color=Tk()
    button=Button(root_bg_color,text="Select Color",command=choose_color)
    button.pack()
    root_bg_color.mainloop()

def Sel_fg_color():
    
    def choose_color():
        global color_hex_fg_code
        color_code=colorchooser.askcolor(title="Choose color")
        color_hex_fg_code=color_code[1]
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
        print(color_hex_fg_code)

    root_fg_color=Tk()
    button=Button(root_fg_color,text="Select Color",command=choose_color)
    button.pack()
    root_fg_color.mainloop()

def main():
    global T
    
    root.title("Text editor")
    root.geometry("700x700")
    
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    
    menubar=Menu(root) 
    Options_Menu=Menu(menubar,tearoff=0) 

    menubar.add_cascade(label="Options", menu=Options_Menu)
    Options_Menu.add_command(label="New",command=new)
    Options_Menu.add_command(label='Open',command=open_file)
    Options_Menu.add_command(label='Save',command=save)
    Options_Menu.add_command(label='Save As',command=saveAs)
    Options_Menu.add_separator()
    Options_Menu.add_command(label='Exit',command = lambda: close_window(root))
    
    Customize_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Customize",menu=Customize_Menu)
    Customize_Menu.add_command(label="Font Style",command=Sel_Font_Style)
    Customize_Menu.add_command(label="Font Size",command=Set_Font_Size)
    Customize_Menu.add_command(label="BG Color",command=Sel_bg_color)
    Customize_Menu.add_command(label="FG Color",command=Sel_fg_color)
    
    T=Text(root,height=700,width=700)
    T.grid(row=1, column=0, sticky='nsew')

    Font_tuple=(font_name,font_size,"bold")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()
