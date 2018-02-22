import ImageGrab
import os
import time
import win32api
import win32con
import ImageOps
from numpy import *

x_pad = 24

y_pad = 315


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 758, y_pad + 574)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def get_seat_one():
    box = (x_pad + 29, y_pad + 72, x_pad + 103,  y_pad + 89)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_seat_two():
    box = (x_pad + 151 + 1, y_pad + 74, x_pad + 226, y_pad + 90)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_seat_three():
    box = (x_pad + 1 + 273, y_pad + 74, x_pad + 346, y_pad + 90)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    # im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_seat_four():
    box = (x_pad + 1 + 394, y_pad + 74, x_pad + 467, y_pad + 90)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    # im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_seat_five():
    box = (x_pad + 1 + 515, y_pad + 74, x_pad + 588, y_pad + 90)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    # im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_seat_six():
    box = (x_pad + 1 + 636, y_pad + 74, x_pad + 710, y_pad + 90)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    # im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()


sushiTypes = {
    # common issues involve the change in size with the window
    8391:   'gunkan',       # seat one
    11956:  'onigiri',      # seat one
    15761:  'caliroll',     # seat one

    7012: 'gunkan',         # seat two
    13136: 'onigiri',       # seat two
    14480: 'caliroll',      # seat two

    5993: 'gunkan',         # seat three gunkin
    13029: 'onigiri',       # seat three onigiri
    14168: 'caliroll',      # seat three caliroll

    6024: 'gunkan',         # seat four gunkan
    12208: 'onigiri',       # seat four onigiri
    13699: 'caliroll',              # seat four caliroll

    5789: 'gunkan',         # seat five gunkan
    14046: 'onigiri',       # seat five onigiri
    13590: 'caliroll',      # seat five caliroll

    5546: 'gunkan',         # seat six gunkan
    9894: 'onigiri',        # seat six onigiri
    11946: 'caliroll'        # seat six caliroll

}


def test():
    win32api.SetCursorPos(shrimp)


shrimp = (610, 621)


def getCords():
    x,y = win32api.GetCursorPos()
    print(x,y)


def main():
    get_seat_four()

    get_seat_six()




if __name__ == '__main__':
    main()