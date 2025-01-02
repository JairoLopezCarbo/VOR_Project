from scipy.ndimage import uniform_filter1d
import numpy as np
import matplotlib.pyplot as plt

# Constantes
c = 0.343  # velocidad del sonido en km/ms
f = 30  # frecuencia en Hz
rfx_angle = 5  # ángulo inicial en grados

# Convertir ángulo a radianes para los cálculos
rfx_angle_rad = np.radians(rfx_angle)

# Definición de la función basada en la ecuación proporcionada (con valor absoluto)
def error_phi_abs_1(D, rfx_angle_rad):
    numerator = np.sin(rfx_angle_rad + 2 * np.pi * f * D * (1/np.cos(rfx_angle_rad) - 1) / c)
    denominator = 1 / np.cos(rfx_angle_rad) + np.cos(rfx_angle_rad + 2 * np.pi * f * D * (1/np.cos(rfx_angle_rad) - 1) / c)
    return np.abs(np.arctan(numerator / denominator))/np.pi*180
def error_phi_abs_2(D, rfx_angle_rad):
    numerator = np.sin(rfx_angle_rad)
    denominator = 1 / np.cos(rfx_angle_rad) + np.cos(rfx_angle_rad)
    return np.abs(np.arctan(numerator / denominator))/np.pi*180

# Gráfica 1: Mapa de calor - Variando D y ángulo

D_heatmap = np.linspace(50, 350, 100)  # D de 50 km a 350 km
angles_heatmap = np.linspace(5, 45, 100)  # Ángulos de 5 a 45 grados
D_grid, angles_grid = np.meshgrid(D_heatmap, angles_heatmap)
phi_errors_heatmap_abs = error_phi_abs_1(D_grid, np.radians(angles_grid))

# Suavizar el mapa de calor
phi_errors_heatmap_smooth = uniform_filter1d(phi_errors_heatmap_abs, size=5, axis=0)
phi_errors_heatmap_smooth = uniform_filter1d(phi_errors_heatmap_smooth, size=5, axis=1)

plt.figure(figsize=(10, 8))
plt.contourf(D_heatmap, angles_heatmap, phi_errors_heatmap_smooth, cmap="viridis")
plt.colorbar(label="Absolute error (ϕ er) [degrees]")
plt.title("Heat Map of Absolute Error")
plt.xlabel("Distance (D) [km]")
plt.ylabel("Reflection Angle (ϕ rfx)  [degrees]")
plt.show()

# Gráfica 2: Variando el ángulo, D fijo
D_fixed = 200  # Distancia fija en 200 km
angles = np.linspace(5, 90, 500)  # Ángulos variando de 5 a 45 grados
phi_errors_angle_abs = error_phi_abs_2(D_fixed, np.radians(angles))

# Suavizar los resultados de la gráfica 2
phi_errors_angle_smooth = uniform_filter1d(phi_errors_angle_abs, size=50)

plt.figure(figsize=(10, 6))
plt.plot(angles, phi_errors_angle_abs, linewidth=5)
plt.title("Reflection Angle vs Absolute error")
plt.xlabel("Reflection Angle (ϕ rfx)  [degrees]")
plt.ylabel("Absolute error (ϕ er) [degrees]")
plt.grid(True)
plt.show()

