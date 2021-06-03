import sys
import os
import pandas as pd
from datetime import datetime
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from interface import Ui_ControlTanques
from PASSWORD import Ui_ClaveAdmin
from estadisticas import Ui_Estadisticas

# Application Class
class Application(QMainWindow, Ui_ControlTanques):
    #Método constructor de la clase
    def __init__(self, parent = None):
        super().__init__()
        #QMainWindow Start
        QMainWindow.__init__(self)
        # Ui_AnalisysCheck.__init__(self)
        self.setupUi(self)
        #Title
        self.setWindowTitle("CONTROL DE TEMPERATURA BELLAVISTA")
        # Add variables
        self.now = datetime.now()
        time = str(self.now.strftime("%H:%M:%S"))
        date = str(self.now.strftime("%y/%m/%d"))
        self.lb_hora.setText(time)
        self.lb_fecha.setText(date)
        #Agree new item
        self.bt_act_des.clicked.connect(self.fn_configuration_temp)
        self.actionAdmin.triggered.connect(self.fn_admin)
        self.actionEstadisticas.triggered.connect(self.fn_estadisticas)
        self.actionAcerca.triggered.connect(self.fn_about)
        self.dial_1.setMinimum(35)
        self.dial_1.setMaximum(65)
        self.dial_1.setValue(40)
        self.dial_2.setMinimum(35)
        self.dial_2.setMaximum(65)
        self.dial_2.setValue(40)
        # self.dial_1.disable()
        # self.dial_2.disable()
        #self.bt_act_des.disable()
        
        # self.actionSelecci_n.triggered.connect(self.fn_select)
        # self.actionSalirr.triggered.connect(self.fn_exit)
        # self.actionAcerca_de_Nosotros.triggered.connect(self.fn_about)


    def fn_configuration_temp(self):
    
        def __init__(self, parent= None):
            #QMainWindow Start
            super().__init__()
            QMainWindow.__init__(self,parent)
            #Charge MainWindow 
            self.setupUi(self)
            # uic.loadUi("acerca.ui", self)
            self.setWindowTitle("PASSWORD")

    def fn_admin(self):
        def __init__(self, parent= None):
            #QMainWindow Start
            super().__init__()
            QMainWindow.__init__(self,parent)
            #Charge MainWindow 
            self.setupUi(self)
            # uic.loadUi("acerca.ui", self)
            self.setWindowTitle("PASSWORD")

    def fn_estadisticas(self):
        
        def __init__(self, parent= None):
            #QMainWindow Start
            super().__init__()
            QMainWindow.__init__(self,parent)
            #Charge MainWindow 
            self.setupUi(self)
            # uic.loadUi("acerca.ui", self)
            self.setWindowTitle("Estadisticas")

    def fn_about(self):
         pass


if __name__ == "__main__": 
   dirname = os.path.dirname(PyQt5.__file__)
   plugin_path = os.path.join(dirname, 'plugins', 'platforms')
   app = QApplication(sys.argv)        #App Inicialization
   _Application = Application()        #Object Class
   _Application.show()                 #Show Window
   app.exec_()                         #Execute Aplication