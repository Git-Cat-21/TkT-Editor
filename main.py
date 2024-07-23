from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import colorchooser
import sys


root=Tk()
file_path=None
save_location=None
font_name='Agave Nerd Font' #default font
font_size=15 #default font size
color_hex_bg_code='#e2c6f1' #default bg color
color_hex_fg_code='black' #default fg color

def New(event=None):
    print("Opening a new file")
    main()

def close_window(window):
    window.destroy()

def Open_file(event=None):
    global file_path
    
    if(len(sys.argv) == 2):
        file_path = sys.argv[1]
        if file_path:
            with open(file_path, "r") as fileobj:
                content = fileobj.read()
                print("file read succesfully")
                T.delete("1.0",END)
                T.insert("1.0",content)
    
    else:    
        print("opening an existing file")
        file_path = askopenfilename()
        if file_path:
            with open(file_path, "r") as fileobj:
                content = fileobj.read()
                print("file read succesfully")
                T.delete("1.0",END)
                T.insert("1.0",content)

def saveAs(event=None):
    t=T.get("1.0","end-1c")
    global save_location
    global file_path 
    print("Save As")
    save_location=asksaveasfilename()
    if save_location:
        with open(save_location,"w+") as file1:
            file1.write(t)
    print(f"File saved to location: {save_location}")
    file_path=save_location
    
def Save(event=None):
    global file_path
    print("Saving the file")
    if not file_path:
        saveAs()
    else:
        with open(file_path,"w") as file1:
            t = T.get("1.0",END)  
            file1.write(t)  
        print(f"File saved to location: {file_path}")

def Open_ReadMe(event=None):
    global file_path
    file_path="README.md"
    with open(file_path,"r") as file_ptr:
        content=file_ptr.read()
        T.delete("1.0",END)
        T.insert("1.0",content)

def Sel_font_style():
    def fetch_font_style():
        global font_name
        font_name=var.get()
        print(font_name)
        Font_tuple=(font_name,font_size,"bold")
        T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

    root_font_style = Tk()
    root_font_style.geometry("350x350")
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
    
def clear_all(self):
    T.delete("1.0",END)

def main():
    global T
    # global file_path
        
        
    
    root.title("TkT editor")
    root.geometry("1280x720")
    
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    
    menubar=Menu(root) 
    Options_Menu=Menu(menubar,tearoff=0) 
    # menubar.bind('<Alt-1>', Options_Menu)

    

    menubar.add_cascade(label="Options", menu=Options_Menu)
    
    Options_Menu.add_command(label="New  ctrl+n",command=New)
    root.bind('<Control-n>', New)
        
    Options_Menu.add_command(label="Open  ctrl+o",command=Open_file)
    root.bind('<Control-o>', Open_file)
    
    Options_Menu.add_command(label="Save  ctrl+s",command=Save)
    root.bind('<Control-s>', Save)
    
    Options_Menu.add_command(label="Save As",command=saveAs)
    # root.bind('<Control-Shift-s>', saveAs)
    
    Options_Menu.add_command(label="Clear Screen  ctrl+l",command=clear_all)
    root.bind('<Control-l>',clear_all)
    
    Options_Menu.add_separator()
    Options_Menu.add_command(label="Exit",command = lambda: close_window(root))
    
    Customize_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Customize",menu=Customize_Menu)
    Customize_Menu.add_command(label="Font Style",command=Sel_font_style)
    Customize_Menu.add_command(label="Font Size",command=Set_font_size)
    Customize_Menu.add_command(label="BG Color",command=Sel_bg_color)
    Customize_Menu.add_command(label="FG Color",command=Sel_fg_color)

    Help_menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=Help_menu)
    Help_menu.add_command(label="ReadMe",command=Open_ReadMe)
    
    T=Text(root,height=700,width=700)
    T.focus_set()
    T.grid(row=1, column=0, sticky='nsew')

    Font_tuple=(font_name,font_size,"bold")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)

    if len(sys.argv) == 2 : 
        Open_file()
        
    root.mainloop()

if __name__ == "__main__":
    main()

