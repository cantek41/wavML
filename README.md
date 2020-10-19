# wavML

The purpose of this study is to predict measure value of human true and false 
vocal cords from personal sound, using Machine Learning.


["Gender"]= #1-male, 0-female
["Age"]=#1-young, 0-adult

<img src="https://github.com/cantek41/wavML/blob/master/image/app.PNG"  width="200">


# How to work

cmd --> python wavToWeigth.py wavfile gender age

## example :

 
E:\theVoice\wavML>python wavToWeigth.py wavs\tr-0014.wav 1 1

tahminler

vLF = [12.75458479]    Length False Vocal Cords  mm

VLT = [12.22397778]    Length True Vocal Cords mm

vTF = [4.50374265]     Thickness False Vocal Cords mm

vTT = [4.33245914]     Thickness True Vocal Cords mm

vWF = [4.5851325]      Width False Vocal Cords mm

vWT = [4.13349566]     Width True Vocal Cords mm


# dataset
http://www.voxforge.org/tr


# requirements
librosa

joblib

sklearn

numpy

PyQt5

scipy

pip install sounddevice

# References

Qiao Hu, MS, Shang-Yong Zhu, MS, Feng Luo, MS,
Yong Gao, MS, Xi-Yue Yang, MS
High-Frequency Sonographic Measurements of True and False Vocal Cords
American Institute of Ultrasound in Medicine • J Ultrasound Med 2010; 29:1023–1030
