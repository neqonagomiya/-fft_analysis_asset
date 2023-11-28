import os
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as pticker

from cl import Colin
cl = Colin()

parser = argparse.ArgumentParser(
        description="you can display and analysis data using FFT (only support .npy or .csv)."
        )
parser.add_argument("-f", "--filename",
                    required=True,
                    type=str,
                    help="you must specify the data_file you want to analysis (only support .npy or .csv).")

args = parser.parse_args()

fs = 48000.0
filename = args.filename
filename_no_ext = os.path.splitext(filename)[0]
ext = os.path.splitext(filename)[1]

if os.path.isfile(filename) == False:
    print(cl.cstr("file does NOT exist."))
    sys.exit(1)

if ext == ".npy":
    data = np.load(filename)
elif ext == ".csv":
    data = np.loadtxt(filename, delimiter=",")
else:
    print(cl.cstr("NOT supported file."))
    sys.exit(1)

N = len(data)
window = np.hanning(N)
data_w = window * data
tscale = np.arange(N)/fs
fscale = np.fft.fftfreq(N, d=1.0/fs)
norm_F = np.fft.fft(data_w) / (N/2.0) # normalization
acf = 1/(np.sum(window)/N) # Correction value of window_func
norm_F = norm_F * acf # Correction
amp_F = np.abs(norm_F)
Power_F = amp_F ** 2

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

fig.subplots_adjust(bottom=0.15, wspace=0.0, hspace=0.6)

ax1.set_title("time_domain", y=-0.5)
ax1.set_xlabel("time[sec]")
ax1.set_ylabel("Amp")
ax1.plot(tscale, data, label="t_data")

ax2.set_title("frequency_domain", y=-0.5)
ax2.set_xlabel("fequency[Hz]")
ax2.set_xlim(0, fs/2) # = fscale[:N//2] and Power_F[:N//2]
ax2.set_ylabel("Power")
ax2.plot(fscale, Power_F, label="f_data")

ax1.legend()
ax2.legend()

ax1.yaxis.set_major_formatter(pticker.ScalarFormatter(useMathText=True)) # le->x10
#ax.yaxis.offsetText.set_fontsize(10)
ax1.ticklabel_format(style="sci", axis="y", scilimits=(0,0))
ax2.yaxis.set_major_formatter(pticker.ScalarFormatter(useMathText=True)) # le->x10
ax2.ticklabel_format(style="sci", axis="y", scilimits=(0,0))
plt.gca().yaxis.set_tick_params(direction="in")

#plt.tight_layout() 

plt.show()


