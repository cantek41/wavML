# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:01:09 2020

@author: cantek
"""

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import voiceToWeight as voice

def soundToWeigt(age, gender):
    fs=48000
    duration = 10 
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float32')
    print ("Recording Audio")
    sd.wait()
    print ("Audio recording complete , Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    x=myrecording.T[0]
    x=x.T
    data=voice.analiz(x, fs, gender, age)
    return data