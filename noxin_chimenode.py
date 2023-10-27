class NoxinChime:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
    
        return {
            "required": {
                "image": ("IMAGE",),
                "playsound": (["enable", "disable"],),
                "soundPath": ("STRING", {
                    "multiline": False,
                    "default": 'C:\Windows\Media\chimes.wav'
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    
    FUNCTION = "main"
    CATEGORY = "NoxinNodes"

    def main(self, image, playsound, soundPath):
        if playsound == "enable": 
        
            import subprocess, os, platform
            if platform.system() == 'Darwin':       # macOS
                subprocess.call(('open', soundPath))
            elif platform.system() == 'Windows':    # Windows
                os.startfile(soundPath)
            else:                                   # linux variants
                subprocess.call(('xdg-open', soundPath))
        
        return (image,)
