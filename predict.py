#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from cv2 import imread
from keras.models import load_model
from PIL import Image
from std_msgs.msg import String
import numpy as np
import vlc
import rospy

"""
Predict
This script loads a pre-trained CNN model and classifies whale blowholes based
on a single image
Isaac Vandor
"""
from argparse import ArgumentParser
rospy.init_node("Commands")
pub = rospy.Publisher('/command_words', String, queue_size=1)

def parse_command_line(raw_args=None):
    """
    Parse command-line arguments.

    Use the built-in Python argparse facility to parse the command-line
    arguments as well as construct and provide meaningful help and feedback
    should bad data be entered or help be requested. By doing this we'll
    automatically get a traditional usage message as well as a help
    response.

    Args:
        raw_args:   The arguments as obtained from the command line.
                    Normally this is left at None unless one wants to
                    load in values for unit testing.

    Returns:
        The input filename.
    """

    assert raw_args is None or isinstance(raw_args, list)
    # Use the Python argparser to parse command line input and provide
    # usage information and feedback should bad input be given or help
    # requested.
    default_filename = 'speech_dataset/testing_dir/spectrogram1.png'

    parser = ArgumentParser(
        description="Grab still images from a video."
    )
    parser.add_argument(
        '--input', '-i', default=default_filename,
        nargs='?', const=default_filename, metavar="input_filename",
        help='Optional filename for input video file. '
        'Default: {0}'.format(default_filename)
    )
    args = parser.parse_args(raw_args)
    return args.input

def load(trained_model):
    """ Loads a pre-trained model. """

    model = load_model(trained_model)
    return model

def predict(trained_model, test_image):
    """ Loads an image, resizes it to the size model was trained on,
    corrects the color channels to be similar to the model's channels
    and predicts the blowhole """

    #input_filename = 'speech_dataset/testing_dir/spectrogram.png'
    img = Image.open(input_filename)
    img = img.resize((75,75), resample=0)     # resize to 75x75 px
    img = img.save('speech_dataset/OutputData/temp.png')
    img = imread('speech_dataset/OutputData/temp.png')
    img = img.astype(np.float32)/255.0      # convert to float32
    #img = np.array(img).astype(np.float32)

    # turn image into a 1-element batch :
    #img = np.expand_dims(img, axis=0)

    img = img[:,:,::-1]         # convert from RGB to BGR
    # prediction probability vector :
    #result = model.predict(img)
    result = trained_model.predict(np.expand_dims(img, axis=0))[0]
    return result

def find_voice(list, dict):
    """ Finds the biggest element in the list and looks for the corresponding
    key in the dictionary

    result: list whose biggest element we're trying to find
    list: dictionary whose key corresponds to the largest element """
    idx = list.argmax(axis=0)    # find the index of the biggest argument

    # most probable item :
    #best_index = np.argmax(result, axis=1)[0]
    # look for the key corresponding to the biggest argument
    decoded = [key for key, value in dict.items() if value == idx]
    return decoded[0]
    #return best_index

if __name__ == "__main__":

    input_filename = parse_command_line()
    model = load(trained_model='models/model.h5')
    result = predict(trained_model=model, test_image='speech_dataset/spectrograms/OutputData/scaledoutput.png')

    voice_types = {"background_noise": 0, "backward": 1, "bed":2, "bird": 3, "cat": 4, "dog": 5, "down": 6, "eight": 7, "five": 8, "follow": 9, "forward": 10, "four": 11, "go": 12, "happy": 13, "left": 14, "marvin": 15, "off": 16, "on": 17, "one": 18, "right": 19, "sheila": 20, "stop":21,"three": 22, "tree": 23, "two": 24, "up": 25, "wow": 26, "yes": 27}

    alphabet = find_voice(list=result, dict=voice_types)
    pub.publish(alphabet)
    print("The word is: ", alphabet)
