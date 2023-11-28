import os
import sys
import argparse

import numpy as np

from cl import Colin
cl = Colin()

parser = argparse.ArgumentParser(
        description="you can convert .npy to .csv, and opposit using this code (only support .npy or .csv)."
        )
parser.add_argument("-f", "--filename",
                    required=True,
                    type=str,
                    help="you must specify the file you want to convert (only support .npy or .csv).")

args = parser.parse_args()

filename = args.filename
filename_no_ext = os.path.splitext(filename)[0]
ext = os.path.splitext(filename)[1]


if os.path.isfile(filename) == False:
    print(cl.cstr("file does NOT exist."))
    sys.exit(1)

if ext == ".npy":
    data = np.load(f"{filename_no_ext}.npy")
    np.savetxt(f"{filename_no_ext}.csv", data, delimiter=",")
elif ext == ".csv":
    data = np.loadtxt(f"{filename_no_ext}.csv", delimiter=",")
    np.save(f"{filename_no_ext}.npy", data)
else:
    print(cl.cstr("NOT supported file."))
    sys.exit(1)

print(cl.cstr("fin"))
