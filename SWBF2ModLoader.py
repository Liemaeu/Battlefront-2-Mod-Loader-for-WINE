import os
import tkinter
import sys

#Set default directory
DefaultDirectory = None

#List of the mod names
ModList = (["BF3", "Battlefront III Legacy"], ["MAV", "KOTOR"], ["BDT", "The Dark Times"], ["TOR", "TORfront"], ["GZB", "Battles of the Storm #1"], ["KHS", "Battles of the Storm #2"], ["KYC", "Battles of the Storm #3"], ["MFT", "Battles of the Storm #4"], ["MSF", "Battles of the Storm #5"], ["RCM", "Republic Commando #1"], ["ZRC", "Republic Commando #2"], ["BFP", "The Battlefront Project"], ["TOW", "Tides of War"], ["ABG", "Designated Days"], ["ABC", "Clone Wars Extended"], ["UCW", "Ultimate Battlefront: The Clone Wars"], ["CWG", "Clone Wars Geonosis"], ["CWT", "Battlefront II Clone Wars"], ["025", "The Battles of the Clone Wars #1"], ["AOV", "The Battles of the Clone Wars #2"], ["CMW", "The Battles of the Clone Wars #3"], ["TBW", "The Battles of the Clone Wars #4"], ["BRS", "Scarif MP"], ["BFX", "Battlefront Extreme"], ["TCW", "The Clone Wars"], ["ZZZ", "A New Frontier"], ["AAA-v1.3patch", "Unofficial 1.3 Patch"], ["RE1", "Realistic Geonosis"])


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
mainwindow.geometry("500x800")

#Function to check if the name of the mod is in the ModList
def getName(i):
    for a in range(len(ModList)):
        if Mods[i] == ModList[a][0]:
            return ModList[a][1]
    return "Unknown"

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
        tkinter.Label(frame, text = getName(i)).grid(row=i, sticky="nsew", column=0) #name of the mod
        tkinter.Label(frame, text = Mods[i], fg="grey").grid(row=i, sticky="nsew", column=1) #name of the mod folder
        os.chdir(Directory + str(Mods[i]))
        if os.path.isfile('addme.script') is True: #Checks if the mod is active or not
            tkinter.Button(frame, text = "Disable", command = lambda a=i:Disable(a), fg="white", bg="red").grid(row=i, sticky="nsew", column=2)
        else:
            tkinter.Button(frame, text = "Enable", command = lambda a=i:Enable(a), fg="white", bg="green").grid(row=i, sticky="nsew", column=2)

#Adds scrollbars
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = tkinter.Canvas(mainwindow, borderwidth=0)
frame = tkinter.Frame(canvas)
vsb = tkinter.Scrollbar(mainwindow, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
hsb = tkinter.Scrollbar(mainwindow, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=hsb.set)

vsb.pack(side="right", fill="y")
hsb.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))            
            
#Creates the window
create()
mainwindow.mainloop()
