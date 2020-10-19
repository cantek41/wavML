# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:40:44 2020

@author: cantek
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:56:24 2020

@author: cantek
"""

import librosa
import numpy as np
import pandas as pd
import os
from joblib import load as modelLoad
#import sys

def analiz(voice,fs, gender, age):
    rowdf = pd.DataFrame(columns=['Gender', 'Age', 'chrMean', 'chrMedian', 'chrMin', 'chrMax', 'censMean', 'censMedian', 'censMin', 'censMax', 'melMean', 'melMedian', 'mfccMean', 'mfccMedian', 'mfccMin', 'mfccMax', 'rmsMean', 'rmsMedian', 'rmsMin', 'rmsMax', 'specCentMean', 'specCentMedian', 'tonnetzMean', 'tonnetzMedian', 'tonnetzMin', 'tonnetzMax', 'z0Mean', 'z0Median', 'z0Min', 'z0Max'])
    newRow={}
    #audio=sys.argv[1]#r"E:\theVoice\dataset\tr\ysfkck-20140609-jqt\wav\tr-0011.wav"
    newRow["Gender"]=gender#sys.argv[2] #1-male, 0-female
    newRow["Age"]=age #.argv[3]  #1-young (<18), 0-adult(18-39)
    
    #python wavToWeigth.py E:\theVoice\dataset\tr\ysfkck-20140609-jqt\wav\tr-0011.wav 1 1
    
    y, sr = voice, fs#librosa.load(audio)
    
    chr=librosa.feature.chroma_stft(y=y, sr=sr)
    newRow["chrMean"]=np.mean(chr)
    newRow["chrMedian"]=np.median(chr)
    newRow["chrMin"]=np.min(chr)
    newRow["chrMax"]=np.max(chr)
    
    cens = librosa.feature.chroma_cens(y=y, sr=sr)
    newRow["censMean"]=np.mean(cens)
    newRow["censMedian"]=np.median(cens)
    newRow["censMin"]=np.min(cens)
    newRow["censMax"]=np.max(cens)
    
    
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    newRow["melMean"]=np.mean(mel)
    newRow["melMedian"]=np.median(mel)
    #newRow["melMin"]=np.min(mel)
    #newRow["melMax"]=np.max(mel)
    
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    newRow["mfccMean"]=np.mean(mfcc)
    newRow["mfccMedian"]=np.median(mfcc)
    newRow["mfccMin"]=np.min(mfcc)
    newRow["mfccMax"]=np.max(mfcc)
    
    
    rms = librosa.feature.rms(y=y)
    newRow["rmsMean"]=np.mean(rms)
    newRow["rmsMedian"]=np.median(rms)
    newRow["rmsMin"]=np.min(rms)
    newRow["rmsMax"]=np.max(rms)
    
    
    specCent = librosa.feature.spectral_centroid(y=y, sr=sr)
    newRow["specCentMean"]=np.mean(specCent)
    newRow["specCentMedian"]=np.median(specCent)
    #newRow["specCentMin"]=np.min(specCent)
    #newRow["specCentMax"]=np.max(specCent)
    
    yy = librosa.effects.harmonic(y)
    tonnetz = librosa.feature.tonnetz(y=yy, sr=sr)
    newRow["tonnetzMean"]=np.mean(tonnetz)
    newRow["tonnetzMedian"]=np.median(tonnetz)
    newRow["tonnetzMin"]=np.min(tonnetz)
    newRow["tonnetzMax"]=np.max(tonnetz)
    
    z0=librosa.feature.zero_crossing_rate(y)
    newRow["z0Mean"]=np.mean(z0)
    newRow["z0Median"]=np.median(z0)
    newRow["z0Min"]=np.min(z0)
    newRow["z0Max"]=np.max(z0)
    
    rowdf=rowdf.append(newRow,ignore_index=True)
    path = os.getcwd()
    models=os.listdir(os.path.join(path,"models"))
    print("tahminler")
    tahminler={}
    for model in models:  
        loaded_model = modelLoad(os.path.join(path,"models",model))
        pred=loaded_model.predict(rowdf)
        name=model.split(".")[0]
        print("{0} = {1}".format(name,pred[0]))
        tahminler[name]=pred[0]
    return tahminler


