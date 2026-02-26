import numpy as np


def extract_peak_window(signal, window_size=20):
    idx = np.argmax(signal)

    start = max(0, idx - window_size)
    end = min(len(signal), idx + window_size)

    window = signal[start:end]

    #if near boundaries
    if len(window) < 2*window_size:
        pad_size = 2*window_size - len(window)
        window = np.pad(window, (0, pad_size))

    return window
