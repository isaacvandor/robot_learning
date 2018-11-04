#!/usr/bin/env python

from pydub import AudioSegment
import soundfile as sf
import time

#'/home/nina/catkin_ws/src/audio_bot/robot_learning/data_processing_utilities
size_threshold = 21000
T1 = 0
T2 = 1500 #milliseconds
Interval = 100
stream_file = '../data/stream_recordings/stream.wav'
newAudio = AudioSegment.from_wav(stream_file)
time.sleep(1.5)
print("Wav files starting to be written")
i = 0

while sf.info(stream_file).duration > (T2/1000):
    segment = newAudio[T1:T2]
    name = str(i)
    segment.export('../data/ogg_files/%s.ogg' %name, format="ogg")
    size = sf.info('../data/ogg_files/%s.ogg' %name, verbose=True).extra_info
    beg = size.index("Length")+9
    end = size.index("\n", beg)
    size = int(size[beg:end])
    '''
    if size > size_threshold:
    '''
    segment.export('../data/stream_recordings/%s.wav' %name, format="wav")
    i += 1
    T1 += Interval
    T2 += Interval
    time.sleep(Interval/1000)
