#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys
import os
invs = int(round(int(sys.argv[1])/15))
print(invs)

#ZOOM 900, 800x600 E UP


_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]


spell = [ 1593 , 442 ]

seaweeed = [ 1020 , 160 ]
sand = [ 1066 , 162 ]
me = [ 1291 , 369 ]

# flax =[ 1015 , 157 ]
deposit = RR[4]
bank = pg.position()
time.sleep(2)
os.system('say move to me')
time.sleep(2)
me = pg.position()
def cast():
    if random.randint(0,10) == 5:
        time.sleep(random.randint(3,4))

    pg.moveTo(bank[0]+random.randint(-2,2),bank[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.9+(random.random()/10))
    pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.8+random.random()/2)
    # print('k')
    pg.moveTo(seaweeed[0]+random.randint(-2,2),seaweeed[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(random.random()/10)
    pg.click()
    time.sleep(random.random()/10)
    pg.click()
    pg.moveTo(sand[0]+random.randint(-2,2),sand[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.8+(random.random()/2))
    pg.press('esc')
    time.sleep(.65)
    # for i in range(5):

    pg.moveTo(spell[0]+random.randint(-2,2),spell[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(3+(random.random()/2))

    if random.randint(0,10) == 5:
        time.sleep(3)



def pickup():
    pg.moveTo(bank[0]+random.randint(-2,2),bank[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.9+(random.random()/10))
    pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.8+random.random()/2)
    time.sleep(.8+(random.random()/2))
    pg.press('esc')
    pg.moveTo(me[0]+random.randint(-2,2),me[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    for k in range(random.randint(10,15)):
        pg.click()
        time.sleep(.65+random.random()/2)
        if random.randint(0,10) == 5:
            time.sleep(random.randint(0,1))




for i in tqdm(range(invs)):
    t1 = time.time()
    for j in range(random.randint(4,6)):
        cast()
    pickup()
    # pg.moveTo(run_bank[0]+random.randint(-1,1),run_bank[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(10.+(random.random()))
    # # time.
    # pg.moveTo(deposit[0]+random.randint(-1,1),deposit[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(.5+random.random()/2)
    # pg.press('esc')
    # time.sleep(.65)
    # pg.moveTo(run_tree[0]+random.randint(-1,1),run_tree[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(10+random.random())
    #
    #
    #
    #
    #
    #
    #

    print(i,time.time()-t1, pg.position())
