import os
import tkinter
import sys

#Set default directory
DefaultDirectory = None

#List of the mod names
ModList = (["BFX", "Battlefront Extreme"], ["TCW", "The Clone Wars"], ["ZZZ", "AI Hero Support"], ["AAA-v1.3patch", "Unofficial 1.3 Patch"], ["RE1", "Realistic Geonosis"], ["ABR", "Abregado-Rae: Venezia"], ["ALS", "Aldura: Orbital Assault (space)"], ["ABC", "All Battle Crisis (Rathia Beachhead)"], ["ARF", "Ancient Research Facility"], ["AYC", "Attack in Yavin Canyons"], ["DOW", "AotC: Declaration of War"], ["NUF", "Battle For Republic City"], ["UCM", "Battle For Republic City"], ["CCC", "Coruscant Order 66: Taking the Council Chamber"], ["CX1", "Coruscant Order 66: Taking the Council Chamber"], ["CBT", "Crater Battle"], ["DCC", "DCC Clan Map"], ["EMC", "Eriadu: Mountiantop City"], ["EXG", "Exogorth"], ["OI2", "Flooded Oil Refinery"], ["FZZ", "Folzia: Dock City"], ["GAD", "Galidraan Snowcapped Forest"], ["GSP", "Gall Mountains"], ["NGE", "Geonosis: Canyons"], ["HFV", "Hoth: Frozen Valley"], ["HUG", "Hoth Underground"], ["JAG", "Jade Moon"], ["DIS", "Kadrala: Islands + XGCW Mygeeto"], ["KAF", "Kafah Minor"], ["KF1", "Kashyyyk: Forest"], ["LS1", "Los Santos"], ["MYG", "Modable Mygeeto"], ["MED", "Mos Eisley Dawn"], ["MUU", "Muunilinst: Harnaidan"], ["NTH", "Naboo: Theed Hangar"], ["DQ9", "Pestox"], ["DQ3", "Raxus Prime"], ["BOS", "Saleucami: Valley"], ["SWT", "Samaria: Wustentempel"], ["SAC", "Sarlacc Interior"], ["SSA", "Servorum: Swamp"], ["LLV", "Sraiden: Ash Forest"], ["SDA", "Star Destroyer Assault"], ["THF", "Talus: Hillside"], ["TSU", "Taris: Nightfall"], ["TSS", "Taris: Spiral Stair"], ["RGR", "The Rihaken, River of Kashyyyk"], ["TBA", "Theed: Back Alleys"], ["THR", "Thrakia: Oceanic Pass"], ["TWF", "Trench Warfare"], ["TRO", "Tropicanae"], ["NUT", "Utapau Assault"], ["VDI", "Verena Defense: Immortal"], ["VER","Veriss: Mining Colony"], ["MGA", "Vinsoth: Battle on the Plains"], ["VFD", "Virmund: City"], ["WOK", "Wonkuun"], ["WS2", "World Side"], ["XBR", "Xagobah: Ravine"], ["YAP", "Yavin 4 Ancient Pyramids"], ["ENC", "Yavin IV: Mine"])


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
        tkinter.Label(text = getName(i)).grid(row=i, sticky="nsew", column=0) #name of the mod
        tkinter.Label(text = Mods[i], fg="grey").grid(row=i, sticky="nsew", column=1) #name of the mod folder
        os.chdir(Directory + str(Mods[i]))
        if os.path.isfile('addme.script') is True: #Checks if the mod is active or not
            tkinter.Button(text = "Disable", command = lambda a=i:Disable(a), fg="white", bg="red").grid(row=i, sticky="nsew", column=2)
        else:
            tkinter.Button(text = "Enable", command = lambda a=i:Enable(a), fg="white", bg="green").grid(row=i, sticky="nsew", column=2)

#Creates the window
create()
mainwindow.mainloop()
