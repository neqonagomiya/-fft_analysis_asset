import argparse
import numpy as np
import soundfile as sf

from cl import Colin
cl = Colin()

parser = argparse.ArgumentParser(
        description="You can record using this code by specifying input/output audio device."
        )
parser.add_argument("--save_wav",
                    action="store_true",
                    help="This is flag to save data as .wav.")
args = parser.parse_args()

fs = 48000.0
f0 = 440.0
A = 1.0
duration = 3.0
filename = f"sin_{int(f0)}_{int(duration)}s"

arr = np.arange(int(fs*duration))
sin = A * np.sin(2.0*np.pi*f0/fs*arr)
sin_wav = np.array(sin * (2**15 - 1)).astype(np.int16)# normalization for int16 (-32768~32767)


print(cl.cstr("save as:", color=cl.BLUE))
np.save(f"{filename}.npy", sin_wav)
print("-> " + f"{filename}.npy")
if args.save_wav==True:
    sf.write(f"{filename}.wav", sin_wav, int(fs))
    print("-> " + f"{filename}.wav")

print(cl.cstr("fin"))
