# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys,rs
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib, ssl
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(698, 651)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 30, 625, 565))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 191, 521))
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 120, 120, 255), stop:1 rgba(120, 230, 255, 255));\n"
"border-top-left-radius:50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(219, 30, 361, 521))
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(370, 50, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200)")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 140, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(329, 190, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(350, 450, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 120, 120, 255), stop:1 rgba(180, 255, 255, 255));\n"
"color:rgba(255,255,255,240);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(390, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0,0,0,200)")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(329, 240, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(329, 290, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(330, 340, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(280, 136, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(0,0,0,150)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(280, 236, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(0,0,0,150)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(276, 180, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0,0,0,150)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(280, 336, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(0,0,0,150)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(280, 286, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(0,0,0,150)")
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 30, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ev\'s Dragons")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(46,82,101,200);\n"
"color:rgba(20, 100, 100, 255);\n"
"padding-bottom:7px;\n"
"border:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "SMTP"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Sender Email"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.setText(_translate("Form", "Send"))
        
        self.label_5.setText(_translate("Form", "w q ) m"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Subject"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Receiver Email"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "message"))
        self.label_6.setText(_translate("Form", "Ñ"))
        self.label_7.setText(_translate("Form", "º"))
        self.label_8.setText(_translate("Form", "µ"))
        self.label_9.setText(_translate("Form", "ô"))
        self.label_10.setText(_translate("Form", "Ñ"))
        self.pushButton_2.setText(_translate("Form", "X"))
        self.pushButton_2.clicked.connect(form.close)
        self.pushButton.clicked.connect(self.send)
    def send (self):    
        
        server=smtplib.SMTP('64.233.184.108',587)
        server.starttls()
        server.login(self.lineEdit.text(),self.lineEdit_2.text())
        message='subject:'+self.lineEdit_3.text()+'\n'+self.plainTextEdit.toPlainText()
        server.sendmail(self.lineEdit.text(), self.lineEdit_4.text(),message)
        server.close()
        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    form=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())
