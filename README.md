# ComfyUI_NoxinNodes
Utility nodes for ComfyUI that I created for me but am happy to share.

noxin_chimenode:

This node grants the ability to trigger a sound file via the operating system. 
It was designed to alert me that a long running ksampler batch or upscaler is done, and that there is something to review. I run from windows, so by default it points to the chimes.wav.
I am aware of the security potential of running it via operating system subprocess, but the positive is that it could be repurposed to run a sorting/external upsampling system afterwards rather than play a sound.

noxin_scaledresolution:

This node provides both raw and multiplied values of height and width, with a built in switch for SD1.5 and SDXL - I hated having to multiply them with multiple nodes and convert between floats and ints.

noxin_promptlibrary + noxin_saveprompt:

Allows you to read from library text files in this folder from a single node, as well as save any non-existing prompts into that library via the save node. Try out the attached workflows for an example of use.