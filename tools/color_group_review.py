import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import numpy as np

threshold = 50

def color_distance(c1, c2):
    return np.sqrt(sum((np.array(c1) - np.array(c2)) ** 2))

def load_rectangles(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def group_colors(dominant_colors):
    color_groups = []
    for color in dominant_colors:
        found = False
        for group in color_groups:
            if color_distance(color, group[0]) < threshold:
                group.append(color)
                found = True
                break
        if not found:
            color_groups.append([color])
    return color_groups

def draw_color_groups(ax, rectangles):
    for rect in rectangles:
        x, y, w, h = rect["position"]
        dominant_colors = rect["dominant_colors"]
        
        color_groups = group_colors(dominant_colors)

        for i, group in enumerate(color_groups):
            rect_height = 20
            ax.add_patch(patches.Rectangle((x, y + i * rect_height), w, rect_height, 
                                            facecolor=[c / 255 for c in group[0]], edgecolor='black'))
            
            for j, color in enumerate(group):
                ax.add_patch(patches.Rectangle((x + j * 50, y + i * rect_height), 50, rect_height, 
                                                facecolor=[c / 255 for c in color], edgecolor='black'))

def main():
    rectangles = load_rectangles('renk_bilgileri.json')

    fig, ax = plt.subplots()
    ax.set_title('Benzer Renk Grupları')
    
    draw_color_groups(ax, rectangles)

    ax.set_xlim(0, 800)  
    ax.set_ylim(0, 1000) 
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    main()
