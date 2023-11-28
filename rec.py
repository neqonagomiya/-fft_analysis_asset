import os
import sys
import datetime
import argparse

import numpy as np
import sounddevice as sd
import soundfile as sf

from cl import Colin
cl = Colin()

parser = argparse.ArgumentParser(
        description="You can record using this code by specifying input/output audio device."
        )
parser.add_argument("-i", "--input_device_num",
                    required=True,
                    type=int,
                    help="you must specify input device num found using display_sd.py.")
parser.add_argument("-o", "--output_device_num",
                    required=True,
                    type=int,
                    help="you must specify output device num found using display_sd.py.")
parser.add_argument("--save_wav",
                    action="store_true",
                    help="This is flag to save data as .wav.")

args = parser.parse_args()


dtype = "float32" # default value of lib-sounddevice
fs = 48000.0
channels = 1
duration = 3.0

sd.default.dtype = dtype
sd.default.samplerate = int(fs)
sd.default.channels = channels
sd.default.device = [args.input_device_num, args.output_device_num] # [input_device_num, output_device_num]

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
rec_filename = f"recdata_{now}"

# rec
print(cl.cstr("start ") + "rec")
try:
    recdata = sd.rec(int(duration*fs))
    sd.wait()
except KeyboardInterrupt:
    print(cl.cstr("Recording was FORCED to stop!"))
    sys.exit(1)

print(cl.cstr("Done ") + "rec")

# save file
print(cl.cstr("save as:", color=cl.BLUE))
np.save(f"{rec_filename}.npy", recdata)
print("-> " + f"{rec_filename}.npy")
if args.save_wav==True:
    sf.write(f"{rec_filename}.wav", recdata, int(fs))
    print("-> " + f"{rec_filename}.wav")

print(cl.cstr("fin"))
