import pygame
import usb.core
import usb.util


class Trackball:
    button_one = None
    button_two = None
    button_three = None

    def __init__(self, vendor, product, id):
        self.device = (list(usb.core.find(idVendor=vendor, idProduct=product, find_all=True)))[id]
        self.endpoint = self.device[0][(0, 0)][0]

    def set_buttons(self, one, two, three):
        self.button_one = one
        self.button_two = two
        self.button_three = three

    def read(self):
        try:
            data = self.device.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize, timeout=5)
            return raw_to_x_y(data)

        except usb.core.USBError as e:
            return 0, 0  # default to not moving, I guess !

    def get_buttons(self):
        # TODO:  Replace all of this with real buttons
        #         Y'know, like arcade buttons
        rtn = list()
        keystate = pygame.key.get_pressed()

        if keystate[self.button_one]:
            rtn.append('one')
        if keystate[self.button_two]:
            rtn.append('two')
        if keystate[self.button_three]:
            rtn.append('three')

        return rtn

# https://www.orangecoat.com/how-to/read-and-decode-data-from-your-mouse-using-this-pyusb-hack
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
