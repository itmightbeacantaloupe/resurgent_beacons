import numpy as np

MC_runs = 100  # configurable , for same runs with different inputs
Seed = 25   # configurable , for reproducible testing

# configurable
pulsars = [
    {
        "name": "PSR_A",
        "direction": np.array([0.42, 0.42, 0.42]),  # position by unit vector
        "mean_photon_rate": 180.0,  # photons/s
        "pulse_period": 0.041,  # s
        "pulse_width": 0.002,  # s
        "clock_bias": 2e-6,  # s
        "noise_std": 5e-7  # s
    },
    {
        "name": "PSR_B",
        "direction": np.array([-0.42, 0.91, 0.27]),
        "mean_photon_rate": 120.0,
        "pulse_period": 0.079,
        "pulse_width": 0.003,
        "clock_bias": -1e-6,
        "noise_std": 3e-7
    },
    {
        "name": "PSR_c",
        "direction": np.array([0.22, -0.31, -0.09]),
        "mean_photon_rate": 150.0,
        "pulse_period": 0.051,
        "pulse_width": 0.005,
        "clock_bias": 3e-6,
        "noise_std": 2e-7
    },
    {
        "name": "PSR_d",
        "direction": np.array([-0.22, 0.22, 0.32]),
        "mean_photon_rate": 190.0,
        "pulse_period": 0.042,
        "pulse_width": 0.004,
        "clock_bias": -3e-6,
        "noise_std": 4e-7
    }
]


def pulse_profile(t, period, width):  # for toa
    return np.exp(-0.5 * ((t % period - period / 2) / width) ** 2)
