from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename,asksaveasfile
root=Tk()
file_path=None
savelocation=None
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


def main():
    global T
    
    root.title("Text editor")
    root.geometry("700x700")
    
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    
    #creates menu object and stores it in menubar MAIN MENU BAR
    #menu object called file submenu
    #tearoff detach the menu from the main window and turn it into a separate window not detached
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
    file1.add_command(label="Font Style")
    file1.add_command(label="Font Size")
    file1.add_command(label="bg color")
    file1.add_command(label="fg color")
    
    T=Text(root,height=700,width=700,bg='#e2c6f1')
    T.grid(row=1, column=0, sticky='nsew')

    Font_tuple=('Helvetica',15,"bold")
    T.configure(font=Font_tuple,foreground="black")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()
