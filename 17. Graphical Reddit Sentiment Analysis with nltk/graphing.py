import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


# GPT 3 (for static reddit file):

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

max_points = 50  # Number of points to display (window size)
current_index = 0  # To track which part of the data to display

# Read all the lines from the file once since it's fixed
with open('reddit-out.txt', 'r') as f:
    lines = f.readlines()

total_lines = len(lines)  # Total number of lines in the file


def animate(i):
    global current_index

    # Ensure we don't go out of bounds
    if current_index + max_points <= total_lines:
        current_data = lines[current_index:current_index + max_points]
    else:
        current_data = lines[-max_points:]  # If we exceed, show the last 50

    xar, yar = [], []
    y = 0

    # Process the current window of data
    for index, l in enumerate(current_data):
        if 'pos' in l:
            y += 1
        elif 'neg' in l:
            y -= 1
        xar.append(index + current_index)
        yar.append(y)

    # Clear the previous plot and update with new data
    ax1.clear()
    ax1.plot(xar, yar)

    # Set limits for the x-axis to create a shifting window
    ax1.set_xlim(current_index, current_index + max_points - 1)
    ax1.set_ylim(min(yar) - 1, max(yar) + 1)

    # Increment the current index to shift the window
    if current_index + max_points < total_lines:
        current_index += 1  # Move the window forward


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

