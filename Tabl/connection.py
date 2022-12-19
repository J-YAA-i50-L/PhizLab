import serial
import sys
from serial.tools import list_ports


def do(ongoing, self):
    liist = [str(elem) for elem in list_ports.comports()]
    for elem in liist:
        if 'последовательный порт' not in elem.lower():
            if sys.platform.startswith('win'):
                port = elem[:4]
            else:
                raise EnvironmentError('Unsupported platform')
    while ongoing:
        try:
            ser = serial.Serial(port, 9600)
            val = int(ser.readline().strip())
            self.val.display(val)
        except:
            pass