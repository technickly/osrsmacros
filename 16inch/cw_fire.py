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

invs_ = int(round(float(sys.argv[1])/28,1))
print('Invs = ',invs_)
#zoomed out, north start at anvil


# bank = [ 1273 , 90 ]

bank_log= [ 1018 , 157 ]
time.sleep(.5)
fire = pg.position()
print('move')
time.sleep(2.2)
bank = pg.position()
print('done locs')
inv_log = [ 1570 , 384 ]

 # = [ 1177 , 434 ]
# run_bank = [ 1417 , 288 ]

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

def burn():
    pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(1,2) + random.random()/3)
    pg.moveTo(bank_log[0],bank_log[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*3) + random.random()/3)
    pg.press('esc')
    time.sleep(1 + random.random())
    pg.moveTo(inv_log[0],inv_log[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(1,2) + random.random())
    pg.moveTo(fire[0],fire[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(1,2) + random.random())
    pg.press('space')

    time.sleep(random.randint(58,62) + random.random())
    pg.click()
    # time.sleep((.6*3) + random.random()/3)


for i in range(invs_):
    burn()
    if i % 3 == 0:
        time.sleep(random.randint(0,2))

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
