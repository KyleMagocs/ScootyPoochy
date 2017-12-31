import serial
from serial.tools import list_ports

class ColorLib:
    try:
        teensy = None
        for port in list_ports.comports():
            if 'Teensy' in port.description:
                teensy = serial.Serial(port.device)
                break
    except:
        teensy = None

    col1 = b'w'
    col2 = b'w'
    try:
        teensy.write(col1 + col2)
    except:
        pass

    @classmethod
    def set_colors(cls, color1=None, color2=None):
        try:
            if color1 is not None:
                cls.col1 = color1
            if color2 is not None:
                cls.col2 = color2
            cls.teensy.write(cls.col1 + cls.col2)
        except:
            pass