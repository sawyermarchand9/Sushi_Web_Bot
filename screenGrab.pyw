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


def main():
    screenGrab()

    
if __name__ == '__main__':
    main()
