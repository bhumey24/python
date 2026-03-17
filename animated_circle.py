import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

speed = float(input("Enter speed of the circle (e.g., 0.1): "))


x, y = 5, 5
dx, dy = 0, 0

fig, ax = plt.subplots()
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_title("Use Arrow Keys to Move the Circle")


def on_key(event):
    global dx, dy
    if event.key == 'up':
        dx, dy = 0, speed
    elif event.key == 'down':
        dx, dy = 0, -speed
    elif event.key == 'left':
        dx, dy = -speed, 0
    elif event.key == 'right':
        dx, dy = speed, 0

fig.canvas.mpl_connect('key_press_event', on_key)


def update(frame):
    global x, y
    x += dx
    y += dy

   
    x = max(0.5, min(x, 9.5))
    y = max(0.5, min(y, 9.5))

    circle.center = (x, y)
    return circle,

ani = FuncAnimation(fig, update, interval=30)

plt.show()