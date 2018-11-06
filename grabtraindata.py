#!/usr/python/env
import os
import matplotlib.pyplot as plt
import PIL
import random

# dimensions of images
img_width, img_height = 610, 450


train_data_dir = 'speech_dataset/train_dir'
validation_data_dir = 'speech_dataset/validation_dir'

wav_count = 0

def length_directory(dir_name):
    numfiles = len([f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))])
    return numfiles

print(length_directory("speech_dataset/train_dir"))

for root, sub, files in os.walk('speech_dataset/train_dir'):
    print('reading files now')
    count = 0
    files = sorted(files)
    for f in files:
        while count <= 100:
            im = PIL.Image.open(os.path.join(root, f))
            img_width, img_height = im.size
            left = random.randint(0,10)
            top = random.randint(0,50)
            tile = im.crop((left,top,left,top))
            tile.show()
            resized_tile = tile.resize((75,75))
            name = "speech_dataset/validation_dir_holdback/spectrogram.png"
            im.save(name)
            #plt.show()
            print('file printing now')    
            count+=1
            print(count)