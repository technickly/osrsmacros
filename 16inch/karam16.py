import time
import random
import os
import sys
import pyautogui
from tqdm import tqdm
#zoom 60

invs_ = int(sys.argv[1])
#180 = 3 hours!
    #browfa
tele = [ 1192 , 395 ]


karam_fish = [ 1286 , 282 ]
karam_to_ring = [ 1312 , 459 ]
ring_to_bank = [ 1600 , 510 ]
bank_to_ring = [ 929 , 210 ]


_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR = [  _02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33]

karam_inv = [ 1523 , 372 ]
DJR = [ 1577 , 419 ]
DKP = [ 1536 , 381 ]



def fish():
    pyautogui.moveTo(karam_fish[0]+random.randint(-1,1),karam_fish[1]+random.randint(-1,1),.5+random.random()/2.5,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(random.randint(100,115))

def run_bank():
    #From fish to Ring
    pyautogui.moveTo(karam_to_ring[0],karam_to_ring[1],.6+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(5+random.random()/5)

    pyautogui.moveTo(DJR[0],DJR[1],.8+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(4+random.random()/5)


    pyautogui.moveTo(tele[0],tele[1],.9+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(5.5+random.randint(-1,1))

    pyautogui.moveTo(ring_to_bank[0],ring_to_bank[1],.3+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(17+random.random()*2)

    r1 = RR[random.randint(2,12)]
    pyautogui.moveTo(r1[0],r1[1],.5+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(2.2+random.random()/10)

    pyautogui.press('esc')
    time.sleep(2.5+random.random()/10)
    if random.randint(0,15) == 5 and i != 0:
        print('Breaking 3-12')
        time.sleep(random.randint(3,12))


def run_back():
    pyautogui.moveTo(bank_to_ring[0],bank_to_ring[1],.7+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(random.randint(16,18)+random.random())

    pyautogui.moveTo(DKP[0],DKP[1],.5+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(5+random.randint(-1,1))
    if random.randint(0,15) == 5 and i != 0:
        print('Breaking 3-12')
        time.sleep(random.randint(3,15))

    pyautogui.moveTo(tele[0],tele[1],.9+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(5.5+random.randint(-1,1))
for i in tqdm(range(invs_)):
    tt = time.time()
    if random.randint(0,7) == 5 and i != 0:
        print('Breaking 3-12')
        time.sleep(random.randint(3,12))

    fish()
    run_bank()
    run_back()

    print((time.time()-tt)/60,i)
