class NoxinPromptSave:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        
        return {
            "required": {
                "newprompt": ("STRING", {"default": "","multiline": True}),
                "librarynum": ("INT", {"default": 1, "min": 1, "max": 6, "step": 1}),
                "saveprompt": (["on", "off"], ),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "main"
    OUTPUT_NODE = True
    CATEGORY = "NoxinNodes"

    def main(self, newprompt, saveprompt, librarynum):      
        outStr = newprompt
        
        if saveprompt == "on" and newprompt != "" and newprompt != "Empty Library":   
            libraryFile = "promptlibrary" + str(librarynum) + ".txt"
            
            import os
            my_dir = os.path.dirname(os.path.abspath(__file__))  
            library_path = os.path.join(my_dir, 'library')
            library_path = os.path.join(library_path, libraryFile)        
            lines = open(library_path, "r").read().splitlines()
            
            if newprompt in lines:
                print("Noxin Prompt Save: Prompt already exists")
            else:
                print("Noxin Prompt Save: Adding new prompt")
                f = open(library_path, "a+")
                f.write(newprompt + "\n")
                f.close()               
                
        return (outStr,)
