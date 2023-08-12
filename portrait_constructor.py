import math
import json
import numpy as np
from webcolors import name_to_rgb
import matplotlib.pyplot as plt
from text_processor import TextProcessor
from color_extractor import ColorExtractor


def convert_names_to_numbers(color_names):
    return [list(name_to_rgb(color)) for color in color_names]

def optimize_grid_shape(rgb_colors):
    color_grid = np.vstack(rgb_colors)
    num_colors = color_grid.shape[0]
    sq_root = int(math.sqrt(num_colors))
    height = sq_root
    width = 0
    while height > 1:
        if num_colors % height == 0:
            width = num_colors // height
            break
        height -= 1
    if width == 0:
        height = sq_root
        width = int(math.ceil(num_colors / sq_root))
        filler = [[255, 255, 255]] * (height * width - num_colors)
        if filler:
            color_grid = np.vstack((rgb_colors, filler))
    return color_grid.reshape(height, width, 3)

def construct_portrait(color_names):
    fig, ax = plt.subplots()
    ax.axis('off')
    rgb_colors = convert_names_to_numbers(color_names)
    color_grid = optimize_grid_shape(rgb_colors)
    ax.imshow(color_grid)
    return fig

if __name__ == "__main__":
    processor = TextProcessor()
    text = processor.process('text.txt')

    with open('colors.json') as file:
        colors = json.load(file)
    extractor = ColorExtractor(colors)
    extracted_colors = extractor.extract(text)
    portrait = construct_portrait(extracted_colors)
    portrait.savefig('portrait.png')