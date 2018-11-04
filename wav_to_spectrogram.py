#!/usr/python/env
import os
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from cv2 import imwrite

# dimensions of images
img_width, img_height = 75, 75


train_data_dir = 'speech_dataset/train_dir'
validation_data_dir = 'speech_dataset/validation_dir'

wav_count = 0

def length_directory(dir_name):
    numfiles = len([f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))])
    return numfiles

print(length_directory("data_processing_utilities/data/stream_recordings"))
'''
## Try/except loop

while length_directory("data_processing_utilities/data/stream_recordings") > wav_count:
    try:
        wav_file_name = wav_count + ".wav"
        print("reading file: " + wav_file_name)
        sample_rate, samples  =  wavfile.read("data_processing_utilities/data/stream_recordings/" + wav_file_name)
        wav_count += 1
        
        frequencies, times, spectrogram = signal.spectrogram(samples/sample_rate)
        plt.pcolormesh(times, frequencies, spectrogram)
        plt.axis('off')
        plt.tight_layout()
        #plt.ylabel('Frequency(Hz)')
        #plt.xlabel('Time(seconds)')
        #name = "speech_dataset/testing_dir/spectrogram%s.png" % str(count)
        name = "speech_dataset/testing_dir/spectrogram.png"
        plt.savefig(name, frameon='false', pad_inches=0.0, bbox_inches='tight')
        #plt.show()
        print('file printing now')  

    except:
        print('pass')
        pass

## Single File
while length_directory("data_processing_utilities/data/recording_test") > wav_count:
    wav_file_name = str(wav_count) + ".wav"
    print("reading file: " + wav_file_name)
    sample_rate, samples  =  wavfile.read("data_processing_utilities/data/recording_test/" + wav_file_name)
    wav_count += 1

    frequencies, times, spectrogram = signal.spectrogram(samples/sample_rate)
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.axis('off')
    plt.tight_layout()
    #plt.ylabel('Frequency(Hz)')
    #plt.xlabel('Time(seconds)')
    #name = "speech_dataset/testing_dir/spectrogram%s.png" % str(count)
    name = "speech_dataset/testing_dir/spectrogram.png"
    plt.savefig(name, frameon='false', pad_inches=0.0, bbox_inches='tight')
    #plt.show()
    print('file printing now')  

'''
for root, sub, files in os.walk('data_processing_utilities/data/recording_test'):
    print('reading files now')
    count = 0
    files = sorted(files)
    for f in files:
        while count <= 100:
            sample_rate, samples  =  wavfile.read(os.path.join(root, f))  # <---
            frequencies, times, spectrogram = signal.spectrogram(samples/sample_rate)
            plt.pcolormesh(times, frequencies, spectrogram)
            plt.axis('off')
            plt.tight_layout()
            #plt.ylabel('Frequency(Hz)')
            #plt.xlabel('Time(seconds)')
            #name = "speech_dataset/testing_dir/spectrogram%s.png" % str(count)
            name = "speech_dataset/testing_dir/spectrogram.png"
            plt.savefig(name, frameon='false', pad_inches=0.0, bbox_inches='tight')
            #plt.show()
            print('file printing now')    
            count+=1
            print(count)