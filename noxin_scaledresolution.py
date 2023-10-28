class NoxinScaledResolution:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "SD15_WIDTH": ("INT", {"default": 512}),
                "SD15_HEIGHT": ("INT", {"default": 512}),
                "SDXL_WIDTH": ("INT", {"default": 1024}),
                "SDXL_HEIGHT": ("INT", {"default": 1024}),
                "SDXL_MODE": (["off", "on"], ),
                "UPSCALEFACTOR": ("FLOAT", {"round": "False", "default": 2.0}),
            },
        }

    RETURN_TYPES = ("INT","INT","INT","INT","FLOAT")
    RETURN_NAMES = ("WIDTH","HEIGHT","RAW_WIDTH","RAW_HEIGHT","UPSCALEFACTOR")

    FUNCTION = "main"
    CATEGORY = "NoxinNodes"

    def main(self, SD15_WIDTH, SD15_HEIGHT, SDXL_WIDTH, SDXL_HEIGHT, UPSCALEFACTOR, SDXL_MODE):
        finalWidth = 0
        finalHeight = 0
        if SDXL_MODE == "off":
            targetWidth = SD15_WIDTH
            targetHeight = SD15_HEIGHT
        else:
            targetWidth = SDXL_WIDTH
            targetHeight = SDXL_HEIGHT        
            
        finalWidth = int(targetWidth * UPSCALEFACTOR)
        finalHeight = int(targetHeight * UPSCALEFACTOR)
        
        print("Running scaled node")
        return (finalWidth,finalHeight,targetWidth,targetHeight, UPSCALEFACTOR)