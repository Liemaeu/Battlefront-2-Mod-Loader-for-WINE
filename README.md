# Battlefront-2-Mod-Loader-for-WINE
An unofficial mod loader for Star Wars: Battlefront II that run native on GNU/Linux, macOS and BSD (with Python)

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

Alternativly you can change the vaule of the DefaultDirectory variable in the SWBF2ModLoader.py script from None to "/path/to/Star Wars Battlefront II/GameData/addon/". After that you can launch the mod loader with the command: python3 SWBF2ModLoader.py.
