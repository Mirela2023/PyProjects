import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 6, 1000)
y = x**2 - 4*x + 3

plt.figure(figsize=(10,7))
plt.plot(x, y, label='f(x) = x² - 4x + 3')

plt.axhline(0, color='darkgreen', linewidth=1.1)
plt.axvline(0, color='darkgreen', linewidth=1.1)
plt.ylim(-5, 10)

# Stilizare titlu
# am folosit r'$f(x)$' care scrie f(x) ca expresie matematică
plt.title(
    r'Graficul funcției $f(x) = x^2 - 4x + 3$',
    fontsize=14,
    color='navy',
    pad=15,
    bbox=dict(
        facecolor='aliceblue',  # culoare fundal
        edgecolor='gray',       # culoare margine
        boxstyle='round,pad=0.5',  # colțuri rotunjite, spațiere
        alpha=0.9   # transparență (1 = opac)
    )
)

plt.xlabel('X')
plt.ylabel('y=f(x)')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.3)

# Stilizare legenda
plt.legend(
    loc='center',
    facecolor='whitesmoke',
    edgecolor='gray',
    frameon=True,
    fontsize=10,
    shadow=True,
    framealpha=0.9,
    fancybox=True
)
plt.show()
