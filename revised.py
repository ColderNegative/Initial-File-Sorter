#import tkinter for window with instance and title
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import marshal
import json

#window size and struture with tkinter window = win

win = tk.Tk()
win.title("file sorter")
width = 800
height = 600
canvas = tk.Canvas(win, height=height, width=width)
canvas.pack()

#widget class from tkinter smplified for my application

class widget:
    def __init__(self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color

    def frame(self):
        frame_widget = tk.Frame(win, bg=self.color)
        frame_widget.place(y=self.posy, relx=self.posx, relwidth=self.width, relheight=self.height)

    def label(self, text):
        label = tk.Label(win, bg=self.color, text = text)
        label.place(y=self.posy, relx=self.posx, relwidth=self.width, height=self.height)
 
    def button(self, text, command=None):
        self.command = command
        button = tk.Button(win, bg=self.color,command=command, text= text)
        button.place(y=self.posy, relx=self.posx, relwidth=self.width, height=self.height)
    
    def entry(self):
        global entry
        entry = tk.Entry(win, font=40)
        entry.place(relx=self.posx, y=self.posy, height=self.height, relwidth=self.width)

    def clear(self):
        entry.delete(0,tk.END)     

#various functions of buttons

def create(entry):
    
    if entry == "":
        pass
    else:
        main_frame.insert(tk.END, entry)
        label_entr.clear()
        data = main_frame.get(0,tk.END)
        with open('file.json', 'w') as f:
            json.dump(data, f)

def store_des():
    filn = main_frame.curselection()
    filt = filn[0]
    root_filename =  filedialog.askdirectory(initialdir = "/",title = "Select file")
    print(filt)
    for i in range(filt):
        if des_frame.get(i) == "":
            var = "-"
            des_frame.insert(i, var)
        else:
            pass
    
    des_frame.delete(filn)
    des_frame.insert(filn, root_filename)

    dest = des_frame.get(0, tk.END)

    with open('des.json', 'w') as f:
                json.dump(dest, f)
    
def store_org():
    root_filename =  filedialog.askdirectory(initialdir = "/",title = "Select file")
    label_org['text'] = root_filename
    with open('org.json', 'w') as f:
        json.dump(root_filename, f)

def clear():
    empty = []
    main_frame.delete(0, tk.END)
    des_frame.delete(0, tk.END)
    with open('file.json', 'w') as f:
        json.dump(empty, f)
    with open('des.json', 'w') as r:
        json.dump(empty, r)

def run():
    with open('file.json', 'r') as f:
        data_files = json.load(f)
        length = len(data_files)
    with open('org.json', 'r') as r:
        data_org = json.load(r)
    with open('des.json', 'r') as g:
        data_des = json.load(g)

    for i in range(length):
        source = Path(data_org)
        for path in source.glob('*'+str(data_files[i])):
            destination = Path(data_des[i])
            path.replace(destination / path.name)

def delete():
    filselc = main_frame.curselection()
    main_frame.delete(filselc)
    files = main_frame.get(0,tk.END)
    with open('file.json', 'w') as f:
        json.dump(files, f)
    filloc = filselc[0]
    des_frame.delete(filloc)
    destfil = des_frame.get(0,tk.END)
    with open('des.json', 'w') as r:
        json.dump(destfil, r)

#Check data function to create persistance across instances

def check_data():
    with open ('file.json', 'r') as f:
        data = json.load(f)
        data_length = len(data)
    for i in range(data_length):
        var = data[i]
        main_frame.insert(i, var)
    with open ('org.json', 'r') as r:
        data_org = json.load(r)
    label_org['text'] = data_org
    with open ('des.json', 'r') as f:
        data = json.load(f)
        data_length = len(data)
    for i in range(data_length):
        var = data[i]
        des_frame.insert(i, var)

#GUI framework and widgets

label_org = tk.Label(win, bg='white')
label_org.place(y=70, relx=0.24, relwidth=0.71, height=55)

main_frame = tk.Listbox(win, bg='light grey')
main_frame.place(y=190, relx=0.03, relwidth=0.4, height=400)

des_frame = tk.Listbox(win, bg='light grey')
des_frame.place(y=190, relx=0.44, relwidth=0.51, height=400)

v = tk.Scrollbar(main_frame)
v.pack(side = tk.RIGHT, fill = tk.Y) 
v.config(command=main_frame.yview)

label_entr = widget(0.24, 70, 0.71, 55, 'white')
label_entr.entry()

label_org = tk.Label(win, bg='white')
label_org.place(y=10, relx=0.24, relwidth=0.71, height=55)

add = widget(0.03, 70, 0.2, 55, '#3b4555')
add.button('ADD FILE TYPE',lambda: create(entry.get()))

add = widget(0.03, 10, 0.2, 55, '#3b4555')
add.button('ORIGIN',lambda: store_org())

add = widget(0.748, 130, 0.2, 55, '#3b4555')
add.button('DESTINTATION',lambda: store_des())

add = widget(0.03, 130, 0.2, 55, '#3b4555')
add.button('CLEAR',lambda: clear())

add = widget(0.44, 130, 0.3, 55, '#3b4555')
add.button('RUN',lambda: run())

add = widget(0.24, 130, 0.19, 55, '#3b4555')
add.button('DELETE',lambda: delete())

#Main loop and check data function before end after all widgets are deffined

check_data()
win.mainloop()