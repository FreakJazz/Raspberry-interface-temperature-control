# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlTanques(object):
    def setupUi(self, ControlTanques):
        ControlTanques.setObjectName("ControlTanques")
        ControlTanques.resize(657, 460)
        self.centralwidget = QtWidgets.QWidget(ControlTanques)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 491, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 571, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.bt_act_des = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bt_act_des.setEnabled(False)
        self.bt_act_des.setObjectName("bt_act_des")
        self.gridLayout.addWidget(self.bt_act_des, 3, 0, 1, 1)
        self.lb_hora = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_hora.setFont(font)
        self.lb_hora.setObjectName("lb_hora")
        self.gridLayout.addWidget(self.lb_hora, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lb_fecha = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_fecha.setFont(font)
        self.lb_fecha.setObjectName("lb_fecha")
        self.gridLayout.addWidget(self.lb_fecha, 0, 1, 1, 1)
        self.lb_des_act = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_des_act.setFont(font)
        self.lb_des_act.setObjectName("lb_des_act")
        self.gridLayout.addWidget(self.lb_des_act, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.sb_delta = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sb_delta.setObjectName("sb_delta")
        self.gridLayout.addWidget(self.sb_delta, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 170, 581, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dial_1 = QtWidgets.QDial(self.frame)
        self.dial_1.setEnabled(False)
        self.dial_1.setGeometry(QtCore.QRect(470, 20, 91, 81))
        self.dial_1.setObjectName("dial_1")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(50, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(240, 10, 91, 20))
        self.label_8.setObjectName("label_8")
        self.lcd_temp_set_1 = QtWidgets.QLCDNumber(self.frame)
        self.lcd_temp_set_1.setGeometry(QtCore.QRect(350, 30, 101, 41))
        self.lcd_temp_set_1.setObjectName("lcd_temp_set_1")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lcd_temp_act_1 = QtWidgets.QLCDNumber(self.frame)
        self.lcd_temp_act_1.setGeometry(QtCore.QRect(230, 30, 101, 41))
        self.lcd_temp_act_1.setObjectName("lcd_temp_act_1")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(360, 10, 91, 20))
        self.label_9.setObjectName("label_9")
        self.lb_est_resistencia = QtWidgets.QLabel(self.frame)
        self.lb_est_resistencia.setEnabled(True)
        self.lb_est_resistencia.setGeometry(QtCore.QRect(240, 80, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_est_resistencia.setFont(font)
        self.lb_est_resistencia.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_est_resistencia.setObjectName("lb_est_resistencia")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 290, 581, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dial_2 = QtWidgets.QDial(self.frame_2)
        self.dial_2.setEnabled(False)
        self.dial_2.setGeometry(QtCore.QRect(470, 20, 91, 81))
        self.dial_2.setObjectName("dial_2")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(50, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(240, 10, 91, 20))
        self.label_10.setObjectName("label_10")
        self.lcd_temp_set_2 = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_temp_set_2.setGeometry(QtCore.QRect(350, 30, 101, 41))
        self.lcd_temp_set_2.setObjectName("lcd_temp_set_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lcd_temp_act_2 = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_temp_act_2.setGeometry(QtCore.QRect(230, 30, 101, 41))
        self.lcd_temp_act_2.setObjectName("lcd_temp_act_2")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(360, 10, 91, 20))
        self.label_14.setObjectName("label_14")
        self.lb_est_resistencia_2 = QtWidgets.QLabel(self.frame_2)
        self.lb_est_resistencia_2.setGeometry(QtCore.QRect(240, 80, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_est_resistencia_2.setFont(font)
        self.lb_est_resistencia_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_est_resistencia_2.setObjectName("lb_est_resistencia_2")
        ControlTanques.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ControlTanques)
        self.statusbar.setObjectName("statusbar")
        ControlTanques.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(ControlTanques)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menubar.setObjectName("menubar")
        self.menuPrincipal = QtWidgets.QMenu(self.menubar)
        self.menuPrincipal.setObjectName("menuPrincipal")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        ControlTanques.setMenuBar(self.menubar)
        self.actionAdmin = QtWidgets.QAction(ControlTanques)
        self.actionAdmin.setObjectName("actionAdmin")
        self.actionEstadisticas = QtWidgets.QAction(ControlTanques)
        self.actionEstadisticas.setObjectName("actionEstadisticas")
        self.actionAcerca = QtWidgets.QAction(ControlTanques)
        self.actionAcerca.setObjectName("actionAcerca")
        self.menuPrincipal.addAction(self.actionAdmin)
        self.menuAyuda.addAction(self.actionAcerca)
        self.menubar.addAction(self.menuPrincipal.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(ControlTanques)
        QtCore.QMetaObject.connectSlotsByName(ControlTanques)

    def retranslateUi(self, ControlTanques):
        _translate = QtCore.QCoreApplication.translate
        ControlTanques.setWindowTitle(_translate("ControlTanques", "MainWindow"))
        self.label.setText(_translate("ControlTanques", "Sistema de Calentamiento de Agua"))
        self.bt_act_des.setText(_translate("ControlTanques", "Activar/Desactivar"))
        self.lb_hora.setText(_translate("ControlTanques", "TextLabel"))
        self.label_7.setText(_translate("ControlTanques", "Activar o desactivar el control por resistencias en el tanque"))
        self.label_4.setText(_translate("ControlTanques", "Control de temperatura"))
        self.lb_fecha.setText(_translate("ControlTanques", "TextLabel"))
        self.lb_des_act.setText(_translate("ControlTanques", "Desactivo"))
        self.label_5.setText(_translate("ControlTanques", "Estado"))
        self.label_6.setText(_translate("ControlTanques", "Delta"))
        self.label_11.setText(_translate("ControlTanques", "Resistencia 1 y 2"))
        self.label_8.setText(_translate("ControlTanques", "T. Actual"))
        self.label_2.setText(_translate("ControlTanques", "Temperatura Tanque 1 y 2"))
        self.label_9.setText(_translate("ControlTanques", "T. Requerida"))
        self.lb_est_resistencia.setText(_translate("ControlTanques", "Activado"))
        self.label_13.setText(_translate("ControlTanques", "Resistencia 3 y 4"))
        self.label_10.setText(_translate("ControlTanques", "T. Actual"))
        self.label_3.setText(_translate("ControlTanques", "Temperatura Tanque 3 y 4"))
        self.label_14.setText(_translate("ControlTanques", "T. Requerida"))
        self.lb_est_resistencia_2.setText(_translate("ControlTanques", "Activado"))
        self.menuPrincipal.setTitle(_translate("ControlTanques", "Principal"))
        self.menuAyuda.setTitle(_translate("ControlTanques", "Soporte"))
        self.actionAdmin.setText(_translate("ControlTanques", "Admin"))
        self.actionEstadisticas.setText(_translate("ControlTanques", "Estadisticas"))
        self.actionAcerca.setText(_translate("ControlTanques", "Acerca de nosotros"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControlTanques = QtWidgets.QMainWindow()
    ui = Ui_ControlTanques()
    ui.setupUi(ControlTanques)
    ControlTanques.show()
    sys.exit(app.exec_())
