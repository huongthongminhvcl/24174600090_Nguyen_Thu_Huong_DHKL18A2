print("**    **   **  **    ****    ****   ******")
print("**    **   **  **   **  **  **  **  **    ")
print("********   **  **   **  **  **  **  ** ****")
print("**    **   **  **   **  **  **  **  **  **")
print("**    **    ****      **    **  **  ******")


import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu cho hình trái tim
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Vẽ hình trái tim
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='red')
plt.title('Hình trái tim')
plt.axis('equal')
plt.grid()
plt.show()