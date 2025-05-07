import matplotlib.pyplot as plt
import matplotlib.patches as patches

def inside(p, edge, xmin, xmax, ymin, ymax):
    x, y = p
    if edge == 'left':
        return x >= xmin
    elif edge == 'right':
        return x <= xmax
    elif edge == 'bottom':
        return y >= ymin
    elif edge == 'top':
        return y <= ymax

def intersect(p1, p2, edge, xmin, xmax, ymin, ymax): #накладання точок
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 == y2:
        return p1

    if edge == 'left':
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    elif edge == 'right':
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    elif edge == 'bottom':
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    elif edge == 'top':
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
    return (x, y)

def clip_polygon(polygon, edge, xmin, xmax, ymin, ymax):
    clipped = []
    n = len(polygon)
    for i in range(n):
        curr = polygon[i]
        prev = polygon[i - 1]
        curr_in = inside(curr, edge, xmin, xmax, ymin, ymax)
        prev_in = inside(prev, edge, xmin, xmax, ymin, ymax)

        if curr_in:
            if not prev_in:
                clipped.append(intersect(prev, curr, edge, xmin, xmax, ymin, ymax))
            clipped.append(curr)
        elif prev_in:
            clipped.append(intersect(prev, curr, edge, xmin, xmax, ymin, ymax))
    return clipped

def sutherland_hodgman(polygon, xmin, xmax, ymin, ymax):
    for edge in ['left', 'right', 'bottom', 'top']:
        polygon = clip_polygon(polygon, edge, xmin, xmax, ymin, ymax)
    return polygon

def draw_polygon_and_clipping(original, clipped, clip_window):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_title("Sutherland-Hodgman Clipping")

    xmin, xmax, ymin, ymax = clip_window
    rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                             linewidth=2, edgecolor='red', facecolor='none', linestyle='--', label="Clipping Window")
    ax.add_patch(rect)

    # Original polygon (gray solid)
    orig_poly = original + [original[0]]
    ox, oy = zip(*orig_poly)
    ax.plot(ox, oy, 'gray', label='Original Polygon')

    # Clipped polygon (green)
    if clipped:
        cl_poly = clipped + [clipped[0]]
        cx, cy = zip(*cl_poly)
        ax.plot(cx, cy, 'green', linewidth=2, label='Clipped Polygon')

    ax.legend()
    ax.grid(True)
    plt.show()

# === Вихідні дані ===
polygon = [
    (2, 9),   # A
    (6, 9),   # B
    (6, 6),   # C
    (2, 6),   # D
    (3, 7),   # K
]  # довільний п’ятикутник


clip_window = (3, 5, 3, 7)  # xmin, xmax, ymin, ymax

clipped = sutherland_hodgman(polygon, *clip_window)
draw_polygon_and_clipping(polygon, clipped, clip_window)
