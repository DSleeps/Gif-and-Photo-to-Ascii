# for i in range(1000):
#     print(str(i) + ': ' + '.'*i)
from os import system, name
import PIL
from PIL import Image, ImageFilter
import math as m
import pyperclip as p
import sys
import time
from colr import Colr as C

#asc_characters = ['▁', '▂', '▃', '▄', '▅', '▆', '▇']
#asc_characters = [' ', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█']
#asc_characters = [' ', '.', ':', 'l', 'U', 'B', '#', '$']
asc_characters = [' '] * 1 + ['.'] +  [':'] + ['l'] + ['U'] + ['#'] + ['$']

thresholds = []
for i in range(len(asc_characters)):
    thresholds.append([i * m.ceil(255/len(asc_characters)), (i+1) * m.ceil(255/len(asc_characters))])
print(thresholds)

#The width and height of the command prompt window
width = 0
height = 0

#The ratio between the width and height (height/width)
height_diff = 0

#The type you have to input
type = 'Command'

#Actually get the image
im_name = 'LilGif.gif'
#im_name = 'Caleb.jpg'

if (type == 'Command'):
    width = 230
    height = 63
    height_diff = 2
else:
    width = 39
    height = 1
    height_diff = 1.5

reverse = False

def display_image():
    im = Image.open("Photos/" + im_name) # open colour image
    im = im.convert('L') # convert image to black and white

    #Max darkness value
    max_dark = 255

    width_ratio = m.ceil(im.width/width)
    height_ratio = m.ceil(width_ratio * height_diff)

    #Put a blank line
    im_str = '```'
    for y in range(int(im.height/(height_ratio))):
        for x in range(int(im.width/width_ratio)):
            p_value = im.getpixel((x*width_ratio,y*height_ratio))
            for i in range(len(thresholds)):
                t = thresholds[i]
                if (t[0] <= p_value <= t[1]):
                    im_str += asc_characters[i]
                    break
        im_str += '\n'
    im_str += '```'

    if (reverse == True):
        print(im_str[::-1])
        p.copy(im_str[::-1])
        return im_str[::-1]
    else:
        print(im_str)
        p.copy(im_str)
        return im_str

def convert_image(im):
    im = im.convert('L') # convert image to black and white
    #im = im.filter(ImageFilter.FIND_EDGES)
    #im.show()
    #Max darkness value
    max_dark = 255

    width_ratio = m.ceil(im.width/width)
    height_ratio = m.ceil(width_ratio * height_diff)

    #Put a blank line
    im_str = '```'
    for y in range(int(im.height/(height_ratio))):
        for x in range(int(im.width/width_ratio)):
            p_value = im.getpixel((x*width_ratio,y*height_ratio))
            for i in range(len(thresholds)):
                t = thresholds[i]
                if (t[0] <= p_value <= t[1]):
                    im_str += asc_characters[i]
                    break
        im_str += '\n'
    im_str += '```'

    if (reverse == True):
        return im_str[::-1]
    else:
        return im_str

def convert_edge_image(im):
    im = im.convert('L') # convert image to black and white
    im = im.filter(ImageFilter.FIND_EDGES)
    #im.show()
    #Max darkness value
    max_dark = 255

    width_ratio = m.ceil(im.width/width)
    height_ratio = m.ceil(width_ratio * height_diff)

    #Put a blank line
    im_str = '```'
    for y in range(int(im.height/(height_ratio))-1):
        for x in range(int(im.width/width_ratio)-1):
            p_values = []
            for new_x in range(int(x*width_ratio), int((x+1/2)*width_ratio)):
                for new_y in range(int(y*height_ratio), int((y+1/2)*height_ratio)):
                    p_values.append(im.getpixel((new_x,new_y)))

            p_value = max(p_values)
            for i in range(len(thresholds)):
                t = thresholds[i]
                if (t[0] <= p_value <= t[1]):
                    im_str += asc_characters[i]
                    break
        im_str += '\n'
    im_str += '```'

    if (reverse == True):
        return im_str[::-1]
    else:
        return im_str

def clear():
    _ = system('clear')

def display_gif():
    i = 0

    #Start by processing every image
    gif = Image.open('Photos/' + im_name)
    frames = []
    durations = []
    for i in range(gif.n_frames):
        print(i)
        gif.seek(i)
        frames.append(convert_image(gif))
        durations.append(1/int(1000 / gif.info['duration']))
    i = 0
    while True:
        clear()
        print(frames[i % gif.n_frames])
        time.sleep(durations[i % gif.n_frames])
        i += 1

display_gif()
#display_image()
