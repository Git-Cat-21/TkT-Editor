# hi this is TkT, a portable text editor
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

#welcome to TkT
root=Tk()
root.title("『Tk』Ed")
root.geometry("1280x720")
img=PhotoImage(file='assets/pen1.png')
root.iconphoto(False,img)

def New_page(event=None):
    print("Opening a new file")
    T.delete("1.0",END)
    notification("New File",700)
    T.after(1000,main)
    # main()

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
    
    Options_Menu.add_command(label="New",command=New_page,accelerator="Ctrl+n")
    root.bind('<Control-n>', New_page)
        
    Options_Menu.add_command(label="Open",command=Fetch_file_path,accelerator="Ctrl+o")
    root.bind('<Control-o>', Fetch_file_path)
    
    Options_Menu.add_command(label="Save",command=Save,accelerator="Ctrl+s")
    root.bind('<Control-s>', Save)
    
    Options_Menu.add_command(label="SaveAs",command=saveAs,accelerator="Ctrl+Shift+S")
    root.bind('<Control-Shift-S>', saveAs)
    
    Options_Menu.add_command(label="SpellCheck", command=spell_check,accelerator="F7")
    root.bind('<F7>',spell_check)
    
    Options_Menu.add_command(label="ClearScreen",command=clear_all,accelerator="Ctrl+l")
    root.bind('<Control-l>',clear_all)
    
    Options_Menu.add_separator()
    Options_Menu.add_command(label="Exit",command = lambda: close_window(root))

    Edit_Menu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=Edit_Menu)
    Edit_Menu.add_command(label="Bold",command=set_bold,accelerator="Ctrl+b")
    root.bind("<Control-b>",set_bold)
    Edit_Menu.add_command(label="Italics",command=set_italics,accelerator="Ctrl+i")
    root.bind("<Control-i>",set_italics)
    Edit_Menu.add_command(label="Underline",command=set_underline,accelerator="Ctrl+u")
    root.bind("<Control-u>",set_underline)
    Edit_Menu.add_command(label="Stikethrough",command=set_strike,accelerator="Ctrl+r")
    root.bind("<Control-r>",set_strike)
    Edit_Menu.add_command(label="Bold&Italics",command=set_bold_italics,accelerator="Ctrl+Shift+B")
    root.bind("<Control-Shift-B>",set_bold_italics)
    Edit_Menu.add_command(label="Remove",command=remove_emphasis,accelerator="Ctrl+Shift+R")
    root.bind("<Control-Shift-R>",remove_emphasis)
    
    Edit_Menu.add_separator()
    Edit_Menu.add_command(label="Highlight Text",command=highlight_text,accelerator="Ctrl+e")
    root.bind("<Control-e>",highlight_text)
    Edit_Menu.add_command(label="Find and Replace",command=find_and_replace,accelerator="Ctrl+f")
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
    Print_menu.add_command(label="Generate PDF",command=convert_to_pdf,accelerator="Ctrl+p")
    root.bind("<Control-p>",convert_to_pdf)
    
    T=Text(root,height=700,width=700,undo=True,wrap=NONE)
    T.grid(row=0, column=0, sticky='nsew')
    T.focus_set()
    register_widget('text_widget',T)

    Font_tuple=(font_name,font_size,"normal")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(menu=menubar)

    scroll_bar_v=Scrollbar(root,orient=VERTICAL,command=T.yview)
    scroll_bar_v.grid(row=0,column=1,sticky='ns')
    T.config(yscrollcommand=scroll_bar_v.set)

    scroll_bar_h=Scrollbar(root,orient=HORIZONTAL,command=T.xview)
    scroll_bar_h.grid(row=1,column=0,sticky='ew')
    T.config(xscrollcommand=scroll_bar_h.set)

    if len(sys.argv) == 2 : 
        Fetch_file_path()
    root.mainloop()

if __name__ == "__main__":
    main()

