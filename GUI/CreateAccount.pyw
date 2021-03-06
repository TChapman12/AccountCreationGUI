# Imports #

import tkinter as tk
from tkinter import *

# Window & Config Start #

root = tk.Tk(className='Create Account')
root.geometry("395x450")
root.config(bg='#3c4454')
root.resizable(False, False)
root.title("Create Account")

# Entry Variables #

entry1 = tk.StringVar()
entry2 = tk.StringVar()
entry3 = tk.StringVar()
entry4 = tk.StringVar()
entry5 = tk.StringVar()
entry6 = tk.StringVar()

# Labels #

label1 = tk.Label(root, text="First Name: ", font=16, bg='#3c4454', fg='White')
label1.pack(anchor=W ,ipady=10, ipadx=10) 
label2 = tk.Label(root, text="Last Name: ", font=16, bg='#3c4454', fg='White')
label2.pack(anchor=W ,ipady=10, ipadx=10) 
label3 = tk.Label(root, text="Username: ", font=16, bg='#3c4454', fg='White')
label3.pack(anchor=W ,ipady=10, ipadx=10) 
label4 = tk.Label(root, text="Email: ", font=16, bg='#3c4454', fg='White')
label4.pack(anchor=W ,ipady=10, ipadx=10) 
label5 = tk.Label(root, text="Password: ", font=16, bg='#3c4454', fg='White')
label5.pack(anchor=W ,ipady=10, ipadx=10) 
label6 = tk.Label(root, text="Confirm Password: ", font=16, bg='#3c4454', fg='White')
label6.pack(anchor=W ,ipady=10, ipadx=10)

# Entry Boxes # 

entrybox1 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry1)
entrybox1.pack(after=label1)
entrybox2 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry2)
entrybox2.pack(after=label2)
entrybox3 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry3)
entrybox3.pack(after=label3)
entrybox4 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry4)
entrybox4.pack(after=label4)
entrybox5 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry5)
entrybox5.pack(after=label5)
entrybox6 = tk.Entry(root, width=40, bg='LightGray', textvariable=entry6)
entrybox6.pack(after=label6)

# Definitions #

def submitall():
    var1 = ""
    var2 = ""
    var3 = ""
    var4 = ""
    var5 = ""
    var6 = ""
    var1 += entry1.get()
    var2 += entry2.get()
    var3 += entry3.get()
    var4 += entry4.get()
    var5 += entry5.get()
    var6 += entry6.get()
    f = open(file=(str(var1 + var2)), mode="w")
    [...]
    f.write("First Name: " + var1 + '\n')
    f.write("Last Name: " + var2 + '\n')
    f.write("Username: " + var3 + '\n')
    f.write("Email: " + var4 + '\n')
    f.write("Password: " + var5 + '\n')
    f.write("Confirm: " + var6 + '\n')
    f.write(" " + '\n')
    f.close()

# Buttons #
    
submit = tk.Button(root, text="Submit", command=submitall, cursor='plus', bg='#3c4454', fg='White', activebackground='#3c4454', activeforeground='Green', bd=False)
submit.pack(side=BOTTOM, fill=X)

# Config End #

root.mainloop()

# Window End #
