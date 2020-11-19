#import tkinter for window with instance and title
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import marshal
import json
win = tk.Tk()
win.title("File Sorter")



height = 600
width = 800
x = 0
global widget
widget = False
global des_list
des_list = [] 


canvas = tk.Canvas(win, height=height, width=width)
canvas.pack()

def getdata():
    sto = open('origin.dat','rb')
    dat = marshal.load(sto)
    sto.close()
    frame_Label['text'] = dat


#origin folder:

def store_orgin():
    #get folder directory
    root_filename =  filedialog.askdirectory(initialdir = "/",title = "Select file")

    #store data
    sto = open('origin.dat','wb')
    marshal.dump(root_filename, sto)
    sto.close()

    #display folder directory 
    frame_Label['text'] = root_filename

def add(entry):
    
    widget = True
    sto = open('origin.dat','wb')
    marshal.dump(widget, sto)
    sto.close()

    frame_widget = tk.Frame(frame_files, bg='#7b9c9a')
    frame_widget.place(rely=0.1, relx=0.03, relwidth=0.92, relheight=0.3)

    label_type = tk.Label(frame_widget, text="FILE TYPE", bg='grey')
    label_type.place(relx=0.05, rely=0.1, relwidth=0.5, relheight=0.4)

    label_file = tk.Label(frame_widget, text=entry ,bg='grey')
    label_file.place(relx=0.05, rely=0.6, relwidth=0.5, relheight=0.3)

    global label_des
    label_des = tk.Label(frame_widget, bg='grey')
    label_des.place(relx=0.6, rely=0.6, relwidth=0.35, relheight=0.3)
    
    button_des = tk.Button(frame_widget, text="DESTINATION", bg='#b35454', bd=0, font=40, command=lambda: store_des())
    button_des.place(relx=0.6,  rely=0.1, relwidth=0.35, relheight=0.4)

def store_des():
    #get folder directory 
    global x
    des_filename =  filedialog.askdirectory(initialdir = "/",title = "Select file")
    des_list.append(des_filename)
    #store data

    with open('file.json', 'w') as f:
        json.dump(des_list, f)
    
    print(des_list)


def getlist():
   pass

#Adding widgets for file types

frame = tk.Frame(win, bg='grey')
frame.place(relx=0.03, rely=0.03, relwidth=0.6, relheight=0.1)

entry = tk.Entry(frame, font=40)
entry.place(relx=0.05, rely=0.15, relheight=0.7, relwidth=0.6)

button = tk.Button(frame, text="ADD", font=40, bg='#b35454', bd=0, command=lambda: add(entry.get()))
button.place(relx=0.7, rely= 0.15, relheight=0.7, relwidth=0.25,)

#added files list

frame_list = tk.Frame(win, bg='#7b9c9a')
frame_list.place(rely=0.2, relx=0.03, relwidth=0.92, relheight=0.75)

label = tk.Label(frame_list, text="ADDED FILES", bg='grey')
label.place(relx=0.05, rely=0.05, relwidth=0.7, relheight=0.1)

frame_files = tk.Frame(frame_list, bg='white')
frame_files.place(rely=0.35, relx=0.05, relwidth=0.90, relheight=0.6)

frame_Label = tk.Label(frame_list, bg='white')
frame_Label.place(rely=0.2, relx=0.05, relwidth=0.90, relheight=0.1)

button_orgin = tk.Button(frame_list, text="Origin", bg='#b35454', bd=0, font=40, command=lambda: store_orgin())
button_orgin.place(relx=0.76,  rely=0.05, relwidth=0.19, relheight=0.1)

#run button

frame_run = tk.Frame(win, bg='#7b9c9a')
frame_run.place(relx=0.65, rely=0.03, relwidth=0.3, relheight=0.1)

button_run = tk.Button(frame_run, text="RUN", font=40, bg='#b35454', bd=0)
button_run.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

getlist()
getdata()
#main loop for GUI
win.mainloop()
