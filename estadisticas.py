# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadisticas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Estadisticas(object):
    def setupUi(self, Estadisticas):
        Estadisticas.setObjectName("Estadisticas")
        Estadisticas.resize(594, 366)
        self.centralwidget = QtWidgets.QWidget(Estadisticas)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 571, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 0, 431, 51))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 581, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(330, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gr_tan1 = QtWidgets.QGraphicsView(self.frame_2)
        self.gr_tan1.setGeometry(QtCore.QRect(10, 70, 271, 151))
        self.gr_tan1.setObjectName("gr_tan1")
        self.gr_tan2 = QtWidgets.QGraphicsView(self.frame_2)
        self.gr_tan2.setGeometry(QtCore.QRect(300, 70, 271, 151))
        self.gr_tan2.setObjectName("gr_tan2")
        self.bt_datos = QtWidgets.QPushButton(self.frame_2)
        self.bt_datos.setGeometry(QtCore.QRect(450, 240, 121, 31))
        self.bt_datos.setObjectName("bt_datos")
        Estadisticas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Estadisticas)
        self.statusbar.setObjectName("statusbar")
        Estadisticas.setStatusBar(self.statusbar)

        self.retranslateUi(Estadisticas)
        QtCore.QMetaObject.connectSlotsByName(Estadisticas)

    def retranslateUi(self, Estadisticas):
        _translate = QtCore.QCoreApplication.translate
        Estadisticas.setWindowTitle(_translate("Estadisticas", "MainWindow"))
        self.label.setText(_translate("Estadisticas", "Estadísticas de Temperatura"))
        self.label_2.setText(_translate("Estadisticas", "TANQUE 1 Y 2"))
        self.label_3.setText(_translate("Estadisticas", "TANQUE 3 Y 4"))
        self.bt_datos.setText(_translate("Estadisticas", "VER DATOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Estadisticas = QtWidgets.QMainWindow()
    ui = Ui_Estadisticas()
    ui.setupUi(Estadisticas)
    Estadisticas.show()
    sys.exit(app.exec_())
