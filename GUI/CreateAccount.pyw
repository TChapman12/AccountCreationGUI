# Imports #

from audioop import cross
import tkinter as tk
from tkinter import *

# Window & Config Start #

root = tk.Tk(className='Create Account')
root.geometry("395x200")
root.config(bg='#3c4454')
root.resizable(False, False)
root.title("Create Account")

# Entry Variables #

entry1 = tk.StringVar()
entry2 = tk.StringVar()
entry3 = tk.StringVar()
entry4 = tk.StringVar()

# Labels #

label1 = tk.Label(root, text="Username: ", font=16, bg='#3c4454', fg='White')
label1.pack(anchor=W ,ipady=10, ipadx=10) 
label2 = tk.Label(root, text="Email: ", font=16, bg='#3c4454', fg='White')
label2.pack(anchor=W ,ipady=10, ipadx=10) 
label3 = tk.Label(root, text="Password: ", font=16, bg='#3c4454', fg='White')
label3.pack(anchor=W ,ipady=10, ipadx=10) 
label3 = tk.Label(root, text="Comfirm Password: ", font=16, bg='#3c4454', fg='White')
label3.pack(anchor=W ,ipady=10, ipadx=10)

# Entry Boxes # 

entrybox1 = tk.Entry(root, width=35, bg='LightGray', textvariable=entry1)
entrybox1.place(x=105, y=11)
entrybox2 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry2)
entrybox2.place(x=65, y=54)
entrybox3 = tk.Entry(root, width=36, bg='LightGray', textvariable=entry3)
entrybox3.place(x=97, y=97)
entrybox4 = tk.Entry(root, width=26, bg='LightGray', textvariable=entry4)
entrybox4.place(x=176, y=140)

# Definitions #

def submitall():
    var1 = ""
    var2 = ""
    var3 = ""
    var4 = ""
    f = open("GUI/AccountInfo.txt", "w")
    var1 += entry1.get()
    var2 += entry2.get()
    var3 += entry3.get()
    var4 += entry4.get()
    [...]
    f.write(var1 + '\n')
    f.write(var2 + '\n')
    f.write(var3 + '\n')
    f.write(var4 + '\n')
    f.close()

# Buttons #
    
submit = tk.Button(root, text="Submit", command=submitall, cursor='plus', bg='#3c4454', fg='White', activebackground='#3c4454', activeforeground='Green', bd=False)
submit.pack(fill=X)

# Config End #

root.mainloop()

# Window End #