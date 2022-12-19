from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMainWindow, QApplication, QTabWidget, QPushButton, QLabel
import sys
from PyQt5 import uic
from PyQt5 import QtCore
# from electrical import Ui_electrical
# from gerkony_data import Ui_gerkony_data
# from uzi_data import Ui_uzi_data
# from main_window import Ui_mainWindow
# from mechanic import Ui_mechanic
# from molecular import Ui_molecular
# from amp_data import Ui_amp_data
# from volt_data import Ui_volt_data
# from obj_data import Ui_obj_data
# from press_data import Ui_press_data
# from temp_data import Ui_temp_data
# from pokaz import Ui_Pokaz


portt = ''


class MainWindow(QMainWindow):
    def __init__(self):
        global portt
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.mech.clicked.connect(self.show_mech)
        self.molec.clicked.connect(self.show_molec)
        self.elec.clicked.connect(self.show_elec)
        self.statusbar.showMessage(portt)

    def show_mech(self):
        mechanical = Mechanic(self)
        mechanical.show()
        self.hide()

    def show_molec(self):
        molecular = Molecular(self)
        molecular.show()
        self.hide()

    def show_elec(self):
        electrical = Electrical(self)
        electrical.show()
        self.hide()


class Mechanic(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('mechanic.ui', self)
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.submit.clicked.connect(self.submitting)

    def submitting(self):
        ch = []
        if self.gerkony_btn.isChecked():
            ch.append(self.gerkony_btn)
        if self.uzi_btn.isChecked():
            ch.append(self.uzi_btn)
        choice = MechChoosen(self, ch)
        choice.show()
        self.hide()

    def show_parent(self):
        self.parent.show()
        self.close()


class Molecular(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('molecular', self)
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.submit.clicked.connect(self.submitting)

    def submitting(self):
        ch = []
        if self.temper_btn.isChecked():
            ch.append(self.temper_btn)
        if self.pressure_btn.isChecked():
            ch.append(self.pressure_btn)
        if self.obj_btn.isChecked():
            ch.append(self.obj_btn)
        choice = MolecChoosen(self, ch)
        choice.show()
        self.hide()

    def show_parent(self):
        self.parent.show()
        self.close()


class Electrical(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('electrical.ui', self)
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.submit.clicked.connect(self.submitting)

    def submitting(self):
        ch = []
        if self.amperm_btn.isChecked():
            ch.append(self.amperm_btn)
        if self.voltm_btn.isChecked():
            ch.append(self.voltm_btn)
        choice = ElecChoosen(self, ch)
        choice.show()
        self.hide()

    def show_parent(self):
        self.parent.show()
        self.close()


class MechChoosen(QWidget):
    def __init__(self, parent=None, choice=[]):
        super().__init__(parent, QtCore.Qt.Window)
        self.parent = parent
        self.choice = []
        if self.parent.gerkony_btn in choice:
            self.choice.append(GerkonyData(self))
        if self.parent.uzi_btn in choice:
            self.choice.append(UziData(self))
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle('MechChoosen')
        if self.choice:
            self.tab_plate = QTabWidget(self)
            self.tab_plate.move(0, 0)
            self.tab_plate.resize(700, 500)
            for elem in self.choice:
                self.tab_plate.addTab(elem, elem.tab_name)
        else:
            self.lbl = QLabel(self)
            self.lbl.resize(200, 100)
            self.lbl.move(300, 200)
            self.lbl.setText('Вы ничего не выбрали.')
            self.bck_btn = QPushButton(self)
            self.bck_btn.resize(81, 31)
            self.bck_btn.move(0, 0)
            self.bck_btn.setText('Назад')
            self.bck_btn.clicked.connect(self.show_parent)

    def show_parent(self):
        self.parent.show()
        self.close()


class MolecChoosen(QWidget):
    def __init__(self, parent=None, choice=[]):
        super().__init__(parent, QtCore.Qt.Window)
        self.parent = parent
        self.choice = []
        if self.parent.temper_btn in choice:
            self.choice.append(TempData(self))
        if self.parent.pressure_btn in choice:
            self.choice.append(PressData(self))
        if self.parent.obj_btn in choice:
            self.choice.append(ObjData(self))
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle('MolecChoosen')
        if self.choice:
            self.tab_plate = QTabWidget(self)
            self.tab_plate.move(0, 0)
            self.tab_plate.resize(700, 500)
            for elem in self.choice:
                self.tab_plate.addTab(elem, elem.tab_name)
        else:
            self.lbl = QLabel(self)
            self.lbl.resize(200, 100)
            self.lbl.move(300, 200)
            self.lbl.setText('Вы ничего не выбрали.')
            self.bck_btn = QPushButton(self)
            self.bck_btn.resize(81, 31)
            self.bck_btn.move(0, 0)
            self.bck_btn.setText('Назад')
            self.bck_btn.clicked.connect(self.show_parent)

    def show_parent(self):
        self.parent.show()
        self.close()


class ElecChoosen(QWidget):
    def __init__(self, parent=None, choice=[]):
        super().__init__(parent, QtCore.Qt.Window)
        self.parent = parent
        self.choice = []
        if self.parent.amperm_btn in choice:
            self.choice.append(AmpData(self))
        if self.parent.voltm_btn in choice:
            self.choice.append(VoltData(self))
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle('ElecChoosen')
        if self.choice:
            self.tab_plate = QTabWidget(self)
            self.tab_plate.move(0, 0)
            self.tab_plate.resize(700, 500)
            for elem in self.choice:
                self.tab_plate.addTab(elem, elem.tab_name)
        else:
            self.lbl = QLabel(self)
            self.lbl.resize(200, 100)
            self.lbl.move(300, 200)
            self.lbl.setText('Вы ничего не выбрали.')
            self.bck_btn = QPushButton(self)
            self.bck_btn.resize(81, 31)
            self.bck_btn.move(0, 0)
            self.bck_btn.setText('Назад')
            self.bck_btn.clicked.connect(self.show_parent)

    def show_parent(self):
        self.parent.show()
        self.close()


class GerkonyData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('gerkony_data.ui', self)
        self.tab_name = 'Герконы'
        self.parent = parent
        self.vals = []
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        try:
            self.table.setRowCount(0)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(['Расстояние', 'Время'])
            self.ongoing = True
        except Exception as e:
            print(e)

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                time = 500
                v = [len(self.vals), time]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                self.table.setItem(0, 0, item1)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class UziData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('uzi_data.ui', self)
        self.tab_name = 'Узи'
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        self.table = pokazTable(self)
        self.table.table.setRowCount(2)
        self.table.table.setColumnCount(2)
        self.ongoing = True
        self.right = False

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
            while not self.right:
                if self.stop.clicked():
                    right = True
                print('fffffffffffffffffffffffffffff')
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
            try:
                self.table.show()
            except Exception as e:
                print(e)
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                v = [len(self.vals), 0]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                item2 = QTableWidgetItem(str(v[1]))
                self.table.table.setItem(0, 0, item1)
                self.table.table.setItem(0, 1, item2)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class TempData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('temp_data.ui', self)
        self.tab_name = 'Датчик температуры'
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        self.table = pokazTable(self)
        self.table.table.setRowCount(2)
        self.table.table.setColumnCount(2)
        self.ongoing = True

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
            try:
                self.table.show()
            except Exception as e:
                print(e)
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                v = [len(self.vals), 0]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                item2 = QTableWidgetItem(str(v[1]))
                self.table.table.setItem(0, 0, item1)
                self.table.table.setItem(0, 1, item2)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class PressData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('press_data.ui', self)
        self.tab_name = 'Датчик давления'
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        self.table = pokazTable(self)
        self.table.table.setRowCount(2)
        self.table.table.setColumnCount(2)
        self.ongoing = True

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
            try:
                self.table.show()
            except Exception as e:
                print(e)
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                v = [len(self.vals), 0]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                item2 = QTableWidgetItem(str(v[1]))
                self.table.table.setItem(0, 0, item1)
                self.table.table.setItem(0, 1, item2)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class ObjData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('obj_data', self)
        self.tab_name = 'Датчик объема'
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        self.table = pokazTable(self)
        self.table.table.setRowCount(2)
        self.table.table.setColumnCount(2)
        self.ongoing = True

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
            try:
                self.table.show()
            except Exception as e:
                print(e)
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                v = [len(self.vals), 0]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                item2 = QTableWidgetItem(str(v[1]))
                self.table.table.setItem(0, 0, item1)
                self.table.table.setItem(0, 1, item2)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class AmpData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('amp_data.ui', self)
        self.tab_name = 'Амперметр'
        self.parent = parent
        self.vals = []
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        self.table = pokazTable(self)
        self.table.table.setRowCount(2)
        self.table.table.setColumnCount(2)
        self.ongoing = True

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
            try:
                self.table.show()
            except Exception as e:
                print(e)
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                v = [len(self.vals), 0]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                item2 = QTableWidgetItem(str(v[1]))
                self.table.table.setItem(0, 0, item1)
                self.table.table.setItem(0, 1, item2)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class VoltData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('volt_data.ui', self)
        self.tab_name = 'Вольтметр'
        self.parent = parent
        self.back_button.clicked.connect(self.show_parent)
        self.start.clicked.connect(self.go)
        self.stop.clicked.connect(self.go)
        self.add.clicked.connect(self.go)
        self.table = pokazTable(self)
        self.table.table.setRowCount(2)
        self.table.table.setColumnCount(2)
        self.ongoing = True

    def go(self):
        if self.sender().text() == 'Старт':
            self.ongoing = True
        elif self.sender().text() == 'Стоп':
            self.ongoing = False
            try:
                self.table.show()
            except Exception as e:
                print(e)
        elif self.sender().text() == 'Добавить в таблицу':
            try:
                # ИЗ ПОРТА ПИХАТЬ СЮДА
                v = [len(self.vals), 0]
                self.vals.append(v)
                item1 = QTableWidgetItem(str(v[0]))
                item2 = QTableWidgetItem(str(v[1]))
                self.table.table.setItem(0, 0, item1)
                self.table.table.setItem(0, 1, item2)
            except Exception as e:
                print(e)

    def show_parent(self):
        self.parent.parent.show()
        self.parent.close()


class pokazTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('pokaz.ui', self)
        self.parent = parent


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
