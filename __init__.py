from .noxin_chimenode import *
from .noxin_scaledresolution import *
from .noxin_promptlibrary import *
from .noxin_saveprompt import *



# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "NOXCHIME": NOXCHIME,
    "NOXSCALEDRES": NOXSCALEDRES,
    "NOXPROMPTLIB_LOAD": NOXPROMPTLIB_LOAD,
    "NOXPROMPTLIB_SAVE": NOXPROMPTLIB_SAVE
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "NOXCHIME": "Noxin Complete Chime",
    "NOXSCALEDRES": "Noxin Scaled Resolutions",
    "NOXPROMPTLIB_LOAD": "Load from Noxin Prompt Library",    
    "NOXPROMPTLIB_SAVE": "Save to Noxin Prompt Library"    
}