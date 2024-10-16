
import json
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

with open('data\hsv_color_codes.json', 'r') as file:
    data = json.load(file)

red= data["red"]
blue= data["blue"]
yellow= data["yellow"] 
black= data["black"]

def normalize_hsv(hsv_list):
    return [(h / 360, s / 100, v / 100) for h, s, v in hsv_list]

normalize_colors = normalize_hsv(black)


rgb_colors = [mcolors.hsv_to_rgb(hsv) for hsv in normalize_colors]

fig, ax = plt.subplots(figsize=(6, 2))

for i, rgb in enumerate(rgb_colors):
    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=rgb))

ax.set_xlim(0, len(rgb_colors))
ax.set_ylim(0, 1)
ax.axis('off')
plt.show()