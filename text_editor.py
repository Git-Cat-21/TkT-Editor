from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename

root=Tk()
file_path=None
savelocation=None
font_style_name='Agave Nerd Font' #default font

def new():
    print("opening a new file")
    main()

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
    global font_style_name

    def fetch_font_style():
        font_style_name=var.get()
        print(font_style_name)
        Font_tuple=(font_style_name,15,"bold")
        T.configure(font=Font_tuple,foreground="black")

    root_font_style = Tk()
    root_font_style.geometry("280x280")
    root_font_style.title("Font Styles")
    var = StringVar(root_font_style,"1")

    fonts = ["Arial", "Times New Roman", "Helvetica", "Verdana", "Courier New", "Georgia", "Tahoma", "Garamond", "Comic Sans MS","Lucida Console"]

    for i in fonts:
        Radiobutton(root_font_style, text=i, variable=var, value=i, command=fetch_font_style).pack(anchor=W)
    B=Button(root_font_style,text="OK",command=root_font_style.quit)

    B.pack(side=LEFT)

    B1=Button(root_font_style,text="Cancel",command=root_font_style.quit)
    B1.pack(side=LEFT)
    
    root_font_style.mainloop()

def main():
    global T
    
    root.title("Text editor")
    root.geometry("700x700")
    
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    
    menubar=Menu(root) 
    file=Menu(menubar,tearoff=0) 

    menubar.add_cascade(label="Options", menu=file)
    file.add_command(label="New",command=new)
    file.add_command(label='Open',command=open_file)
    file.add_command(label='Save',command=save)
    file.add_command(label='Save As',command=saveAs)
    file.add_separator()
    file.add_command(label='Exit',command=root.quit)
    
    file1=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Customize",menu=file1)
    file1.add_command(label="Font Style",command=Sel_Font_Style)
    file1.add_command(label="Font Size")
    file1.add_command(label="BG Color")
    file1.add_command(label="FG Color")
    
    T=Text(root,height=700,width=700,bg='#e2c6f1')
    T.grid(row=1, column=0, sticky='nsew')

    Font_tuple=(font_style_name,15,"bold")
    T.configure(font=Font_tuple,foreground="black")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()
