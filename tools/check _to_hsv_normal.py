
import json
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


with open('data\hsv_color_codes.json', 'r') as file:
    data = json.load(file)

red= data["red"]
blue= data["blue"]
yellow= data["yellow"]
black= data["black"]

def hsv_normalizer(color_list):

    normal_list=[]
    for i in range(0, len(color_list), 4):

        group = color_list[i:i+4]

        if len(group) == 4:  
            h_avg = sum([item[0] for item in group]) // 4
            s_avg = sum([item[1] for item in group]) // 4
            v_avg = sum([item[2] for item in group]) // 4
            normal_list.append((h_avg, s_avg, v_avg))
            
    return normal_list

colors = {
    "red": hsv_normalizer(red),
    "blue": hsv_normalizer(blue),
    "yellow": hsv_normalizer(yellow),
    "black": hsv_normalizer(black),
}

def normalize_hsv(hsv_list):
    return [(h / 360, s / 100, v / 100) for h, s, v in hsv_list]

for i in [ colors["yellow"]]:

    normalize_colors = normalize_hsv(i)

    rgb_colors = [mcolors.hsv_to_rgb(hsv) for hsv in normalize_colors]
    fig, ax = plt.subplots(figsize=(6, 2))

    for i, rgb in enumerate(rgb_colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=rgb))

    ax.set_xlim(0, len(rgb_colors))
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()