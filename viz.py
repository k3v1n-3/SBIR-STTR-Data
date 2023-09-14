import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FixedFormatter, FixedLocator
import numpy as np
from scipy import interpolate
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from moviepy.editor import *
from moviepy.video.io.bindings import mplfig_to_npimage



# Read the filtered data from CSV
filtered_data = pd.read_csv('awardData.csv')

# Exclude the year 2023
filtered_data = filtered_data[filtered_data['Award Year'] < 2023]

# Group Data by Award year and sum the Award amount
grouped_data = filtered_data.groupby('Award Year')['Award Amount'].sum().reset_index()

# Create interpolation function using B-spline
x = grouped_data['Award Year']
y = grouped_data['Award Amount']
bspline = interpolate.make_interp_spline(x, y)
x_new = np.linspace(x.min(), x.max(), 500)
y_new = bspline(x_new)

# Initialize the plot
fig, ax = plt.subplots(figsize=(12,6))


# Add background image
img = plt.imread("airForce.png")

# Calculate center and range for x and y
x_center = (x.max() + x.min()) / 2
y_center = y.max() * 0.5

# Define the extent to which the image should be displayed
# [left, right, bottom, top]
img_extent = [x_center - 5, x_center + 5, y_center - 0.25 * y.max(), y_center + 0.25 * y.max()]

# Add image to plot
ax.imshow(img, extent=img_extent, aspect='auto', alpha=0.5)

# Set the background color of the plot to black
ax.set_facecolor('black')
fig.set_facecolor('black')  # For the part of the figure outside the axes

# Set the color of the ticks, tick labels, and axis label to white
ax.tick_params(colors='white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Set the title color to white
ax.title.set_color('white')

# Set the color of the spines (the box) to white
for spine in ax.spines.values():
    spine.set_edgecolor('white')

# Set axis labels and title 
ax.set_xlabel('Award Year')
ax.set_ylabel('Total Awarded $$$ (in Millions)')
ax.set_title('Total SBIR/STTR Awarded by Year')

# Initialize an empty line
line, = ax.plot([], [], lw=2)

# Set axis limits
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0, y.max() * 1.1)

# Manually set x-ticks to show more years
ax.set_xticks(range(int(x.min()), int(x.max()) + 1, 3))  # Changed the step to 3 years for readability

# Get current y-ticks and set custom labels
yticks = ax.get_yticks()
ax.yaxis.set_major_locator(FixedLocator(yticks))
ax.yaxis.set_major_formatter(FixedFormatter(['{:.0f}M'.format(x/1e6) for x in yticks]))

# Add a text annotation for the data source
ax.text(0.8, 0.02, 'Source: sbir.gov', transform=ax.transAxes, fontsize=10, va='bottom', ha='left', color = 'white')

# Initialize function
def init():
    line.set_data([], [])
    return line,

# Animation function
def update(frame):
    line.set_data(x_new[:frame], y_new[:frame])
    return line,

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=len(x_new), init_func=init, blit=True, interval=20)

# Create a function to return a frame for each 't'
def make_frame(t):
    frame = int(np.clip(np.round(t * 1000 / 20), 0, len(x_new) - 1))
    line, = ax.plot(x_new[:frame], y_new[:frame], lw=2, color = 'blue')  # Create a new line or update the existing line
    return mplfig_to_npimage(fig)

# Calculate the duration of the animation in seconds
duration = len(x_new) * 20 / 1000

# Create a MoviePy Clip object
video = VideoClip(make_frame, duration=duration)

# Load your audio clip
audio = AudioFileClip("Air_Force_Song.mp3")

# Set audio
audio = AudioFileClip("Air_Force_Song.mp3").subclip(26,26+duration)
video = video.set_audio(audio)

# Write the result to a file
video.write_videofile('awardAni.mp4', fps=24)
