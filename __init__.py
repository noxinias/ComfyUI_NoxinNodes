from .noxin_chimenode import *
from .noxin_scaledresolution import *
from .noxin_promptlibrary import *
from .noxin_saveprompt import *



# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "NoxinChime": NoxinChime,
    "NoxinScaledResolution": NoxinScaledResolution,
    "NoxinPromptLoad": NoxinPromptLoad,
    "NoxinPromptSave": NoxinPromptSave
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "NoxinChime": "Noxin Complete Chime",
    "NoxinScaledResolution": "Noxin Scaled Resolutions",
    "NoxinPromptLoad": "Load from Noxin Prompt Library",    
    "NoxinPromptSave": "Save to Noxin Prompt Library"    
}