import warnings
warnings.filterwarnings("ignore")
import random
import pyautogui as pg
import time
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import sys
# ick()

#zoomed out, north start at anvil


# bank = [ 1273 , 90 ]

bank_bar = [ 1018 , 157 ]
anvil = [ 1177 , 434 ]
run_bank = [ 1417 , 288 ]

# verztele = [ 1593 , 388 ]
#
# mushroom = [ 1120 , 615 ]
#
# prayer_tele = [ 1550 , 387 ]
# bloom  = [ 1536 , 428 ]
# m1 = [ 1288 , 356 ]
# m2 = [ 1321 , 354 ]
# m3 = [ 1310 , 391 ]
# m4 = [ 1274 , 368 ]
#

# import cv2
# import numpy as np
import pyautogui
# from PIL import ImageGrab
import sys

def smith():
    pg.moveTo(run_bank[0],run_bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(7,8) + random.random()/3)
    pg.moveTo(bank_bar[0],bank_bar[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*3) + random.random()/3)
    pg.press('esc')
    time.sleep(1 + random.random())
    pg.moveTo(anvil[0],anvil[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(7,8) + random.random())
    pg.press('space')
    time.sleep(random.randint(58,62) + random.random())
    pg.click()
    # time.sleep((.6*3) + random.random()/3)


for i in range(15):
    smith()
    if i % 3 == 0:
        time.sleep(random.randint(0,5))

#start at bank
# def buy_coal():
#     pg.moveTo(ordan[0],ordan[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(7.5 + random.random()/3)
#
#     pg.moveTo(coal[0],coal[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
#
#     pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(7.5 + random.random()/3)
#
#     pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
# def buy_iron():
#     pg.moveTo(ordan[0],ordan[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(5.5 + random.random()/3)
#
#     pg.moveTo(iron[0],iron[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
#
#     pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(5.5 + random.random()/3)
#
#     pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
#
# for j in range(100):
#     for i in range(2):
#         buy_iron()
#         buy_coal()
#
#         if random.randint(0,15) == 3:
#             time.sleep(3)
#             print('sleep 3')
#     if random.randint(0,15) == 3:
#         time.sleep(random.randint(8,13))
#         print('sleep 15')
#
#     pg.hotkey('command','right')
#     time.sleep(7 + random.random()/2)
