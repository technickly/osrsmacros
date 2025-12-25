import warnings
warnings.filterwarnings("ignore")

import pyautogui as pg
import random
import time
import sys
from tqdm import tqdm

# num_ = int(sys.argv[1])*2
t1 = time.time()
x,y = pg.position()
_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570


#pg.moveTo(1661 , 378
#)
# x,y = [ 1657 , 885 ]
RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]



def move_through_inv(RR,shuffle,reverse,click):

    tween_delay = random.random()/(random.randint(2,4));print('oi')
    # IF WANT TO SHUFFLE
    if shuffle == True:
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            random.shuffle(RR)
    # IF WANT TO REVERSE
    if reverse == True:
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            RR.reverse()
    for pos in RR:
        move_delay = random.random()/2
        pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
        if click == True:
            if random.randint(0,2) == 1:
                pg.click()
            else:
                pg.click()
                time.sleep(random.random()/5)
                pg.click()
        time.sleep(move_delay)

def mine_once():
    # noise = random.randint(-1,1)
    tween_delay = random.random()/(random.randint(2,4));print('oi')

    pg.moveTo(x , y,tween_delay,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(15,20) + random.random()/5)
    # if random.randint(0,15) == 1:
        # pg.press('f1')
        # pg.click()
        # time.sleep(11.4 + random.random()/5)
        # pg.press('f1')
        # pg.click()
        # time.sleep(1.4 + random.random()/5)

def wc():
    tween_delay = random.random()/(random.randint(2,4));print('oi')

    noise = random.randint(-1,1)
    for j in range(random.randint(6,7)):
        pg.moveTo(x+noise , y+noise,tween_delay,pg.easeInQuad)

        pg.click()
        time.sleep(random.randint(15,20) + random.random()/5)
    if random.randint(0,15) == 1:
        # pg.press('f1')
        # pg.click()
        time.sleep(random.randint(8,15)+ random.random()/5)
        # pg.press('f1')
        # pg.click()
        # time.sleep(1.4 + random.random()/5)
for i in tqdm(range(300000)):

    wc()
    move_through_inv(RR,shuffle=False,reverse=True,click=True)
    if random.randint(0,12) == 1:
        # pg.press('f1')
        # pg.click()
        time.sleep(random.randint(8,15)+ random.random()/5)

    # mine_once()

#
