class NoxinSimpleMath:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "INT1": ("INT", {"default": 0, "step": 1, "display": "number"}),
                "INT2": ("INT", {"default": 0, "step": 1, "display": "number"}),
                "FLOAT1": ("FLOAT", {"default": 0.0, "step": 0.05, "round": 0.001, "display": "number"}),
                "FLOAT2": ("FLOAT", {"default": 0.0, "step": 0.05, "round": 0.001, "display": "number"}),
                "STRING1": ("STRING", {"default": "0", "multiline": False}),
                "STRING2": ("STRING", {"default": "0", "multiline": False}),
                "VAL1SRC": (["INT", "FLOAT","STRING"],),
                "VAL2SRC": (["INT", "FLOAT","STRING"],),
                "OPERATION": (["ADD","SUB","MUL","DIV"],),            
            },
        }

    RETURN_TYPES = ("INT","FLOAT","STRING")

    FUNCTION = "main"
    CATEGORY = "NoxinNodes"

    def main(self, INT1, INT2, FLOAT1, FLOAT2, STRING1, STRING2, VAL1SRC, VAL2SRC, OPERATION):
        print("Simple Math Node")
        
        val1 = 0
        val2 = 0
        
        if VAL1SRC == "INT":
            val1 = INT1
        elif VAL1SRC == "FLOAT":
            val1 = FLOAT1        
        elif VAL1SRC == "STRING":
            val1 = float(STRING1)

        if VAL2SRC == "INT":
            val2 = INT2
        elif VAL2SRC == "FLOAT":
            val2 = FLOAT2        
        elif VAL2SRC == "STRING":
            val2 = float(STRING2)
            
        result = 0
        if OPERATION == "ADD":
            result = val1 + val2
        elif OPERATION == "SUB":
            result = val1 - val2
        elif OPERATION == "MUL":
            result = val1 * val2
        elif OPERATION == "DIV":
            result = val1 / val2
            
        finalInt = int(result)
        finalFloat = float(result)
        finalString = str(result)       
        return (finalInt, finalFloat,finalString)