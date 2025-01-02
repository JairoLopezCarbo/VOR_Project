import numpy as np
import matplotlib.pyplot as plt

# Parámetros generales
fs = 5000        # Frecuencia de muestreo (Hz)
T = 0.5          # Duración de la señal para visualización (segundos)
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Vector de tiempo

# Parámetros de la señal x(t, ϑ)
f_ref = 50.0     # Frecuencia de la referencia (Hz)
β = 12.0          # Índice de modulación
f_B = 3.0        # Frecuencia de la señal moduladora (Hz)
ϑ = np.pi / 2    # Fase (rad) 

# Definición de x(t, ϑ)
x = np.cos(2 * np.pi * f_ref * t + β * np.sin(2 * np.pi * f_B * t)) + np.cos(2 * np.pi * f_B * t + ϑ)

# Tono individual con desfase respecto a f_ref de 90 grados
tono = np.cos(2 * np.pi * f_B * t + ϑ)

# Encontrar el desfase en tiempo
t_desfase = ϑ / (2 * np.pi * f_B)  # Tiempo correspondiente al desfase

# Parámetros para s(t, ϑ)
A = 10.0          # Amplitud de la portadora
m = 1          # Índice de modulación
f_C = 60.0       # Frecuencia de la portadora (Hz)

# Definición de s(t, ϑ)
s = A * (1 + m * x) * np.cos(2 * np.pi * f_C * t)

# Encontrar los máximos
t_max_x = t[np.argmax(x)]  # Tiempo del máximo de x(t, ϑ)
t_max_tono = t_max_x+t_desfase  # Tiempo del máximo del tono

# Graficar x(t, ϑ) y s(t, ϑ)
plt.figure(figsize=(14, 8))

# Graficar x(t, ϑ)
plt.subplot(2, 1, 1)
plt.plot(t, x, linewidth = 3)
plt.plot(t, tono, 'r--', label=f'Variable Signal (ϑ = +90°)', linewidth = 3)  # Línea discontinua para el tono
plt.axvline(x=t_max_x, linestyle='-.', color = 'navy', linewidth = 2)  # Línea vertical para el máximo de x(t, ϑ)
plt.axvline(x=t_max_tono, linestyle='-.', color = 'firebrick', linewidth = 2)  # Línea vertical para el máximo del tono
plt.ylabel('Amplitude')
plt.title('x(t, ϑ)')
plt.grid(True)
plt.legend()

# Graficar s(t, ϑ)
plt.subplot(2, 1, 2)
plt.plot(t, s, color='orange' , label=f'Py = 100W', linewidth = 3)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('y(t, ϑ)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
