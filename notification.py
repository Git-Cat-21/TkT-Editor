from tkinter import *
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