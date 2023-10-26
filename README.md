# ComfyUI_NoxinNodes
Utility nodes for ComfyUI that I created for me but am happy to share.

noxin_chimenode:

This node grants the ability to trigger a sound file via the operating system. 
It was designed to alert me that a long running ksampler batch or upscaler is done, and that there is something to review. I run from windows, so by default it points to the chimes.wav.
I am aware of the security potential of running it via operating system subprocess, but the positive is that it could be repurposed to run a sorting/external upsampling system afterwards rather than play a sound.