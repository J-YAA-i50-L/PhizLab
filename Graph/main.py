from PyQt5.QtWidgets import QApplication, QMainWindow
from serial.tools import list_ports
from PyQt5 import QtCore
# from PyQt5 import uic
import serial
import time
import sys
from pyui.main_window import Ui_MainWindow
from pyui.electricity import Ui_Electricity
from pyui.mkt_choice import Ui_MKTChoice
from pyui.mechanic import Ui_Mechanic
from pyui.pv import Ui_PV
from pyui.pt import Ui_PT
from pyui.vt import Ui_VT


class ReadThread(QtCore.QThread):
    def __init__(self, parent=None, connection=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.parent = parent
        if connection:
            self.connection = connection
        else:
            msg = 'Подключите устройство к ноутбуку и перезагрузите программу'
            self.parent.statusbar.showMessage(msg)
        self.plot_x_data = []
        self.plot_y_data = []

    def run(self):
        self.running = True
        while self.running:
            data = str(connection.readline())[2:-5]
            if self.parent.name != 'mechanic':
                ax_1_data, ax_2_data = [int(elem) for elem in data.split(' ')]
                self.plot_x_data.append(ax_1_data)
                self.plot_y_data.append(ax_2_data)
                self.parent.chart.clear()
                self.parent.chart.plot(self.plot_x_data, self.plot_y_data)
            else:
                ax_1_data = float(f'{time.perf_counter() - self.parent.begin:0.4f}')
                ax_2_data = int(data)
                self.plot_x_data.append(ax_1_data)
                self.plot_y_data.append(ax_2_data)
                self.parent.chart.clear()
                self.parent.chart.plot(self.plot_x_data, self.plot_y_data)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('ui/main_window.ui', self)
        self.setupUi(self)
        self.mechanic.clicked.connect(self.new_window)
        self.mkt.clicked.connect(self.new_window)
        self.electricity.clicked.connect(self.new_window)

    def new_window(self):
        if self.sender() == self.mechanic:
            target = Mechanic(self)
            target.show()
            self.hide()
        elif self.sender() == self.mkt:
            target = MKTChoice(self)
            target.show()
            self.hide()
        elif self.sender() == self.electricity:
            target = Electricity(self)
            target.show()
            self.hide()


class Mechanic(QMainWindow, Ui_Mechanic):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        global connection
        # uic.loadUi('ui/mechanic.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.name = 'mechanic'
        self.axes = ['x', 't']
        self.chart.setLabel('left', self.axes[0], units='м')
        self.chart.setLabel('bottom', self.axes[1], units='с')
        self.back.clicked.connect(self.get_back)
        self.ReadThread = ReadThread(parent=self, connection=connection)
        if choosen_port:
            self.start.clicked.connect(self.on_start)
            self.stop.clicked.connect(self.on_stop)
        else:
            self.start.setDisabled(True)
            self.stop.setDisabled(True)

    def on_start(self):
        if not self.ReadThread.isRunning():
            self.ReadThread.start()
            self.begin = float(f'{time.perf_counter():0.4f}')

    def on_stop(self):
        self.ReadThread.running = False

    def get_back(self):
        self.parent.show()
        self.hide()

    def closeEvent(self, event):
        self.ReadThread.running = False
        self.ReadThread.wait(1000)
        self.parent.show()
        self.close()


class Electricity(QMainWindow, Ui_Electricity):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        global connection
        # uic.loadUi('ui/electricity.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.axes = ['U', 'I']
        self.name = 'electricity'
        self.chart.setLabel('left', self.axes[0], units='В')
        self.chart.setLabel('bottom', self.axes[1], units='А')
        self.back.clicked.connect(self.get_back)
        self.ReadThread = ReadThread(parent=self, connection=connection)
        if choosen_port:
            self.start.clicked.connect(self.on_start)
            self.stop.clicked.connect(self.on_stop)
        else:
            self.start.setDisabled(True)
            self.stop.setDisabled(True)

    def on_start(self):
        if not self.ReadThread.isRunning():
            self.ReadThread.start()
            self.begin = float(f'{time.perf_counter():0.4f}')

    def on_stop(self):
        self.ReadThread.running = False

    def get_back(self):
        self.parent.show()
        self.hide()

    def closeEvent(self, event):
        self.ReadThread.running = False
        self.ReadThread.wait(1000)
        self.parent.show()
        self.close()


class MKTChoice(QMainWindow, Ui_MKTChoice):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        # uic.loadUi('ui/mkt_choice.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.back.clicked.connect(self.get_back)
        self.submit.clicked.connect(self.new_window)

    def new_window(self):
        if self.pv.isChecked():
            target = PV(self)
            target.show()
            self.hide()
        elif self.pt.isChecked():
            target = PT(self)
            target.show()
            self.hide()
        elif self.vt.isChecked():
            target = VT(self)
            target.show()
            self.hide()

    def get_back(self):
        self.parent.show()
        self.hide()

    def closeEvent(self, event):
        self.parent.show()
        self.close()


class PV(QMainWindow, Ui_PV):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        global connection
        # uic.loadUi('ui/pv.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.axes = ['P', 'V']
        self.name = 'pv'
        self.chart.setLabel('left', self.axes[0], units='Па')
        self.chart.setLabel('bottom', self.axes[1], units='л')
        self.back.clicked.connect(self.get_back)
        self.ReadThread = ReadThread(parent=self, connection=connection)
        if choosen_port:
            self.start.clicked.connect(self.on_start)
            self.stop.clicked.connect(self.on_stop)
        else:
            self.start.setDisabled(True)
            self.stop.setDisabled(True)

    def on_start(self):
        if not self.ReadThread.isRunning():
            self.ReadThread.start()
            self.begin = float(f'{time.perf_counter():0.4f}')

    def on_stop(self):
        self.ReadThread.running = False

    def get_back(self):
        self.parent.show()
        self.hide()

    def closeEvent(self, event):
        self.ReadThread.running = False
        self.ReadThread.wait(1000)
        self.parent.show()
        self.close()


class PT(QMainWindow, Ui_PT):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        global connection
        # uic.loadUi('ui/pt.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.axes = ['P', 'T']
        self.name = 'pt'
        self.chart.setLabel('left', self.axes[0], units='Па')
        self.chart.setLabel('bottom', self.axes[1], units='С')
        self.back.clicked.connect(self.get_back)
        self.ReadThread = ReadThread(parent=self, connection=connection)
        if choosen_port:
            self.start.clicked.connect(self.on_start)
            self.stop.clicked.connect(self.on_stop)
        else:
            self.start.setDisabled(True)
            self.stop.setDisabled(True)

    def on_start(self):
        if not self.ReadThread.isRunning():
            self.ReadThread.start()
            self.begin = float(f'{time.perf_counter():0.4f}')

    def on_stop(self):
        self.ReadThread.running = False

    def get_back(self):
        self.parent.show()
        self.hide()

    def closeEvent(self, event):
        self.ReadThread.running = False
        self.ReadThread.wait(1000)
        self.parent.show()
        self.close()


class VT(QMainWindow, Ui_VT):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        global connection
        # uic.loadUi('ui/vt.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.axes = ['V', 'T']
        self.name = 'vt'
        self.chart.setLabel('left', self.axes[0], units='л')
        self.chart.setLabel('bottom', self.axes[1], units='С')
        self.back.clicked.connect(self.get_back)
        self.ReadThread = ReadThread(parent=self, connection=connection)
        if choosen_port:
            self.start.clicked.connect(self.on_start)
            self.stop.clicked.connect(self.on_stop)
        else:
            self.start.setDisabled(True)
            self.stop.setDisabled(True)

    def on_start(self):
        if not self.ReadThread.isRunning():
            self.ReadThread.start()
            self.begin = float(f'{time.perf_counter():0.4f}')

    def on_stop(self):
        self.ReadThread.running = False

    def get_back(self):
        self.parent.show()
        self.hide()

    def closeEvent(self, event):
        self.ReadThread.running = False
        self.ReadThread.wait(1000)
        self.parent.show()
        self.close()


if __name__ == '__main__':
    choosen_port, connection = '', ''
    port_list = [str(elem) for elem in list_ports.comports()]
    for port in port_list:
        if 'последовательный порт' not in port.lower():
            choosen_port = port[:4]
    if choosen_port:
        connection = serial.Serial(choosen_port, 9600)
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
