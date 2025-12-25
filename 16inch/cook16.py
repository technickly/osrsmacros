#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = round(int(sys.argv[1])/28)

#ZOOM 900, 800x600 E UP


_00 = 1240, 315; _01 = 1285, 315; _02 = 1330, 315; _03 = 1375, 315
_10 = 1240, 350; _11 = 1285, 350; _12 = 1330, 350; _13 = 1375, 350
_20 = 1240, 385; _21 = 1285, 385; _22 = 1330, 385; _23 = 1375, 385
_30 = 1240, 420; _31 = 1285, 420; _32 = 1330, 420; _33 = 1375, 420
_40 = 1240, 455; _41 = 1285, 455; _42 = 1330, 455; _43 = 1375, 455
_50 = 1240, 490; _51 = 1285, 490; _52 = 1330, 490; _53 = 1375, 490
_60 = 1240, 525; _61 = 1285, 525; _62 = 1330, 525; _63 = 1375, 525

RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]


#myth
stove = [ 1395 , 369 ]
#burthope
stove = [ 1296 , 250 ]

# fire = stove
raw = [ 1017 , 158 ]

deposit = [ 1375 , 477 ]

bank = [ 1167 , 380 ]

def cook():
    if random.randint(0,10) == 30:
        print('pause')
        time.sleep(5 + random.random())
        pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(26.+(random.random()*3.5))
        pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(26.+(random.random()*3.5))
    else:
        pg.moveTo(bank[0]+random.randint(-2,2),bank[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(.9+(random.random()/10))
        pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(.8+(random.random()/2))
        pg.moveTo(raw[0]+random.randint(-2,2),raw[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(1.8+(random.random()/2))
        pg.press('esc')
        time.sleep(.65)
        pg.moveTo(stove[0]+random.randint(-2,2),stove[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(.8+random.random()/2)
        pg.press('space')
        time.sleep(65+random.random())




for i in tqdm(range(invs)):
    t1 = time.time()
    cook()
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
