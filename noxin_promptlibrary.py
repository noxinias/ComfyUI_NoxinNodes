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
            },
        }

    RETURN_TYPES = ("STRING" ,"STRING"  ,"STRING"  ,"STRING"  ,"STRING"  ,"STRING",)
    RETURN_NAMES = ("prompt1", "prompt2", "prompt3", "prompt4", "prompt5", "prompt6",)
    
    FUNCTION = "main"
    CATEGORY = "NoxinNodes"   


    def main(self, prompt1, prompt2, prompt3, prompt4, prompt5, prompt6):
        placeholderStr = "Empty Library"
    
        if prompt1 == placeholderStr:
            prompt1 = ""    
        if prompt2 == placeholderStr:
            prompt2 = ""    
        if prompt3 == placeholderStr:
            prompt3 = ""    
        if prompt4 == placeholderStr:
            prompt4 = ""    
        if prompt5 == placeholderStr:
            prompt5 = ""    
        if prompt6 == placeholderStr:
            prompt6 = ""  
            
        return (prompt1, prompt2, prompt3, prompt4, prompt5, prompt6,)
