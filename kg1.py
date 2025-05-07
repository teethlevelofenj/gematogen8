import matplotlib.pyplot as plt
import numpy as np

# Запит даних у користувача
x0 = float(input("Введіть координату x початкової точки A: "))
y0 = float(input("Введіть координату y початкової точки A: "))
n = int(input("Скільки дотичних побудувати (n): "))

r = 3.0  # Радіус кола

# Ініціалізація списків для зберігання точок
points_A = [(x0, y0)]
points_L = []
points_P = []

# Поточна точка A
Ax, Ay = x0, y0

for _ in range(n):
    d = np.sqrt(Ax**2 + Ay**2)
    if d <= r:
        print("Одна з точок потрапила всередину кола. Побудову зупинено.")
        break  

    angle_OA = np.arctan2(Ay, Ax) 
    angle_offset = np.arccos(r / d)  # знаходження кута AOL
    angle_tangent = angle_OA + angle_offset # знаходження кута LO(Ox)

    # Точка дотику
    lx = r * np.cos(angle_tangent)
    ly = r * np.sin(angle_tangent)

    # Точка P
    px = 2 * lx - Ax
    py = 2 * ly - Ay

    # Зберігаємо точки
    points_L.append((lx, ly))
    points_P.append((px, py))

    # Наступна точка A — це нова P
    Ax, Ay = px, py
    points_A.append((Ax, Ay))

# Побудова
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), r, color='b', fill=False)
ax.add_artist(circle)

for i in range(len(points_L)):
    Ax, Ay = points_A[i]
    Lx, Ly = points_L[i]
    Px, Py = points_P[i]
    ax.plot([Ax, Lx], [Ay, Ly], 'r-')   # AL
    ax.plot([Lx, Px], [Ly, Py], 'r--')  # LP

# Візуалізація
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-r-10, r+10)
ax.set_ylim(-r-10, r+10)
ax.set_title(f"{len(points_L)} послідовних дотичних")
plt.show()
