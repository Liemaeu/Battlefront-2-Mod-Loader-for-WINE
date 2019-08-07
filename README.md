# Battlefront-2-Mod-Loader-for-WINE
An unofficial mod loader for Star Wars: Battlefront II that runs native on GNU/Linux, macOS and BSD (with Python).

It automaticly recognizes the name of the mod by its folder name.

![alt text]()

What this mod loader does:

It renames the addme.script file into the mod folders to (de)activate them.

Installation:

Just download the SWBF2ModLoader.py.

Dependencies:

-Python3

-tkinter

How to run the script:

python3 SWBF2ModLoader.py "/path/to/Star Wars Battlefront II/GameData/addon/"

"/path/to/Star Wars Battlefront II/GameData/addon/" must be the path to your addon folder, e.g. "/home/max/.steam/steam/steamapps/common/Star Wars Battlefront II/GameData/addon/"

Alternativly you can change the value of the DefaultDirectory variable in the SWBF2ModLoader.py script from None to "/path/to/Star Wars Battlefront II/GameData/addon/". After that you can launch the mod loader with the command: python3 SWBF2ModLoader.py.

To add more mod names edit the 2 dimensional arrey ModList in the SWBF2ModLoader.py script. The syntax is: ["name of folder", "name of mod"], e.g. ["BFX", "Battlefront Extreme"].

You can report new mods by opening an issue here on GitHub or by sending me an email: liemaeu@gmail.com. Thank you very much for making this mod loader better!
