import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from config import pulsars, MC_runs, Seed
from ai.ai_model import AITOA
from navigation.toa import non_ai_toa
from simulation.simulation import pulsar_simulation
from preprocessing.normalisation import extract_peak_window

X_train = []
y_train = []
np.random.seed(Seed)

true_toas = []
ai_toas = []
classical_toas = []

# training AI with Features through simulation data for each monte carlo run for each pulsar
for pulsar in pulsars:
    for i in range(MC_runs):
        t, pure, observed, true_toa = pulsar_simulation(pulsar)
        features = extract_peak_window(observed)  # only values from peak window for reducing dimensionality

        X_train.append(features)
        y_train.append(true_toa)



X_train = np.array(X_train)
y_train = np.array(y_train)
model = AITOA()  # calling AI component
model.train(X_train, y_train)  # training
ai_errors = []
nonai_errors = []

# evaluating Errors through simulation data for each monte carlo run for each pulsar
for pulsar in pulsars:
    for i in range(MC_runs):
        t, pure, observed, true_toa = pulsar_simulation(pulsar)
        classical_toa = non_ai_toa(t, observed)
        features = extract_peak_window(observed)
        ai_toa = model.predict(features.reshape(1, -1))[0]

        true_toas.append(true_toa)
        classical_toas.append(classical_toa)
        ai_toas.append(ai_toa)

        nonai_errors.append(abs(classical_toa - true_toa))
        ai_errors.append(abs(ai_toa - true_toa))

mean_nonai = np.mean(nonai_errors)
mean_ai = np.mean(ai_errors)

#toa values
print("Average True TOA:", np.mean(true_toas))
print("Average Classical TOA:", np.mean(classical_toas))
print("Average AI TOA:", np.mean(ai_toas))
#error values
print("Mean Non-AI Error:", mean_nonai)
print("Mean AI Error:", mean_ai)
print("Error Reduction (%):", round(100*(mean_nonai-mean_ai) / mean_nonai, 2))

print("Samples used for training:", X_train.shape[0])
print("Feature dimension:", X_train.shape[1])


