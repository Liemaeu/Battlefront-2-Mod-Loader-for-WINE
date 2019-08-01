import os
import tkinter
import sys


DefaultDirectory = None


try:
    if sys.argv[1] != None:
        Directory = sys.argv[1]
except:
    if DefaultDirectory != None:
        Directory = DefaultDirectory
    else:
        print("Error. You have to run this script with the path to your addon folder or set the DefaultDirectory in this script.")
        exit()


os.chdir(Directory)
Mods = list(filter(os.path.isdir, os.listdir()))


mainwindow = tkinter.Tk()
mainwindow.title("SWBF2 Mod Loader")

def Enable(i):
    os.chdir(Directory + str(Mods[i]))
    try:
        os.rename('addme.script.disabled', 'addme.script')
    except:
        pass
    create()


def Disable(i):
    os.chdir(Directory + str(Mods[i]))
    try:
        os.rename('addme.script', 'addme.script.disabled')
    except:
        pass
    create()

def create():   
    for i in range(len(Mods)):
        tkinter.Label(text = Mods[i]).grid(row=i, sticky="nsew", column=0)
        tkinter.Button(text = "Enable", command = lambda a=i:Enable(a)).grid(row=i, sticky="nsew", column=1)
        tkinter.Button(text = "Disable", command = lambda b=i:Disable(b)).grid(row=i, sticky="nsew", column=2)
        os.chdir(Directory + str(Mods[i]))
        if os.path.isfile('addme.script') is True:
            tkinter.Label(text = "active", fg="green").grid(row=i, sticky="nsew", column=3)
        else:
            tkinter.Label(text = "inactive", fg="red").grid(row=i, sticky="nsew", column=3)


create()

mainwindow.mainloop()