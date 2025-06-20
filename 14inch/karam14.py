import time
import random
import os
import sys
import pyautogui
from tqdm import tqdm


invs_ = int(sys.argv[1])
#180 = 3 hours!
    #browfa
tele = [ 920 , 375 ]

karam_fish = [ 1015 , 268 ]
karam_to_ring = [ 1032 , 429 ]
ring_to_bank = [ 1293 , 472 ]
_00 = 1240, 315; _01 = 1285, 315; _02 = 1330, 315; _03 = 1375, 315
_10 = 1240, 350; _11 = 1285, 350; _12 = 1330, 350; _13 = 1375, 350
_20 = 1240, 385; _21 = 1285, 385; _22 = 1330, 385; _23 = 1375, 385
_30 = 1240, 420; _31 = 1285, 420; _32 = 1330, 420; _33 = 1375, 420
_40 = 1240, 455; _41 = 1285, 455; _42 = 1330, 455; _43 = 1375, 455
_50 = 1240, 490; _51 = 1285, 490; _52 = 1330, 490; _53 = 1375, 490
_60 = 1240, 525; _61 = 1285, 525; _62 = 1330, 525; _63 = 1375, 525
RR = [  _02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33]

karam_inv = [ 1523 , 372 ]
bank_to_ring = [ 692 , 207 ]
DJR = [ 1248 , 348 ]
DKP = [ 1244 , 394 ]


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
