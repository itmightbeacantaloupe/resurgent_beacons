import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from config import pulse_profile


def pulsar_simulation(pulsar, duration=0.1, dt=5e-4):
    t = np.arange(0, duration, dt)
    phase_shift = np.random.uniform(0, pulsar["pulse_period"])  # randomized

    pure_signal = pulse_profile(t + phase_shift, pulsar["pulse_period"], pulsar["pulse_width"])  # non-bias
    flawed_t = t + pulsar["clock_bias"] + phase_shift  # biased

    noise_signal = pulse_profile(flawed_t, pulsar["pulse_period"], pulsar["pulse_width"])
    noise = np.random.normal(0, pulsar["noise_std"], size=len(t))  # cosmic noise

    observ_signal = noise_signal + noise
    true_toa = phase_shift + pulsar["pulse_period"]/2

    return t, pure_signal, observ_signal, true_toa
