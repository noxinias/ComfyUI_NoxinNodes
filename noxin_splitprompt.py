class NoxinSplitPrompt:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        
        return {
            "required": {
                "loraword": ("STRING", {"display": "slider", "default": "","multiline": False}),
                "subject": ("STRING", {"default": "","multiline": False}),
                "clothing": ("STRING", {"default": "","multiline": False}),
                "setting": ("STRING", {"default": "","multiline": False}),
                "photography": ("STRING", {"default": "","multiline": False}),
                "face": ("STRING", {"default": "","multiline": False}),
                "default_positive": ("STRING", {"default": "","multiline": False}),
                "specific_negative": ("STRING", {"default": "","multiline": False}),   
                "default_negative": ("STRING", {"default": "","multiline": False}),               
                "orderstring": ("STRING", {"default": "loraword,subject,clothing,setting,photography,face,default_positive","multiline": False}),
                "delimiter": ("STRING", {"default": ",", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING"  ,"STRING"  ,"STRING"   ,"STRING"  ,"STRING"      ,"STRING","STRING"           ,"STRING"           ,"STRING"          ,"STRING","STRING",)
    RETURN_NAMES = ("loraword", "subject", "clothing", "setting", "photography", "face" , "default_positive","specific_negative","default_negative","Combo+", "Combo-",)

    FUNCTION = "main"
    CATEGORY = "NoxinNodes"

    def main(self, loraword, subject, clothing, setting, photography, face, default_positive, specific_negative, default_negative, orderstring, delimiter):      
        sections = [loraword, subject, clothing, setting, photography, face, default_positive, specific_negative, default_negative]
        sectionNames = ["loraword", "subject", "clothing", "setting", "photography", "face", "default_positive"]
        
        default_order = "loraword,subject,clothing,setting,photography,face,default_positive"
        
        orderstring = orderstring.replace(" ","") #strip spaces
        orderstring = orderstring.lower()
        orderstring = orderstring.split(",")
        delim = delimiter

        ind = 0
        fullPrompt = ""
        for sectionName in orderstring:
            sectionIndex = sectionNames.index(sectionName)
            sectionData = sections[sectionIndex]
            fullPrompt = fullPrompt + sectionData
            if ind < len(orderstring)-1 and sectionData != "":
                fullPrompt = fullPrompt + delim

            ind = ind + 1

        postivePrompt = fullPrompt
        negativePrompt = specific_negative + delim + default_negative

        print("Combined Prompt+: " + postivePrompt)
        print("Combined Prompt-: " + negativePrompt)

        return (loraword, subject, clothing, setting, photography, face, default_positive, specific_negative, default_negative, postivePrompt, negativePrompt)
