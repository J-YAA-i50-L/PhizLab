from collections import deque
import serial
import sys
from serial.tools import list_ports
import matplotlib.pyplot as plot  # $ pip install matplotlib
import matplotlib.animation as animation

npoints = 30
x = deque([0], maxlen=npoints)
y = deque([0], maxlen=npoints)
fig, ax = plot.subplots()
[line] = ax.step(x, y)


def update(dy):
    x.append(x[-1] + 1)  # update data
    y.append(y[-1] + dy)

    line.set_xdata(x)  # update plot data
    line.set_ydata(y)

    ax.relim()  # update axes limits
    ax.autoscale_view(True, True, True)
    return line, ax


def data_gen():
    while True:
        data = ser.readline()
        # Протестить вживую, неизвестен формат данных
        yield float(data.strip())


try:
    spis = [str(elem) for elem in list_ports.comports()]
    for elem in spis:
        if 'последовательный порт' not in elem.lower():
            if sys.platform.startswith('win'):
                port = elem[:4]
            else:
                raise EnvironmentError('Unsupported platform')
    ser = serial.Serial(port, 9600)
    ani = animation.FuncAnimation(fig, update, data_gen)
    plot.show()
except Exception as e:
    print(e)
