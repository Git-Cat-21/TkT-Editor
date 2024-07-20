from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
root=Tk()
def new():
    print("opening a new file")
    main()

def open_file():
    print("opening an existing file")
    file_path = askopenfilename()
    if file_path:
        with open(file_path, "r") as fileobj:
            content = fileobj.read()
            print(content)
            T.insert("1.0",content)

def delete():
    pass

def saveAs():
    t=T.get("1.0","end-1c")
    savelocation=asksaveasfilename()
    file1=open(savelocation,"w+")
    file1.write(t)
    file1.close()
    print(f"File saved to location: {savelocation}")

def main():
    global T
    
    root.title("Text editor")
    root.geometry("700x700")

    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')

    #creates menu object and stores it in menubar MAIN MENU BAR
    menubar=Menu(root) 
    #menu object called file submenu
    file=Menu(menubar,tearoff=0) 
    #tearoff detach the menu from the main window and turn it into a separate window not detached

    file.add_command(label="New",command=new)
    file.add_command(label='Open',command=open_file)
    # file.add_command(label='Save',command=hello)
    file.add_command(label='Save As',command=saveAs)
    file.add_command(label='Delete',command=delete)
    file.add_command(label='Exit',command=root.quit)
    menubar.add_cascade(label="Options", menu=file)

    T=Text(root,height=700,width=700,bg='#e2c6f1')
    T.grid(row=1, column=0, sticky='nsew')
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()
