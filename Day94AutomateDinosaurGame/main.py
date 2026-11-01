#
from numpy import *
import pyautogui
import time
from PIL import ImageGrab, ImageOps


class cordinates():
    replay_b = (686, 398)
    dino = (449, 398)


def playit():
    pyautogui.click(cordinates.replay_b)


def movedino():
    pyautogui.keyDown('Space')
    time.sleep(0.5)
    print('Jump')
    pyautogui.keyUp('Space')


playit()
time.sleep(1)
movedino()

while True:
    x, y, a, b = 465, 391, 54, 37
    box = (x, y, x + a, y + b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum()
    print(value)

    if value != 2245:
        pyautogui.press('space')
