import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34
c = 3e8
me = 9.11e-31
compton_const = h / (me * c)

# User input
initial_wavelength = float(input("Enter initial wavelength (nm): ")) * 1e-9
theta_deg = float(input("Enter scattering angle (degrees): "))
theta_rad = np.radians(theta_deg)

# Compton shift
delta_lambda = compton_const * (1 - np.cos(theta_rad))
scattered_wavelength = initial_wavelength + delta_lambda

# Energies
E_initial = h * c / initial_wavelength
E_scattered = h * c / scattered_wavelength
KE = E_initial - E_scattered

# Output
print(f"Compton Shift: {delta_lambda:.3e} m")
print(f"Scattered Wavelength: {scattered_wavelength*1e9:.3f} nm")
print(f"Kinetic Energy: {KE:.3e} J")

# Plot Compton shift vs angle only
angles = np.linspace(0, 180, 360)
shifts = compton_const * (1 - np.cos(np.radians(angles)))

plt.figure(figsize=(6, 5))
plt.plot(angles, shifts * 1e12, color='blue')
plt.title("Compton Shift vs Scattering Angle")
plt.xlabel("Scattering Angle (°)")
plt.ylabel("Δλ (pm)")
plt.grid(True)
plt.tight_layout()
plt.show()
