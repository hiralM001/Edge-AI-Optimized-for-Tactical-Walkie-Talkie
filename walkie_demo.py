import pyaudio
import ctypes
import numpy as np

# 1. RNNoise AI Setup
try:
    rnnoise = ctypes.CDLL("librnnoise.so")
except:
    rnnoise = ctypes.CDLL("/usr/local/lib/librnnoise.so")

rnnoise.rnnoise_create.restype = ctypes.c_void_p
rnnoise.rnnoise_create.argtypes = [ctypes.c_void_p]
rnnoise.rnnoise_process_frame.restype = ctypes.c_float
rnnoise.rnnoise_process_frame.argtypes = [
    ctypes.c_void_p, 
    ctypes.POINTER(ctypes.c_float), 
    ctypes.POINTER(ctypes.c_float)
]

st = rnnoise.rnnoise_create(None)

# 2. Audio Processing Parameters
CHUNK = 4800  # Optimized for smooth Bluetooth streaming
RATE = 48000
FORMAT = pyaudio.paInt16
CHANNELS = 1

p = pyaudio.PyAudio()
usb_in = None

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if "USB" in dev['name'] or "PnP" in dev['name'] or "Audio Device" in dev['name']:
        if dev['maxInputChannels'] > 0 and usb_in is None: 
            usb_in = i

try:
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    input_device_index=usb_in,
                    output_device_index=2, # Bluetooth Audio Output
                    frames_per_buffer=CHUNK)

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_float = np.frombuffer(data, dtype=np.int16).astype(np.float32)
        out_floats = np.zeros(CHUNK, dtype=np.float32)

        for i in range(0, CHUNK, 480):
            in_ptr = audio_float[i:i+480].ctypes.data_as(ctypes.POINTER(ctypes.c_float))
            out_ptr = out_floats[i:i+480].ctypes.data_as(ctypes.POINTER(ctypes.c_float))
            rnnoise.rnnoise_process_frame(st, out_ptr, in_ptr)

        cleaned_int16 = np.clip(out_floats * 1.5, -32768, 32767).astype(np.int16)
        stream.write(cleaned_int16.tobytes())

except Exception as e:
    pass
finally:
    if 'stream' in locals():
        stream.stop_stream()
        stream.close()
    p.terminate()
