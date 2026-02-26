import numpy as np


def non_ai_toa(t, signal):
    idx = np.argmax(signal)
    return t[idx]
