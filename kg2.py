import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth, max_depth, f):
    if depth > max_depth:
        return
    angles = [angle - 120, angle, angle + 120]
    for a in angles:
        rad = np.radians(a)
        x_new = x + length * np.cos(rad) 
        y_new = y + length * np.sin(rad)
        plt.plot([x, x_new], [y, y_new], 'k-', linewidth=0.5) 
        next_length = length * f  # Зменшення довжини відповідно до коефіцієнта f
        draw_branch(x_new, y_new, a, next_length, depth + 1, max_depth, f)

# Параметри
max_depth = int(input("Введіть глибину дерева: "))
initial_length= 200.0
reduction_factor = 0.456   # f – коефіцієнт зменшення довжини

# Побудова дерева
plt.figure(figsize=(16, 16))
draw_branch(0, 0, 90, initial_length, 1, max_depth, reduction_factor)
plt.axis('equal')
plt.axis('off')
plt.title(f"Трійкове дерево (глибина {max_depth}) з f = {reduction_factor}")
plt.show()
