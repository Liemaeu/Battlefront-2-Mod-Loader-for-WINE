# Battlefront-2-Mod-Loader-for-WINE
An unofficial mod loader for Star Wars: Battlefront II that runs natively on GNU/Linux, macOS and *BSD.

It **automatically recognizes the name of the mod** by its folder name (nearly every mod from ModDB.com, 166 at the moment).

![Screenshot](https://raw.githubusercontent.com/Liemaeu/Battlefront-2-Mod-Loader-for-WINE/master/Screenshot.png)

## What this mod loader does

It renames the addme.script file in the mod folder to (de)activate them.

## Installation

Just download the SWBF2ModLoader.py file.

## Dependencies

- Python3

- tkinter

## How to run the script

`python3 SWBF2ModLoader.py "/path/to/Star Wars Battlefront II/GameData/addon/"`

"/path/to/Star Wars Battlefront II/GameData/addon/" must be the path to your addon folder, e.g. "/home/max/.steam/steam/steamapps/common/Star Wars Battlefront II/GameData/addon/"

Alternatively you can change the value of the *DefaultDirectory* variable in the SWBF2ModLoader.py script from None to "/path/to/Star Wars Battlefront II/GameData/addon/". After that you can launch the mod loader with the command: `python3 SWBF2ModLoader.py`.

## How to add more mods to the list

To add more mod names edit the 2 dimensional list *ModList* in the SWBF2ModLoader.py script. The syntax is: *["name of folder", "name of mod"]*, e.g. *["BFX", "Battlefront Extreme"]*.

You can submit new mods by opening an issue. Thank you very much!

## ERROR! label instead of enable/disable button

If there is an "ERROR!" label instead of a enable/disable button, this folder is not a valid mod (it has no addme.script/addme.script.disabled file).

If it quits with the message "Not a valid directory!" check if the "/path/to/Star Wars Battlefront II/GameData/addon/" is a correct path to a directory (do not forget the quotes ""!).
