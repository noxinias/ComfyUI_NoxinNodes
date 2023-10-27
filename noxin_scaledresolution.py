class NOXSCALEDRES:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "SD15_WIDTH": ("INT", {"default": 512}),
                "SD15_HEIGHT": ("INT", {"default": 512}),
                "SDXL_WIDTH": ("INT", {"default": 1024}),
                "SDXL_HEIGHT": ("INT", {"default": 1024}),
                "SDXL_MODE": (["off", "on"], ),
                "UPSCALEFACTOR": ("FLOAT", {"default": 2.0}),
            },
        }

    RETURN_TYPES = ("INT","INT","INT","INT")
    RETURN_NAMES = ("WIDTH","HEIGHT","RAW_WIDTH","RAW_HEIGHT")

    FUNCTION = "main"

    #OUTPUT_NODE = False

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
        return (finalWidth,finalHeight,targetWidth,targetHeight)