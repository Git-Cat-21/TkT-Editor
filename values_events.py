from tkinter import *
file_path=None
save_location=None
font_name='Agave Nerd Font' #default font
font_size=15 #default font size
color_hex_bg_code='#e2c6f1' #default bg color
color_hex_fg_code='black' #default fg color
rep_word=None

def notification(message):
    root_destroy=Tk()
    root_destroy.geometry("300x100")
    
    root_destroy.attributes('-topmost',True)
    root_destroy.overrideredirect(True)

    notification_label=Label(root_destroy,text=message,font=("Helvetica",12,"bold"),fg="white",bg="black",padx=10,pady=10)
    notification_label.pack(expand=True,fill='both')

    root_destroy.update_idletasks()
    width=root_destroy.winfo_width()
    height=root_destroy.winfo_height()
    x = (root_destroy.winfo_screenwidth() // 2) - (width // 2)
    y=50
    root_destroy.geometry(f'{width}x{height}+{x}+{y}')

    root_destroy.after(700,root_destroy.destroy)
    root_destroy.mainloop()

def close_window(window):
    window.destroy()

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
