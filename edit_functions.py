from tkinter import *
from tkinter import messagebox
from widget_registry import get_widget
from file_functions import *


def set_bold(event=None):
    T = get_widget('text_widget')
    Font_tuple=(font_name,font_size,"bold")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
    
def set_italics(event=None):
    T = get_widget('text_widget')
    Font_tuple=(font_name,font_size,"italic")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
    

def set_underline(event=None):
    T = get_widget('text_widget')
    Font_tuple=(font_name,font_size,"underline")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

def set_strike(event=None):
    T = get_widget('text_widget')
    Font_tuple=(font_name,font_size,"overstrike")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

def set_bold_italics(event=None):
    T = get_widget('text_widget')
    Font_tuple=(font_name,font_size,"bold italic")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)

def remove_emphasis(event=None):
    T = get_widget('text_widget')
    Font_tuple=(font_name,font_size,"normal")
    T.configure(font=Font_tuple,foreground=color_hex_fg_code,background=color_hex_bg_code)
    
    
def highlight_text(event=None):
    def check_again():
        T=get_widget('text_widget')
        new_sel_ranges=T.tag_ranges("sel")
        if sel_ranges==new_sel_ranges:
            T.tag_remove("highlight","1.0",END)
        else:
            pass

    T=get_widget('text_widget')
    T.tag_remove("highlight","1.0",END)
    sel_ranges=T.tag_ranges("sel")
    
    if not sel_ranges:
        return
    sel_start,sel_end = sel_ranges
    T.tag_add('highlight',sel_start,sel_end)
    T.tag_config('highlight',background="yellow")

    T.after(1500,check_again)

def find_and_replace(event=None):
    T=get_widget('text_widget')
    def check_find_word():
        T.tag_remove("highlight","1.0",END)
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
    find_text.focus_set
    
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