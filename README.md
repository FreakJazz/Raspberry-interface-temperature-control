### Features

- Raspberry control temperature/ Python interface 
- Tanks control/ NTC thermistor
- Control PID and Hysteresis
- SUNLIFE company 
- Quito-Ecuador

# Raspberry Control Temperature Tank

![](https://github.com/FreakJazz/Raspberry-interface-temperature-control/blob/main/images/Solo%20Horizontal.png)


**Table of Contents**

[TOCM]

[TOC]

# Library Installation

In order to use the [Raspberry PI zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/ "Raspberry PI zero W"), we need to install the follw library.

`pip install RPI.GPIO`

Next for the interface in python we are going to use the [PYQT5](https://www.riverbankcomputing.com/static/Docs/PyQt5/ "PYQT5").

`pip intall PyQt5`

For the temperature control we need to install [PID library](https://pypi.org/project/pid/ "PID library").

`pip install pid`

In order to get stadistics for the temperature in a period of time we are gorin to use [Pandas](https://pandas.pydata.org/ "Pandas") and [matplot library](https://matplotlib.org/ "matplot library").

`pip install pandas`
`pip install matplotlib-inline`

# Programation

In the interface, two access codes were configured to be able to vary the setpoint of the temperature in the tanks, there is also a window where you can see a temperature history for system monitoring and generate statistics.

```python
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
```

# Interface

The interface is very intuitive and controls the temperature of 4 tanks through the NTC 20k sensors.

# PCB Desing

![PCB DESING](https://github.com/FreakJazz/Raspberry-interface-temperature-control/blob/main/images/pbc%20desing.PNG)

![PCB DESING 3D](https://github.com/FreakJazz/Raspberry-interface-temperature-control/blob/main/images/pbc%20desing%203D.PNG)


# Results
The temperature control of 4 tanks was carried out using a Raspberry Pi Zero W and a 7' touch screen. The control was carried out using hysteresis with a temperature set point of 28° to 55° Celsius.

Below is the temperature control installed in an electrical panel for tank control.

![PCB DESING 3D](https://github.com/FreakJazz/Raspberry-interface-temperature-control/blob/main/images/pbc%20desing%203D.PNG)


# Contributing

