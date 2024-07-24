from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import colorchooser,messagebox
from spellchecker import SpellChecker
import sys
from values_events import *
from widget_registry import register_widget
from values_events import *
from customize_functions import *

root=Tk()

def New(event=None):
    print("Opening a new file")
    notification("New File")
    main()

def Fetch_file_path(event=None):
    def Open_file(file_path):
        if file_path:
            with open(file_path, "r") as fileobj:
                content = fileobj.read()
                print("file read succesfully")
                T.delete("1.0",END)
                T.insert("1.0",content)
                notification("Opened file successfully")

    global file_path
    if(len(sys.argv) == 2):
        file_path = sys.argv[1]
        Open_file(file_path)
                
    else:    
        print("opening an existing file")
        file_path = askopenfilename()
        Open_file(file_path)
                
        
def spell_check(event=None):
    spell = SpellChecker()
    misspelled = T.get("1.0",END)
    words = misspelled.split()
    correction = []
    for i in words:
        correction.append(spell.correction(i))
    corrected_string = ' '.join(correction)
    T.delete('1.0',END)
    T.insert(END, corrected_string)


    
def clear_all(self):
    T.delete("1.0",END)
    
def find_and_replace(event=None):
    def check_find_word():
        T.tag_remove("highlight","1.0",END)
        info=T.get("1.0","end-1c")
        find_word=find_var.get()

        start_index="1.0"
        while True:
            start_index=T.search(find_word,start_index,nocase=1,stopindex='end')
            if not start_index:
                break
            end_index=f"{start_index}+{len(find_word)}c"   
            T.tag_add("highlight",start_index,end_index)
            start_index=end_index

        T.tag_configure("highlight",background="yellow")         
    def replace_word():
        info = T.get("1.0", "end-1c")
        find_word = find_var.get()
        rep_word = replace_var.get()

        if find_word in info:
            pos=0
            while True:
                pos=info.find(find_word,pos)
                if pos ==-1:
                    break
                T.tag_remove('highlight','1.0',END)
                start_pos = f"1.0 + {pos} chars"
                end_pos = f"1.0 + {pos + len(find_word)} chars"
                T.tag_add('highlight',start_pos,end_pos)
                T.tag_config('highlight',background="yellow")

                T.see(start_pos)
                T.mark_set("insert",end_pos)
                T.focus()

                if messagebox.askyesno("Replace",f"Do you want to replace '{find_word}' and '{rep_word}'?"):
                    info = info[:pos] + rep_word + info[pos + len(find_word):]
                    pos += len(rep_word)
                else:
                    pos+=len(find_word)

                T.delete("1.0",END)
                T.insert("1.0",info)
                T.tag_remove("highlight","1.0",END)

            print(f"Finished replacing occurrences of '{find_word}'")
        else:
            print(f"Word '{find_word}' not found")

    def replace_all():
        info = T.get("1.0", "end-1c")
        find_word = find_var.get()
        rep_word = replace_var.get()
        if find_word in info:
            info = info.replace(find_word, rep_word)
            T.delete("1.0", END)
            T.insert("1.0", info)
            print(f"Replaced all occurrences of '{find_word}' with '{rep_word}'")
        else:
            print(f"Word '{find_word}' not found")

    root_find_replace = Tk()
    root_find_replace.title("Find and Replace")
    root_find_replace.geometry("300x300")
    root_find_replace.configure(bg="#f0f0f0")

    Label(root_find_replace,text="Find and Replace :",bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)
    Label(root_find_replace,text="Find :" ,bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)
    find_var=StringVar(root_find_replace)
    find_text=Entry(root_find_replace,textvariable=find_var,justify=CENTER,font=("Helvetica", 12))
    find_text.pack(pady=5)
    
    replace_var=StringVar(root_find_replace)
    Label(root_find_replace,text="Replace :" ,bg="#f0f0f0",font=("Helvetica",12)).pack(pady=10)
    replace_text=Entry(root_find_replace,textvariable=replace_var,justify=CENTER,font=("Helvetica",12,"bold"))
    replace_text.pack(pady=5)
    print(replace_var.get())

    button_frame = Frame(root_find_replace, bg="#f0f0f0")
    button_frame.pack(pady=10)

    find_button = Button(button_frame, text="Find", font=("Helvetica", 10), bg="#2196f3", fg="white",command=check_find_word)
    find_button.pack(side="left", padx=5)

    replace_button = Button(button_frame, text="Replace", font=("Helvetica", 10), bg="#2196f3", fg="white",command=replace_word)
    replace_button.pack(side="left", padx=5)

    replaceAll_button = Button(button_frame, text="Replace All", font=("Helvetica", 10), bg="#2196f3", fg="white",command=replace_all)
    replaceAll_button.pack(side="left", padx=5)

    exit_button = Button(button_frame, text="Exit", command=lambda: close_window(root_find_replace), font=("Helvetica", 10), bg='#f44336', fg='white')
    exit_button.pack(side="left", padx=5)

    root_find_replace.mainloop()

def main():
    global T
    
    root.title("『Tk』Ed")
    root.geometry("1280x720")
     
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    
    menubar=Menu(root) 
    global Options_Menu
    Options_Menu=Menu(menubar,tearoff=0) 
    # menubar.bind('<Alt-1>', Options_Menu)

    menubar.add_cascade(label="File", menu=Options_Menu)
    # root.bind('<Alt-1>')
    
    Options_Menu.add_command(label="New    ctrl+n",command=New)
    root.bind('<Control-n>', New)
        
    Options_Menu.add_command(label="Open  ctrl+o",command=Fetch_file_path)
    root.bind('<Control-o>', Fetch_file_path)
    
    Options_Menu.add_command(label="Save   ctrl+s",command=Save)
    root.bind('<Control-s>', Save)
    
    Options_Menu.add_command(label="SaveAs",command=saveAs)
    # root.bind('<Control-Shift-s>', saveAs)
    
    Options_Menu.add_command(label="check   F7", command=spell_check)
    root.bind('<F7>',spell_check)
    
    Options_Menu.add_command(label="ClearScreen  ctrl+l",command=clear_all)
    root.bind('<Control-l>',clear_all)
    
    Options_Menu.add_separator()
    Options_Menu.add_command(label="Exit",command = lambda: close_window(root))

    Edit_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=Edit_Menu)
    Edit_Menu.add_command(label="Find and Replace",command=find_and_replace)
    
    Customize_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Customize",menu=Customize_Menu)
    Customize_Menu.add_command(label="Font Style",command=Sel_font_style)
    Customize_Menu.add_command(label="Font Size",command=Set_font_size)
    Customize_Menu.add_command(label="BG Color",command=Sel_bg_color)
    Customize_Menu.add_command(label="FG Color",command=Sel_fg_color)

    Help_menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=Help_menu)
    Help_menu.add_command(label="ReadMe",command=Open_ReadMe)
    Help_menu.add_command(label="Shortcuts F1",command=Open_Shortcuts)
    root.bind('<F1>',Open_Shortcuts)
    
    T=Text(root,height=700,width=700)
    T.grid(row=1, column=0, sticky='nsew')
    T.focus_set()
    register_widget('text_widget',T)

    Font_tuple=(font_name,font_size,"bold")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
    
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)

    if len(sys.argv) == 2 : 
        Fetch_file_path()
    
    root.mainloop()

if __name__ == "__main__":
    main()

