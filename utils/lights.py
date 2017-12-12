import serial

class ColorLib:
    try:
        teensy = serial.Serial('COM5')
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