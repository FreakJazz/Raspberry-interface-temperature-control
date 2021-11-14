import sys
import os
# import pandas as pd
from datetime import datetime
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from interface import Ui_ControlTanques
from PASSWORD import Ui_ClaveAdmin
from estadisticas import Ui_Estadisticas
from acerca import Ui_MainWindow
from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values(".env")
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
        self.dial_1.valueChanged.connect(self.updateLCD_set_1)
        self.dial_2.valueChanged.connect(self.updateLCD_set_2)
        
        # self.actionSelecci_n.triggered.connect(self.fn_select)
        # self.actionSalirr.triggered.connect(self.fn_exit)
        # self.actionAcerca_de_Nosotros.triggered.connect(self.fn_about)
    def updateLCD_set_1(self, event):
        self.lcd_temp_set_1.display(event)

    def updateLCD_set_2(self, event):
        self.lcd_temp_set_2.display(event)

    def fn_configuration_temp(self):
    
        self.mode_password = False
        self.password_frame = Admin(None)
        self.password_frame.show()
        
    def fn_admin(self):    
        self.mode_password = True
        self.password_frame = Admin(None)
        self.password_frame.show()

    def fn_estadisticas(self):
        self.estadisticas_frame = Estadisticas(None)
        self.estadisticas_frame.show()

    def fn_about(self):
        self.about_frame = About(None)
        self.about_frame.show()

class Admin(QMainWindow, Ui_ClaveAdmin):
    
    def __init__(self, parent= None):
        #QMainWindow Start
        super().__init__()
        QMainWindow.__init__(self,parent)
        #Charge MainWindow 
        self.setupUi(self)
        # uic.loadUi("acerca.ui", self)
        self.setWindowTitle("PASSWORD")
        self.bt_1.clicked.connect(self.fn_num_1)
        self.bt_2.clicked.connect(self.fn_num_2)
        self.bt_3.clicked.connect(self.fn_num_3)
        self.bt_4.clicked.connect(self.fn_num_4)
        self.bt_5.clicked.connect(self.fn_num_5)
        self.bt_6.clicked.connect(self.fn_num_6)
        self.bt_7.clicked.connect(self.fn_num_7)
        self.bt_8.clicked.connect(self.fn_num_8)
        self.bt_9.clicked.connect(self.fn_num_9)
        self.bt_0.clicked.connect(self.fn_num_0)
        self.bt_clear.clicked.connect(self.fn_clear)
        self.bt_ok.clicked.connect(self.fn_ok)
        self.bt_borrar.clicked.connect(self.fn_borrar)
    
    def char_len(self,password, char):
        lenght = len(password)
        if lenght <= 6:
            new_pass = str(password)+char
            return new_pass
        else:
            return password

    def fn_num_1(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "1")
        self.lineEdit.setText(new_pass)

    def fn_num_2(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "2")
        self.lineEdit.setText(new_pass)
    
    def fn_num_3(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "3")
        self.lineEdit.setText(new_pass)

    def fn_num_4(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "4")
        self.lineEdit.setText(new_pass)

    def fn_num_5(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "5")
        self.lineEdit.setText(new_pass)

    def fn_num_6(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "6")
        self.lineEdit.setText(new_pass)

    def fn_num_7(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "7")
        self.lineEdit.setText(new_pass)

    def fn_num_8(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "8")
        self.lineEdit.setText(new_pass)

    def fn_num_9(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "9")
        self.lineEdit.setText(new_pass)

    def fn_num_0(self):
        self.password =  self.lineEdit.text()
        new_pass = self.char_len(self.password, "0")
        self.lineEdit.setText(new_pass)

    def fn_clear(self):
        self.lineEdit.setText("")

    def fn_borrar(self):
        self.password =  self.lineEdit.text()
        lenght = len(self.password)-1
        list_pass = list(self.password)
        new_pass = ""
        for x in range(0,lenght):
            new_pass = new_pass + str(list_pass[x])
        self.lineEdit.setText(new_pass)

    def fn_ok(self):
        self.password =  self.lineEdit.text()
        num = int(self.lb_try_number.text())

        if self.password == os.getenv('FIRSTPASSWORD') and Application.mode_password == True:
            self.lb_state.setText("CORRECTO")
            Application.bt_act_des.setEnabled(True)
            self.close()
        elif self.password == os.getenv('SECONDPASSWORD') and Application.mode_password == False:
            self.lb_state.setText("CORRECTO")
            Application.dial_1.setEnabled(True)
            Application.dial_2.setEnabled(True)
            self.close()
        else:
            if num <= 1:
               self.lb_state.setText("ERROR") 
               self.lb_try_number.setText(str(num+1))
               self.lineEdit.clear()
            else: 
                self.bt_1.setEnabled(False)
                self.bt_2.setEnabled(False)
                self.bt_3.setEnabled(False)
                self.bt_4.setEnabled(False)
                self.bt_5.setEnabled(False)
                self.bt_6.setEnabled(False)
                self.bt_7.setEnabled(False)
                self.bt_8.setEnabled(False)
                self.bt_9.setEnabled(False)
                self.bt_0.setEnabled(False)
                self.bt_clear.setEnabled(False)
                self.bt_ok.setEnabled(False)
                self.bt_borrar.setEnabled(False)

class Estadisticas(QMainWindow, Ui_Estadisticas):        
    def __init__(self, parent= None):
        #QMainWindow Start
        super().__init__()
        QMainWindow.__init__(self,parent)
        #Charge MainWindow 
        self.setupUi(self)
        # uic.loadUi("acerca.ui", self)
        self.setWindowTitle("Estadisticas")

    
class About(QMainWindow, Ui_MainWindow):   
    def __init__(self, parent= None):
        #QMainWindow Start
        super().__init__()
        QMainWindow.__init__(self,parent)
        #Charge MainWindow 
        self.setupUi(self)
        # uic.loadUi("acerca.ui", self)
        self.setWindowTitle("Acerca de nosotros")
        pixmap = QPixmap('images/SUNLIFE.png')
        self.label.setPixmap(pixmap)
        self.show()
        self.aceptar.clicked.connect(self.fn_aceptar)

    def fn_aceptar(self):
        self.close()


if __name__ == "__main__": 
   dirname = os.path.dirname(PyQt5.__file__)
   plugin_path = os.path.join(dirname, 'plugins', 'platforms')
   app = QApplication(sys.argv)        #App Inicialization
   Application = Application()        #Object Class
   Application.show()                 #Show Window
   app.exec_()                         #Execute Aplication