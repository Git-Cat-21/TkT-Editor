from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import colorchooser,messagebox
from spellchecker import SpellChecker
import sys
from widget_registry import register_widget
from file_functions import *
from edit_functions import *
from customize_functions import *
from help_functions import *
from print_function import *

root=Tk()
root.title("『Tk』Ed")
root.geometry("1280x720")

def New_page(event=None):
    print("Opening a new file")
    T.delete("1.0",END)
    notification("New File")
    main()

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
    
def main():
    global T
    
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky='e')
    
    menubar=Menu(root) 
    global Options_Menu
    Options_Menu=Menu(menubar,tearoff=0) 
    # menubar.bind('<Alt-1>', Options_Menu)

    menubar.add_cascade(label="File", menu=Options_Menu)
    # root.bind('<Alt-1>')
    
    Options_Menu.add_command(label="New",command=New_page,accelerator="Ctrl+N")
    root.bind('<Control-n>', New_page)
        
    Options_Menu.add_command(label="Open",command=Fetch_file_path,accelerator="Ctrl+O")
    root.bind('<Control-o>', Fetch_file_path)
    
    Options_Menu.add_command(label="Save",command=Save,accelerator="Ctrl+S")
    root.bind('<Control-s>', Save)
    
    Options_Menu.add_command(label="SaveAs",command=saveAs)
    # root.bind('<Control-Shift-s>', saveAs)
    
    Options_Menu.add_command(label="SpellCheck", command=spell_check,accelerator="F7")
    root.bind('<F7>',spell_check)
    
    Options_Menu.add_command(label="ClearScreen",command=clear_all,accelerator="Ctrl+L")
    root.bind('<Control-l>',clear_all)
    
    Options_Menu.add_separator()
    Options_Menu.add_command(label="Exit",command = lambda: close_window(root))

    Edit_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=Edit_Menu)
    Edit_Menu.add_command(label="Highlight Text",command=highlight_text,accelerator="Ctrl+P")
    root.bind("<Control-p>",highlight_text)
    Edit_Menu.add_command(label="Find and Replace",command=find_and_replace,accelerator="Ctrl+F")
    root.bind("<Control-f>",find_and_replace)
    
    Customize_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Customize",menu=Customize_Menu)
    Customize_Menu.add_command(label="Font Style",command=Sel_font_style)
    Customize_Menu.add_command(label="Font Size",command=Set_font_size)
    Customize_Menu.add_command(label="BG Color",command=Sel_bg_color)
    Customize_Menu.add_command(label="FG Color",command=Sel_fg_color)

    Help_menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=Help_menu)
    Help_menu.add_command(label="ReadMe",command=Open_ReadMe)
    Help_menu.add_command(label="Shortcuts",command=Open_Shortcuts,accelerator="F1")
    root.bind('<F1>',Open_Shortcuts)

    Print_menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Print",menu=Print_menu)
    Print_menu.add_command(label="Generate PDF",command=convert_to_pdf)
    
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

