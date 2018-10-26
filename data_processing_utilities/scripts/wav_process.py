#!/usr/bin/env python

from pydub import AudioSegment

t1 = 3000 #Works in milliseconds
t2 = 4500
newAudio = AudioSegment.from_wav("/home/nina/yes.wav")
newAudio = newAudio[t1:t2]
newAudio.export('/home/nina/catkin_ws/src/audio_bot/robot_learning/data_processing_utilities/data/yes.wav', format="wav") #Exports to a wav file in the current path.
