import usb.core
import usb.util


class Trackball:
    def __init__(self, vendor, product, id):
        self.device = list(usb.core.find(idVendor=vendor, idProduct=product, find_all=True))[id]
        self.endpoint = self.device[0][(0, 0)][0]

    def read(self):
        try:
            data = self.device.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize)

            return raw_to_x_y(data)
        except usb.core.USBError as e:
            return 0, 0  # default to not moving, I guess !


def raw_to_x_y(data_array):
    if data_array[2] == 0 and data_array[1] != 0: # right
        x_vel = data_array[1] * -1
    elif data_array[2] == 255 and data_array[1] != 0: # left
        x_vel = (255 - data_array[1])
    else:
        x_vel = 0
    if data_array[4] == 0 and data_array[3] != 0: # down
        y_vel = data_array[3] * -1
    elif data_array[4] == 255 and data_array[3] != 0: # up
        y_vel = 255 - data_array[3]
    else:
        y_vel = 0

    return x_vel, y_vel
