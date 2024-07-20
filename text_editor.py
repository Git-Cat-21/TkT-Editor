from tkinter import *

def new():
    print("opening a new file")
    main()
    
def main():
    root=Tk()
    root.title("Text editor")
    root.geometry("700x700")
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    menubar=Menu(root) #creates menu object and stores it in menubar MAIN MENU BAR
    file=Menu(menubar,tearoff=0) #menu object called file submenu
    #tearoff detach the menu from the main window and turn it into a separate window not detached
    file.add_command(label="New",command=new)
    # file.add_command(label='Open',command=hello)
    # file.add_command(label='Save',command=hello)
    # file.add_command(label='Save As',command=hello)
    file.add_command(label='Exit',command=root.quit)
    menubar.add_cascade(label="Options", menu=file)
    T=Text(root,height=700,width=700,bg='yellow')
    T.grid(row=1, column=0, sticky='nsew')
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()

#save save as cancel open