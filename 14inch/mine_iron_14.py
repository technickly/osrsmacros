#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 900, 800x600 N UP


_00 = 1240, 315; _01 = 1285, 315; _02 = 1330, 315; _03 = 1375, 315
_10 = 1240, 350; _11 = 1285, 350; _12 = 1330, 350; _13 = 1375, 350
_20 = 1240, 385; _21 = 1285, 385; _22 = 1330, 385; _23 = 1375, 385
_30 = 1240, 420; _31 = 1285, 420; _32 = 1330, 420; _33 = 1375, 420
_40 = 1240, 455; _41 = 1285, 455; _42 = 1330, 455; _43 = 1375, 455
_50 = 1240, 490; _51 = 1285, 490; _52 = 1330, 490; _53 = 1375, 490
_60 = 1240, 525; _61 = 1285, 525; _62 = 1330, 525; _63 = 1375, 525

RR = [ _01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]

# [~/osrsmacros/14inch]$ python3 get_position.py
# [~/osrsmacros/14inch]$ python3 get_position.py
iron_spot_1 = [ 883 , 347 ]
iron_spot_2 = [ 1024 , 226 ]
iron_spot_3 = [ 1141 , 354 ]


def mine():
    if random.randint(0,20) == 8:
        print('sleep 4')
        time.sleep(5.4 + random.random())

    if random.randint(0,50) == 7:
        print('switchup')
        pg.moveTo(iron_spot_2[0]+random.randint(-3,2),iron_spot_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(1.9+ random.random()/10)

        time.sleep(1.9+random.random()/10)
        pg.moveTo(iron_spot_1[0]+random.randint(-2,3),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(1.9+random.random()/10)
        pg.moveTo(iron_spot_3[0]+random.randint(-2,2),iron_spot_3[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        # pg.click()
        # time.sleep(3+random.random()/10)
        # time.sleep(2+random.random())
    else:
        # print('left->middle->right')
        # print('middle->right->left')
        pg.moveTo(iron_spot_1[0]+random.randint(-3,2),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(1.9+ random.random()/10)

        pg.moveTo(iron_spot_2[0]+random.randint(-2,3),iron_spot_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(1.9+random.random()/10)

        pg.moveTo(iron_spot_3[0]+random.randint(-2,2),iron_spot_3[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(1.9+random.random()/10)



def move_through_inv(RR,shuffle,reverse,click):
    tween_delay = random.random()/7.5
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
            pg.click()
        time.sleep(move_delay)

for i in tqdm(range(invs)):
    t1 = time.time()
    if random.randint(0,100) == 5:
        print('sleep 205')
        time.sleep(205 + random.random())

    if i == 35:
        print('sleep 3 mins, break')
        time.sleep(150)
    for k in range(random.randint(8,9)):
        mine()
    if i % 3 == 0:
        move_through_inv(RR[0:],shuffle=True,reverse=True,click=True)
    else:
        chance = random.randint(0,1)
        if chance == 0:
            move_through_inv(RR[0:],shuffle=False,reverse=False,click=True)
        else:
            move_through_inv(RR[0:],shuffle=False,reverse=True,click=True)
    print(i,time.time()-t1, pg.position())
