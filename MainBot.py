import ImageGrab
import os
import time
import win32api
import win32con
import ImageOps
from numpy import *


"""
All coordinates assume a screen resolution of 1920 x 1080, explorer 
tool bar is not enabled, browser and pycharm are side by side
    play area
    x_pad = 24 - 1
    y_pad = 337 - 1
    X2 = 791 - 23 = 
    Y2 = 910 - 337 = 478
   
"""

# Global Constants
x_pad = 23      # 23 at half screen

y_pad = 315     # 315 is ideel at half screen


class Cord:
    f_shrimp = (42, 395)
    f_rice = (109, 395)
    f_nori = (42, 462)
    f_roe = (109, 462)
    f_salmon = (42, 532)
    f_unagi = (109, 532)

# ---------------------------

    phone = (693, 430)

    menu_toppings = (636, 328)

    t_shrimp = (583, 264)   #
    t_nori = (589, 328)     #
    t_roe = (712, 328)      #
    t_salmon = (592, 397)   #
    t_unagi = (685, 259)    #
    t_exit = (706, 399)     #

    menu_rice = (639, 356)  #
    buy_rice = (649, 338)   #
    rice_delivery_norm = (595, 356)

    delivery_norm = (595, 356)  #

    # Express: 683, 350


def clear_tables():
    mousePos((108, 247))
    doubleLeftClick()
    time.sleep(.05)
    mousePos((228, 247))
    doubleLeftClick()
    time.sleep(.05)
    mousePos((348, 247))
    doubleLeftClick()
    time.sleep(.05)
    mousePos((468, 247))
    doubleLeftClick()
    time.sleep(.05)
    mousePos((588, 247))
    doubleLeftClick()
    time.sleep(.05)
    mousePos((708, 247))
    doubleLeftClick()
    time.sleep(.1)


def foldMat():
    mousePos((233, 461))
    doubleLeftClick()
    doubleLeftClick()
    time.sleep(.05)


def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        doubleLeftClick()
        time.sleep(.1)
        foldMat()

        time.sleep(1.5)

    elif food == 'onigiri':
        print('Making onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        doubleLeftClick()
        time.sleep(.1)
        foldMat()

        time.sleep(1.5)

    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        doubleLeftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        doubleLeftClick()
        time.sleep(.1)
        foldMat()

        time.sleep(1.5)


def buyFood(food):

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        doubleLeftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        doubleLeftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (230, 254, 255):
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            doubleLeftClick()
            mousePos((580, 349))
            foodOnHand['rice'] += 10
            time.sleep(.1)
            doubleLeftClick()
            time.sleep(2.5)
        else:
            print('rice is NOT available')
            mousePos(Cord.t_exit)
            doubleLeftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        doubleLeftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        doubleLeftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (277, 255, 255):
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            doubleLeftClick()

            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            print("adding 10 nori, nori = ")
            print(foodOnHand['nori'])
            foodOnHand['nori']
            time.sleep(.1)
            doubleLeftClick()
            time.sleep(2.5)
        else:
            print('nori is NOT available')
            mousePos(Cord.t_exit)
            doubleLeftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        doubleLeftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        doubleLeftClick()
        s = screenGrab()
        print("test")
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (247, 247, 247):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            doubleLeftClick()

            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            print("adding 10 roe, roe = ")
            print(foodOnHand['roe'])
            time.sleep(.1)
            doubleLeftClick()
            time.sleep(2.5)
        else:
            print('roe is NOT available')
            mousePos(Cord.t_exit)

            doubleLeftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'shrimp':
        mousePos(Cord.phone)
        time.sleep(.1)
        doubleLeftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.5)
        doubleLeftClick()
        doubleLeftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_shrimp) != (109, 123, 127):
            print('Shrimp is available')
            mousePos(Cord.t_shrimp)
            time.sleep(.1)
            doubleLeftClick()
            doubleLeftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['shrimp'] += 5
            time.sleep(.1)
            doubleLeftClick()
            time.sleep(2.5)
        else:
            print('Shrimp is NOT available')
            mousePos(Cord.t_exit)
            doubleLeftClick()
            doubleLeftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'salmon':
        mousePos(Cord.phone)
        time.sleep(.1)
        doubleLeftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.5)
        doubleLeftClick()
        doubleLeftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_salmon) != (255, 255, 255):
            print('Salmon is available')
            mousePos(Cord.t_salmon)
            time.sleep(.1)
            doubleLeftClick()
            doubleLeftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['salmon'] += 5
            time.sleep(.1)
            doubleLeftClick()
            doubleLeftClick()
            time.sleep(2.5)
        else:
            print('Salmon is NOT available')
            mousePos(Cord.t_exit)
            doubleLeftClick()
            doubleLeftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'unagi':
        mousePos(Cord.phone)
        time.sleep(.1)
        doubleLeftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.5)
        doubleLeftClick()
        doubleLeftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_unagi) != (255, 255, 255):
            print('Unagi is available')
            mousePos(Cord.t_unagi)
            time.sleep(.1)
            doubleLeftClick()
            doubleLeftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['unagi'] += 5
            time.sleep(.1)
            doubleLeftClick()
            doubleLeftClick()
            time.sleep(2.5)
        else:
            print('Unagi is NOT available')
            mousePos(Cord.t_exit)
            doubleLeftClick()
            doubleLeftClick()
            time.sleep(1)
            buyFood(food)


foodOnHand = {'shrimp': 5,
              'rice': 10,
              'nori': 10,
              'roe': 10,
              'salmon': 5,
              'unagi': 5}


def checkFood():
    for i, j in foodOnHand.items():
        if i == 'rice' or i == 'nori' or i == 'roe' or i == 'unagi' or i == 'shrimp' or i == 'salmon':
            if j <= 2:
                print('food is low and needs replenishing')
                buyFood(i)


def get_seat_one():
    box = (x_pad + 29, y_pad + 72, x_pad + 103,  y_pad + 89)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    # im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def get_seat_two():
    box = (x_pad + 151 + 1, y_pad + 74, x_pad + 226, y_pad + 90)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    # im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
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


class Blank:
    seat_1 = 8005
    seat_2 = 9334
    seat_3 = 12313
    seat_4 = 12337
    seat_5 = 9993
    seat_6 = 9541


def check_bubs():
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print('t1 sushi not found!\n sushiType = %i' % s1)

    else:
        print('Table 1 unoccupied')

    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print('t2 sushi not found!\n sushiType = %i' % s2)

    else:
        print('Table 2 unoccupied')

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print('t3 sushi not found!\n sushiType = %i' % s3)

    else:
        print('Table 3 unoccupied')

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print('t4 sushi not found!\n sushiType = %i' % s4)

    else:
        print('Table 4 unoccupied')

    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('table 5 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print('t5 sushi not found!\n sushiType = %i' % s5)

    else:
        print('Table 5 unoccupied')

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('table 6 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print('t6 sushi not found!\n sushiType = %i' % s6)

    else:
        print('Table 6 unoccupied')

    # clear_tables()



'''
    Recipes: 
    
    Onigiri: 
        2 rice, 1 nori 
        
    Caliroll: 
        1 rice, 1 nori, 1 roe
        
    Gunkan: 
        1 rice, 1 nori, 2 roe

    With color
        Shrimp: (218, 246, 255)
        Unagi:  (255, 255, 255)
        Nori:   (66, 103, 178)
        Roe:    (212, 212, 212)
        Salmon  (255, 255, 255)
    Without
        Rice:   (110, 131, 212)
        Shrimp: (109, 123, 127)
        Unagi:  (255, 255, 255)
        Nori:   (66, 103, 178)
        Roe:    (212, 212, 212)
        Salmon: (255, 255, 255)

        
'''


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_coord():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


def doubleLeftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -2, 0)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print("Click")


def screenGrab():

    box = (x_pad + 1, y_pad + 1, x_pad + 769, y_pad + 574)
    im = ImageGrab.grab()
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def startGame():
    # start
    mousePos((374, 240))
    # have to double click to enter window
    doubleLeftClick()
    doubleLeftClick()
    # continue
    mousePos((370, 460))
    doubleLeftClick()
    # skip
    mousePos((690, 535))
    doubleLeftClick()
    # final continue
    mousePos((373, 443))
    doubleLeftClick()


sushiTypes = {
    # common issues involve the change in size with the window
    10002:   'gunkan',       # seat one
    12511:  'onigiri',      # seat one
    16702:  'caliroll',     # seat one

    16132: 'gunkan',         # seat two
    12631: 'onigiri',       # seat two
    13975: 'caliroll',      # seat two

    5993: 'gunkan',         # seat three gunkin
    13029: 'onigiri',       # seat three onigiri
    14168: 'caliroll',      # seat three caliroll

    6024: 'gunkan',         # seat four gunkan
    12208: 'onigiri',       # seat four onigiri
    13699: 'caliroll',      # seat four caliroll *

    5789: 'gunkan',         # seat five gunkan
    14046: 'onigiri',       # seat five onigiri
    13590: 'caliroll',      # seat five caliroll

    5546: 'gunkan',         # seat six gunkan
    9894: 'onigiri',        # seat six onigiri
    11946: 'caliroll'        # seat six caliroll

}


def main():
    startGame()
    time.sleep(3)
    while True:
        check_bubs()
        time.sleep(.1)


if __name__ == '__main__':
    main()


"""
   startGame()
    time.sleep(3)
    time.sleep(3)
    time.sleep(3)
    time.sleep(3)
    
    i = 0
    while i <= 3:
        check_bubs()
        i += 1 
"""



