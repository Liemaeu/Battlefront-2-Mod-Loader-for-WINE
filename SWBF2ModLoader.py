import os
import tkinter
import sys

#Set default directory
DefaultDirectory = None

#List of the mod names
ModList = (["MAP", "Mygeeto Assault: Protector"], ["MMD", "Manaan: Murky Depths"], ["PLS", "Polus: Port District"], ["RVT", "RHEN VAR: TEMPLE"], ["TCC", "Tatooine: Dusk of War"], ["TJW", "Tatooine: Outpost"], ["ABH", "Aaris III: Beachhead"], ["ASL", "Bakura: Town Assault"], ["BOC", "Battle Over Coruscant"], ["BOM", "Battle of Ord Mantell"], ["BOT", "Toola: Frozen Tundra"], ["CER", "Cerea: Moonlit Meele"], ["CS1", "Capital Strike"], ["NAT", "Agamar: Forest"], ["CBM", "Utapau Attack"], ["CCS", "Corella: Shores"], ["CO1", "Coruscant: City"], ["CO2", "Coruscant: Streets"], ["GFR", "Genisis: Lost City"], ["YYY", "Kashyyyk: Episode 3"], ["MTA", "Metrion Aristan"], ["MCW", "Mygeeto"], ["BHA", "Khimera"], ["FR3", "Khimera: Jungle"], ["NSA", "Nar Shaddaa: Eon City"], ["LSD", "Pepperland"], ["JR5", "Ruuria: Jungle Ruins"], ["PGS", "Pegasus"], ["RVR", "Rhen Var: Droid Factory"], ["SK6", "Shakara VI: Swamp Assault"], ["TLC", "The Lost City"], ["YHR", "Yavin 4: Hidden Ruins"], ["VOD", "Yavin IV: Valley of Deceit"], ["JAG", "Jade Moon"], ["ASP", "Alaris Prime: Assault"], ["CSH", "Cerea: Savage Hunt"], ["DTB", "Coruscant: Downtown Battle"], ["FAL", "EP3: Felucia"], ["NGE", "Geonosis: Canyons"], ["KUA", "Kuat: Island"], ["ERB", "Genesis - Endor riverbed"], ["TAS", "Genesis - Tatooine streets"], ["HTR", "Genesis - Hoth trenches"], ["Y4R", "Genesis - Yavin IV ruins"], ["DSH", "Genesis - Death star hangar"], ["KAI", "Genesis - Kamino invasion"], ["RRF", "Urban - Rhen Var: Ruins"], ["RNF", "Urban - Rori: Narmal"], ["KCF", "Urban - Kashyyyk Tree Village"], ["COF", "Urban - Coruscant"], ["ACT", "Urban - Anchorhead"], ["LEG", "Legends Reboot"], ["NBP", "Battlefront Ultimate Commander #6"], ["BPF", "Battlefront Ultimate Commander #5"], ["BCC", "Battlefront Ultimate Commander #4"], ["BOZ", "Battlefront Ultimate Commander #3"], ["ADA", "Battlefront Ultimate Commander #2"], ["BU1", "Battlefront Ultimate Commander #1"], ["ALD", "Aldura Campaign"], ["DAC", "Dantooine City"], ["DAS", "Dantooine Swamp"], ["DLZ", "Dantooine Landing Zone"], ["SUL", "Sullust: Barracks"], ["CRS", "Christophsis: Chaleydonia City"], ["GEA", "Geonosis: Arena"], ["ABD", "Homefront"], ["VNE", "The Core of Galaxy #6"], ["TYH", "The Core of Galaxy #5"], ["TRB", "The Core of Galaxy #4"], ["EP3", "The Core of Galaxy #3"], ["CVA", "The Core of Galaxy #2"], ["AIH", "The Core of Galaxy #1"], ["QXY","Itshadezs Coruscant Invasion"], ["JVC", "Itshadezs Jedi v Clones"], ["JTV", "Itshadezs Jedi Temple order 66"], ["DDA", "Itshadezs Darda Beach"], ["JP4", "Jedi Purge: Coruscant"], ["JP3", "Jedi Purge: Atoa"], ["Y4P", "Yavin IV Plateu"], ["TTC", "Battlefront: Reimagined"], ["JP2", "Jedi Purge: Kessel"], ["JP1", "Jedi Purge: Kashyyyk"], ["MCL", "Dxun: Remnants of the Sith Lords"], ["CHR", "Christophsis"], ["TRS", "Siege of Tritium"], ["ROE", "Rise Of Elite"], ["FRT", "BF3: Tatooine"], ["CWM", "The last space battle"], ["TEP", "The Eclipse"], ["JGG", "Jakku: Graveyard of Giants"], ["FUH", "The Force Unleashed II and a Half"], ["SSB", "Scarif: Space Battle"], ["4TC", "Rumble Conquest"], ["WFE", "War For Existance"], ["GTS", "Ground To Space Example"], ["THB", "Hellish Battle"], ["O66", "Order 66"], ["NEW", "Valley Escape"], ["NS1", "Trash Battle: Noscope only"], ["PEP", "Ready For Battle: Execution"], ["BSW", "Boda: Swamp"], ["JLS", "Jedha: Last Stand"], ["STR", "SOLO: Train Heist"], ["DJJ", "Darth Jar Jar"], ["SMK", "Kessel Mines"], ["AAO", "Ilum: Assault on Frozen Bunker"], ["GEN", "Geonosis: The Second Day"], ["NGL", "Grasslands Fight-Naboo"], ["MNM", "The Ultimate Sides"], ["GCW", "GCW-1035"], ["TAW", "Tatooine At War"], ["TFA", "Galactic Civil War II"], ["RDX", "Battlefront Redux"], ["LEL", "Galactic Marines"], ["KTR", "Knights of War"], ["Y8T", "Yavin 8: Tundra"], ["AON", "Galactic Assault on Naboo"], ["AOG", "Galactic Assault on Geonosis"], ["NDS", "Elite Squadron (DS)"], ["ESQ", "Elite Squadron (PSP)"], ["BAM", "Last Hope"], ["ECW", "Republic Combat"], ["FUK", "Mandalorians"], ["0CW", "City Watch"], ["AOT", "Naboo: Assault on Theed"], ["BOJ", "Battle of Jakku"], ["2SW", "The Sith Wars II"], ["BF3", "Battlefront III Legacy"], ["MAV", "KOTOR"], ["BDT", "The Dark Times"], ["TOR", "The Old Republic"], ["GZB", "Battles of the Storm #1"], ["KHS", "Battles of the Storm #2"], ["KYC", "Battles of the Storm #3"], ["MFT", "Battles of the Storm #4"], ["MSF", "Battles of the Storm #5"], ["RCM", "Republic Commando #1"], ["ZRC", "Republic Commando #2"], ["BFP", "The Battlefront Project"], ["TOW", "Tides of War"], ["ABG", "Designated Days"], ["ABC", "Clone Wars Extended"], ["UCW", "Ultimate Battlefront: The Clone Wars"], ["CWG", "Clone Wars Geonosis"], ["CWT", "Battlefront II Clone Wars"], ["025", "The Battles of the Clone Wars #1"], ["AOV", "The Battles of the Clone Wars #2"], ["CMW", "The Battles of the Clone Wars #3"], ["TBW", "The Battles of the Clone Wars #4"], ["BRS", "Scarif MP"], ["BFX", "Battlefront Extreme"], ["TCW", "The Clone Wars"], ["ZZZ", "A New Frontier"], ["AAA-v1.3patch", "Unofficial 1.3 Patch"], ["RE1", "Realistic Geonosis"])


#Checks if a directory is given or a default directory exists
try:
    if sys.argv[1] != None:
        Directory = sys.argv[1]
except:
    if DefaultDirectory != None:
        Directory = DefaultDirectory
    else:
        print("Error! You have to run this script with the path to your addon folder or set the DefaultDirectory in this script.")
        exit()

#Saves all mods in a list
os.chdir(Directory)
Mods = list(filter(os.path.isdir, os.listdir()))

#Window
mainwindow = tkinter.Tk()
mainwindow.title("SWBF2 Mod Loader")
mainwindow.geometry("600x800")

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
