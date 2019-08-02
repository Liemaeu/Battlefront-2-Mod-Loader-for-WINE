import os
import tkinter
import sys

#Set default directory
DefaultDirectory = None


ModList = (["BFX", "Battlefront Extreme"], ["TCW", "The Clone Wars"], ["ZZZ", "AI Hero Support"], ["AAA-v1.3patch", "1.3 Patch"], ["RE1", "Realistic Geonosis"])


#Checks if a directory is given or a default directory exists
try:
    if sys.argv[1] != None:
        Directory = sys.argv[1]
except:
    if DefaultDirectory != None:
        Directory = DefaultDirectory
    else:
        print("Error. You have to run this script with the path to your addon folder or set the DefaultDirectory in this script.")
        exit()

#Saves all mods in a list
os.chdir(Directory)
Mods = list(filter(os.path.isdir, os.listdir()))

#Window
mainwindow = tkinter.Tk()
mainwindow.title("SWBF2 Mod Loader")

#Function to check if the name of the mod is in the ModList
def getName(i):
    for a in range(len(ModList)):
        if Mods[i] == ModList[a][0]:
            return ModList[a][1]
    return Mods[i] #otherwise it uses the name of the folder

#Function to enable a mod
def Enable(i):
    os.chdir(Directory + str(Mods[i]))
    os.rename('addme.script.disabled', 'addme.script')
    create() #Reloads the window to update the active label

#Function to disable a mod
def Disable(i):
    os.chdir(Directory + str(Mods[i]))
    os.rename('addme.script', 'addme.script.disabled')
    create() #Reloads the window to update the active label

#Function to create the window
def create():   
    for i in range(len(Mods)):
        tkinter.Label(text = getName(i)).grid(row=i, sticky="nsew", column=0)
        os.chdir(Directory + str(Mods[i]))
        if os.path.isfile('addme.script') is True: #Checks if the mod is active or not
            tkinter.Button(text = "Disable", command = lambda a=i:Disable(a), fg="white", bg="red").grid(row=i, sticky="nsew", column=1)
        else:
            tkinter.Button(text = "Enable", command = lambda a=i:Enable(a), fg="white", bg="green").grid(row=i, sticky="nsew", column=1)

#Creates the window
create()
mainwindow.mainloop()
