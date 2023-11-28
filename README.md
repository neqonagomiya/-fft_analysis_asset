# readme.md

## init env
```
python3 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**you can activate env**

```
. ./venv/bin/activate
```


## for running code

**you must need activation environment!!**

### code list

- [x] display_sd.py
    - you can see the available audio devices using this code.
- [x] rec.py
    - you can record using this code by specifying input/output audio device (default save data as .npy).
- [x] analysis_fft.py
    - you can display fft_graph using this code.
- [x] convert_file.py
    - you can convert .npy to .csv, and opposit using this code (only support .npy or .csv).
- [x] make_sinwav.py
    - you can make sine wave of any frequency as .wav.
- [x] cl.py
    - you can color your uncool terminal.
- [x] test_cl.py
    - you can test of cl.py.

### How to process experiment

this code **default** parameters
- samplefrequency is 48000.0

**so You have to change the some parameters you want**
**AND Experiment parameters MUST BE CONSISTENT!!!**

1. activate env

```
. ./venv/bin/activate
```

2. check connected audio devices

```
python3 display_sd.py
```
as a result,

```
> 0 MacBook Pro$N%^%$%/, Core Audio (1 in, 0 out)
< 1 MacBook Pro$N%9%T!<%+!<, Core Audio (0 in, 2 out)
  2 Microsoft Teams Audio, Core Audio (2 in, 2 out)
  3 ZoomAudioDevice, Core Audio (2 in, 2 out)
```

**You must memorize the number of input/output audio devices you use**

3. recording

```
python3 rec.py -i <input_device_num> -o <output_device_num>
```

**dafault save_file format is .npy.**
**But, you set the argument (--save_wav) like following command if you also want a .wav.**

```
python3 rec.py -i <input_device_num> -o <output_device_num> --save_wav
```

4. analysis_fft

```
python3 analysis_fft.py -f <FILENAME (only support .npy or .csv)>
```

#### option

- make_sinwav

```
python3 make_sinwav.py
```

