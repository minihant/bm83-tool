# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\0-Hant\pythonAPP\Pyserial-Demo\ui_demo_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(893, 652)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 10, 201, 321))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.formGroupBox.setFont(font)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.s1__box_1.setFont(font)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.state_label)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(230, 10, 561, 321))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.verticalGroupBox.setFont(font)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.s2__receive_text.setFont(font)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(230, 350, 551, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.verticalGroupBox_2.setFont(font)
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(20, 350, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.formGroupBox1.setFont(font)
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox1)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.timer_send_cb = QtWidgets.QCheckBox(Form)
        self.timer_send_cb.setGeometry(QtCore.QRect(240, 430, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.timer_send_cb.setFont(font)
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 430, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dw = QtWidgets.QLabel(Form)
        self.dw.setGeometry(QtCore.QRect(440, 430, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dw.setFont(font)
        self.dw.setObjectName("dw")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 540, 851, 101))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.s4__RX_Mode = QtWidgets.QPushButton(self.groupBox)
        self.s4__RX_Mode.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.s4__RX_Mode.setFont(font)
        self.s4__RX_Mode.setAutoRepeatInterval(100)
        self.s4__RX_Mode.setDefault(True)
        self.s4__RX_Mode.setObjectName("s4__RX_Mode")
        self.s4__Toggle_Linein = QtWidgets.QPushButton(self.groupBox)
        self.s4__Toggle_Linein.setGeometry(QtCore.QRect(270, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4__Toggle_Linein.setFont(font)
        self.s4__Toggle_Linein.setAutoRepeatInterval(100)
        self.s4__Toggle_Linein.setDefault(True)
        self.s4__Toggle_Linein.setObjectName("s4__Toggle_Linein")
        self.s4__TX_Mode = QtWidgets.QPushButton(self.groupBox)
        self.s4__TX_Mode.setGeometry(QtCore.QRect(20, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.s4__TX_Mode.setFont(font)
        self.s4__TX_Mode.setAutoRepeatInterval(100)
        self.s4__TX_Mode.setDefault(True)
        self.s4__TX_Mode.setObjectName("s4__TX_Mode")
        self.s4__Pairing = QtWidgets.QPushButton(self.groupBox)
        self.s4__Pairing.setGeometry(QtCore.QRect(140, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4__Pairing.setFont(font)
        self.s4__Pairing.setAutoRepeatInterval(100)
        self.s4__Pairing.setDefault(True)
        self.s4__Pairing.setObjectName("s4__Pairing")
        self.s4__Inquire = QtWidgets.QPushButton(self.groupBox)
        self.s4__Inquire.setGeometry(QtCore.QRect(140, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4__Inquire.setFont(font)
        self.s4__Inquire.setAutoRepeatInterval(100)
        self.s4__Inquire.setDefault(True)
        self.s4__Inquire.setObjectName("s4__Inquire")
        self.s4__Clear_EEPROM = QtWidgets.QPushButton(self.groupBox)
        self.s4__Clear_EEPROM.setGeometry(QtCore.QRect(400, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4__Clear_EEPROM.setFont(font)
        self.s4__Clear_EEPROM.setAutoRepeatInterval(100)
        self.s4__Clear_EEPROM.setDefault(True)
        self.s4__Clear_EEPROM.setObjectName("s4__Clear_EEPROM")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(790, 360, 91, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.s3__clear_button = QtWidgets.QPushButton(self.groupBox_2)
        self.s3__clear_button.setGeometry(QtCore.QRect(10, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s3__clear_button.setFont(font)
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.s3__send_button = QtWidgets.QPushButton(self.groupBox_2)
        self.s3__send_button.setGeometry(QtCore.QRect(10, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s3__send_button.setFont(font)
        self.s3__send_button.setObjectName("s3__send_button")
        self.hex_send = QtWidgets.QCheckBox(self.groupBox_2)
        self.hex_send.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.hex_send.setFont(font)
        self.hex_send.setObjectName("hex_send")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(790, 250, 91, 80))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.s2__clear_button = QtWidgets.QPushButton(self.groupBox_3)
        self.s2__clear_button.setGeometry(QtCore.QRect(10, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s2__clear_button.setFont(font)
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.hex_receive = QtWidgets.QCheckBox(self.groupBox_3)
        self.hex_receive.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.hex_receive.setFont(font)
        self.hex_receive.setObjectName("hex_receive")
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.formGroupBox.raise_()
        self.timer_send_cb.raise_()
        self.lineEdit_3.raise_()
        self.dw.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "Setup"))
        self.s1__lb_1.setText(_translate("Form", "port check"))
        self.s1__box_1.setText(_translate("Form", "Check"))
        self.s1__lb_2.setText(_translate("Form", "port"))
        self.s1__box_3.setItemText(0, _translate("Form", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "Length"))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "Parity"))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.s1__lb_6.setText(_translate("Form", "Stop"))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.open_button.setText(_translate("Form", "Open Port"))
        self.close_button.setText(_translate("Form", "Close Port"))
        self.s1__lb_3.setText(_translate("Form", "BardRate："))
        self.verticalGroupBox.setTitle(_translate("Form", "Log"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "Send"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">PAIRING_KEY</span></p></body></html>"))
        self.formGroupBox1.setTitle(_translate("Form", "Port Status"))
        self.label.setText(_translate("Form", "receives"))
        self.label_2.setText(_translate("Form", "sends"))
        self.timer_send_cb.setText(_translate("Form", "Send Interval"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.dw.setText(_translate("Form", "ms"))
        self.groupBox.setTitle(_translate("Form", "Cmd"))
        self.s4__RX_Mode.setText(_translate("Form", "RX Mode"))
        self.s4__Toggle_Linein.setText(_translate("Form", "Toggle Linein"))
        self.s4__TX_Mode.setText(_translate("Form", "TX Mode"))
        self.s4__Pairing.setText(_translate("Form", "Pairing"))
        self.s4__Inquire.setText(_translate("Form", "Inquiring"))
        self.s4__Clear_EEPROM.setText(_translate("Form", "Clear EEPROM"))
        self.s3__clear_button.setText(_translate("Form", "Clean"))
        self.s3__send_button.setText(_translate("Form", "Send"))
        self.hex_send.setText(_translate("Form", "Hex Send"))
        self.s2__clear_button.setText(_translate("Form", "Clear"))
        self.hex_receive.setText(_translate("Form", "Hex Recv"))
