import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Data from the markdown table
position = np.array([
    1.952, 1.928, 1.902, 1.872, 1.854, 1.834, 1.809,
    1.790, 1.772, 1.754, 1.734, 1.714, 1.696, 1.678
])

time = np.array([
    1.60, 4.00, 6.40, 8.75, 11.20, 13.65, 15.95,
    18.50, 20.80, 23.20, 25.55, 27.90, 30.35, 32.70
])


def harmonic_model(t, A, omega, phase, offset):
    return A * np.cos(omega * t + phase) + offset

initial_guess = [
    (position.max() - position.min()) / 2,  # amplitude
    2 * np.pi / (time[-1] / len(time)),      # angular frequency
    0,                                       # phase
    position.mean()                          # offset
]

popt, pcov = curve_fit(harmonic_model, time, position, p0=initial_guess)

amplitude, angular_frequency, phase_shift, offset = popt

# Plot the data and the fit
plt.scatter(time, position, label='Data')
t_fit = np.linspace(time.min(), time.max(), 100)
position_fit = harmonic_model(t_fit, *popt)
plt.plot(t_fit, position_fit, label='Harmonic Fit', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.show()

# Return the optimized parameters
amplitude, angular_frequency, phase_shift, offset
