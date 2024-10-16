import colorsys
import json


with open('data\hex_color_codes.json', 'r') as file:
    data = json.load(file)

red= data["red"]
blue= data["blue"]
yellow= data["yellow"]
black= data["black"]

def hex_to_hsv(hex_color:list)->list:
    hsv_list=[]

    for i in hex_color:

        hex_color = i.lstrip('#')  
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0
        
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        
        h = (h * 360).__round__()
        s = (s * 100).__round__()
        v = (v * 100).__round__()
        hsv= (h, s, v)
        hsv_list.append(hsv)

    return hsv_list

colors = {
    "red": hex_to_hsv(red),
    "blue": hex_to_hsv(blue),
    "yellow": hex_to_hsv(yellow),
    "black": hex_to_hsv(black),
}

print("HSV Rengi:", colors)
