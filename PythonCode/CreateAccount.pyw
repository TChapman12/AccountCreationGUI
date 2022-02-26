# Imports #

import tkinter as tk
from tkinter import *

# Window & Config Start #

root = tk.Tk(className='Login')
root.geometry("400x200")

# Entry Variables #

entry1 = tk.StringVar()
entry2 = tk.StringVar()
entry3 = tk.StringVar()
entry4 = tk.StringVar()
    
# Entry Boxes # 

entrybox1 = tk.Entry(root, textvariable=entry1)
entrybox1.pack()

entrybox2 = tk.Entry(root, textvariable=entry2)
entrybox2.pack()

entrybox3 = tk.Entry(root, textvariable=entry3)
entrybox3.pack()

entrybox4 = tk.Entry(root, textvariable=entry4)
entrybox4.pack()

# Definitions #

def submitall():
    var1 = ""
    var2 = ""
    var3 = ""
    var4 = ""
    f = open("info", "w")
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
    
submit = tk.Button(root, text="submit", command=submitall)
submit.pack()

# Config End #

root.mainloop()

# Window End #