import cv2
import numpy as np
import os
from os.path import isfile, join
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


pathIn = 'C:/Batchelor/Data/IRL/Timelapses/buttontest2/'
pathOut = 'C:/Batchelor/Data/IRL/Timelapses/fail_small_cube_lapse.avi'
fps = 30
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=natural_keys)
files.sort()
print(*files, sep="\n")
# frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

for i in range(len(files)):
    filename = pathIn + files[i]
    # reading each files
    img = cv2.imread(filename)
    resized = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
    height, width, layers = resized.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(resized)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()

print('Timelapse built..')
