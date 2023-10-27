import os
my_dir = os.path.dirname(os.path.abspath(__file__))  

def getPrompts(libFileName):  
    library_path = os.path.join(my_dir, 'library')  
    library_path = os.path.join(library_path, libFileName)  
    lines = open(library_path, "r").read().splitlines()
    if len(lines) == 0:
        return ["Empty Library"]
    else:
        return [""] + lines

def getLibraries():
    library_path = os.path.join(my_dir, 'library')    
    return os.listdir(library_path)       

class NoxinPromptLoad:
    
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        
        return {
            "required": {
                "prompt1": (getPrompts('promptlibrary1.txt'),{"default": ""}),
                "prompt2": (getPrompts('promptlibrary2.txt'),{"default": ""}),
                "prompt3": (getPrompts('promptlibrary3.txt'),{"default": ""}),
                "prompt4": (getPrompts('promptlibrary4.txt'),{"default": ""}),
                "prompt5": (getPrompts('promptlibrary5.txt'),{"default": ""}),
                "prompt6": (getPrompts('promptlibrary6.txt'),{"default": ""}),
                "selectedlibrary": ("INT", {"default": 1, "min": 1, "max": 6, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    
    FUNCTION = "main"
    CATEGORY = "NoxinNodes"   


    def main(self, selectedlibrary, prompt1, prompt2, prompt3, prompt4, prompt5, prompt6):
        if selectedlibrary == 1:
            outStr = prompt1  
        elif selectedlibrary == 2:
            outStr = prompt2
        elif selectedlibrary == 3:
            outStr = prompt3
        elif selectedlibrary == 4:
            outStr = prompt4
        elif selectedlibrary == 5:
            outStr = prompt5
        elif selectedlibrary == 6:
            outStr = prompt6
        else:
            print("Not sure how we got here, but selectedlibrary number wasn't in the allowed space. using lib 1")
            outStr = prompt1
        return (outStr,)
