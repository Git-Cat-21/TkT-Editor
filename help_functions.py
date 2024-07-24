from tkinter import *
from file_functions import close_window
from widget_registry import get_widget
def Open_Shortcuts(event=None):
    shortcut = Tk()
    shortcut.title("Key Shortcuts")
    shortcut.geometry("320x280")
    with open("assets/shortcut.txt", "r") as w:
        content = w.read()
    Label(shortcut,text=content, justify="left",font=("Helvetica",12,"italic")).pack()
    Exit_button=Button(shortcut,text="Exit",command = lambda: close_window(shortcut),font=("Helvetica", 10), bg='#f44336', fg='white')
    Exit_button.pack(padx=10)
    shortcut.configure()
    shortcut.mainloop()

def Open_ReadMe(event=None):
    T=get_widget('text_widget')
    global file_path
    file_path="README.md"
    with open(file_path,"r") as file_ptr:
        content=file_ptr.read()
        T.delete("1.0",END)
        T.insert("1.0",content)