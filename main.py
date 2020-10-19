# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:38:00 2020

@author: cantek

pip install sounddevice --user

"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import threading
import soundToWeigth


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("TheVoice")
        self.setStyleSheet(open("style.qss","r").read())
        self.setMinimumSize(QSize(500,200))
      #  self.setMaximumSize(QSize(500,300))
        self.show()
        

    def initUI(self):
        mainwindow=self.mainwindow()
        self.setCentralWidget(mainwindow)
    
    def mainwindow(self):
        
        gbGender=QGroupBox("Gender")
        gbGender.setFixedWidth(150)
        gbGender.setAlignment(Qt.AlignTop)
        gbAge=QGroupBox("Age")
        gbAge.setFixedWidth(150)
        gbPredict=QGroupBox("Predict")
        gbPredict.setFixedWidth(200)
        
       
        
        #Predict  
        
        tvLF, tvLT = QLabel("Length"), QLabel("Length")  
        tvTF, tvTT = QLabel("Thickness"), QLabel("Thickness")  
        tvWF, tvWT = QLabel("Width"), QLabel("Width")  
        
        tvLF.setObjectName("predictT")
        tvLT.setObjectName("predictT")
        tvTF.setObjectName("predictT")
        tvTT.setObjectName("predictT")
        tvWF.setObjectName("predictT")
        tvWT.setObjectName("predictT")
        
        tvLF.setFixedWidth(60)
        tvLT.setFixedWidth(60)
        tvTT.setFixedWidth(60)
        tvTF.setFixedWidth(60)
        tvWF.setFixedWidth(60)
        tvWT.setFixedWidth(60)
        
        hboxPredTitleRow1 = QHBoxLayout()
        hboxPredTitleRow1.addStretch(1)
        hboxPredTitleRow1.addWidget(tvLT)
        hboxPredTitleRow1.addWidget(tvWT)
        hboxPredTitleRow1.addWidget(tvTT)
        hboxPredTitleRow1.setAlignment(Qt.AlignHCenter)
        
        
        
        hboxPredTitleRow2 = QHBoxLayout()
        hboxPredTitleRow2.addStretch(1)
        hboxPredTitleRow2.addWidget(tvLF)
        hboxPredTitleRow2.addWidget(tvWF)
        hboxPredTitleRow2.addWidget(tvTF)
        hboxPredTitleRow2.setAlignment(Qt.AlignHCenter)
        
        self.vLF, self.vLT = QLabel("vLF"), QLabel("vLT")  
        self.vTF, self.vTT = QLabel("vTF"), QLabel("vTT")  
        self.vWF, self.vWT = QLabel("vWF"), QLabel("vWT")  
        
        self.vLF.setObjectName("predict")
        self.vLT.setObjectName("predict")
        self.vTF.setObjectName("predict")
        self.vTT.setObjectName("predict")
        self.vWF.setObjectName("predict")
        self.vWT.setObjectName("predict")
        
        self.vLF.setFixedWidth(60)
        self.vLT.setFixedWidth(60)
        self.vTT.setFixedWidth(60)
        self.vTF.setFixedWidth(60)
        self.vWF.setFixedWidth(60)
        self.vWT.setFixedWidth(60)
        
        hboxPredRow1 = QHBoxLayout()
        hboxPredRow1.addStretch(1)
        hboxPredRow1.addWidget(self.vLT)
        hboxPredRow1.addWidget(self.vWT)
        hboxPredRow1.addWidget(self.vTT)
        hboxPredRow1.setAlignment(Qt.AlignHCenter)
        
        hboxPredRow2 = QHBoxLayout()
        hboxPredRow2.addStretch(1)
        hboxPredRow2.addWidget(self.vLF)
        hboxPredRow2.addWidget(self.vWF)
        hboxPredRow2.addWidget(self.vTF)
        
        hboxPredRow2.setAlignment(Qt.AlignHCenter)
        
        vboxPredict = QVBoxLayout()
        vboxPredict.addStretch(1)    
        
        labelTVC = QLabel("True Vocal Cord")    
        labelTVC.setAlignment(Qt.AlignHCenter)
        labelTVC.setObjectName("cordTitle")
        vboxPredict.addWidget(labelTVC)
        vboxPredict.addLayout(hboxPredTitleRow1)
        vboxPredict.addLayout(hboxPredRow1)
        
        labelFVC = QLabel("False Vocal Cord")        
        labelFVC.setAlignment(Qt.AlignHCenter)
        labelFVC.setObjectName("cordTitle")
        vboxPredict.addWidget(labelFVC)
        vboxPredict.addLayout(hboxPredTitleRow2)
        vboxPredict.addLayout(hboxPredRow2)
        
        gbPredict.setLayout(vboxPredict)
        
       
        
      
        
        
        #Gender group
        self.rbGenderMale=QRadioButton("Male")
        self.rbGenderFemale=QRadioButton("Female")
        
        genderRbGroup=QButtonGroup()        
        genderRbGroup.addButton(self.rbGenderFemale)
        genderRbGroup.addButton(self.rbGenderMale)
        
        vboxGender = QVBoxLayout()
        vboxGender.addStretch(1)
        
        vboxGender.addWidget(self.rbGenderFemale)
        vboxGender.addWidget(self.rbGenderMale)
        vboxGender.setAlignment(Qt.AlignTop)
        gbGender.setLayout(vboxGender)
        
        
        
        #Age group
        self.rbAgeYoung=QRadioButton("Young")
        self.rbAgeAdult=QRadioButton("Adult")
        
        ageRbGroup=QButtonGroup()        
        ageRbGroup.addButton(self.rbAgeYoung)
        ageRbGroup.addButton(self.rbAgeAdult)
        
        vboxAge = QVBoxLayout()
        vboxAge.addStretch(1)
        
        vboxAge.addWidget(self.rbAgeAdult)
        vboxAge.addWidget(self.rbAgeYoung)
        
        gbAge.setLayout(vboxAge)
        
        btn = QPushButton("Start")
        btn.clicked.connect(self.tiklama)
        
        hboxRow1 = QHBoxLayout()
        hboxRow1.addStretch(1)
        hboxRow1.addWidget(gbGender)
        hboxRow1.addWidget(gbAge)
        hboxRow1.addWidget(gbPredict)
        
        
        
#        self.pbar = QProgressBar(self)
#        self.pbar.setGeometry(30, 40, 200, 25)

#        self.timer = QBasicTimer()
#        self.step = 0
#        btn.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        
        
        self.mesaj = QLabel("İnsanlar bunlara uyacak ve her şey daha güzel olacak düşüncesi \n doğru bir düşünce midir sizce de? ")
        self.mesaj.setObjectName("mesajAlani")
        self.mesaj.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
       # self.mesaj.hide()
        
        btn = QPushButton("Start")
        btn.clicked.connect(self.tiklama)

#        btn1 = QPushButton("btn1")
#        btn1.clicked.connect(self.changeTitle)
#        btn1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
              
        
        widget = QWidget()
        
        
        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
               
        v_box.addLayout(hboxRow1)
#        v_box.addWidget(self.pbar)
        v_box.addWidget(self.mesaj)
        v_box.addWidget(btn)
        
        widget.setLayout(v_box)
        
        return widget
        
            
            
    def tiklama(self):        
        #self.mesaj.show()    
        age = 1 # 1-young , 0 adult
        gender = 0 #1-male, 0-female
        if self.rbAgeAdult.isChecked() == True:
            age = 0
        if self.rbGenderMale.isChecked() == True:
            gender = 1
            
        d=soundToWeigth.soundToWeigt(age, gender)
        self.vLF.setText("{0:.2f}".format(d["vLF"][0]))
        self.vLT.setText("{0:.2f}".format(d["VLT"][0]))
        self.vTF.setText("{0:.2f}".format(d["vTF"][0]))
        self.vTT.setText("{0:.2f}".format(d["vTT"][0]))
        self.vWF.setText("{0:.2f}".format(d["vWF"][0]))
        self.vWT.setText("{0:.2f}".format(d["vWT"][0]))
#        self.result.setText(d)
        

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' fdfd')


def main():    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

