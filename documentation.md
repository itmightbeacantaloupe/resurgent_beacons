AI-Based Pulsar Time-of-Arrival Estimation Prototype

	Project Description
This project is a prototype that demonstrates an AI-based approach for estimating pulsar’s time of arrival (TOA) under noisy and biased observation conditions. The system simulates pulsar signals, extracts features and trains a supervised regression model to predict TOA.
A classical method of TOA estimation is implemented for performance comparison.
The objective is to demonstrate how an AI-based model can reduce estimation error compared to classical method.

	Architecture
The system follows modular architecture:
	Signal Simulation Module
Generates synthetic pulsar signals, applies clock bias and Gaussian noise, produces true TOA values
	Preprocessing Module
Extracts peak window features from the observed signal and reduces dimensionality
	AI Model Module
Trains a supervised regression model and predicts TOA from extracted features
	Classical Baseline Module
Computes TOA using signal-processing methods
	Evaluation Module
Performs Monte Carlo simulations, calculates Mean Absolute Error (MAE) and computes percentage error reduction
To ensure clarity and extensibility, each module is implemented as a separate Python component.

	Technology Stack
The prototype is implemented using:
	Python 3.x
	NumPy, Scikit-Learn libraries
	Custom modular Python code

	Algorithms and AI Model
Simulation: The pulsar signal is generated using configurable parameters:
	Pulse period
	Pulse width
	Clock bias
	Noise standard deviation
Gaussian noise is added to simulate realistic observational conditions.
Random phase shifts simulate unknown pulse arrival times.

Feature Extraction: The system extracts only a peak window around the pulse’s maximum instead of using the full signal. This reduces input dimensionality, improves robustness against noise and allows AI to focus on the most informative region 

AI Model: The AI component is a supervised regression model.
	Input: Peak window signal samples
	Output: Predicted Time-of-Arrival (TOA)
	Training Data: Monte Carlo–generated simulations
The model learns the mapping between signal shape and true TOA.

Classical Baseline: Classical signal processing method estimates TOA directly from the observed signal. This method is used for comparison with the AI-based approach.

Evaluation: Performance is evaluated using Mean Absolute Error (MAE):

MAE=|TOA_estimated - TOA_true|

Report: the system reports:
	Mean Non-AI Error
	Mean AI Error
	Percentage Error Reduction
Monte Carlo simulations ensure statistically stable results.

	Configurable Parameters
The system allows change of:
	MC_runs - number of Monte Carlo simulations
	Seed - random seed for reproducibility. Users may change it to evaluate model robustness under different conditions.
	Pulsar characteristics:
	pulse_period
	pulse_width
	noise_std
	clock_bias
	Sampling resolution (dt)
	Observation duration

	Instructions for Launching
Requirements:
	Python 3.x
	numpy, sckit-learn libraries installed
	Running the Prototype
Configure parameters in config.py if needed.
From the project root directory, run main.py
The console will display:
	Mean Non-AI Error
	Mean AI Error
	Percentage Error Reduction
	Number of training samples
	Feature dimension

	Limitations:
Gaussian noise assumption
Single-pulse window analysis
Simulation-based validation only


