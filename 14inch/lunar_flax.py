#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 900, 800x600 E UP

_00 = 1240, 315; _01 = 1285, 315; _02 = 1330, 315; _03 = 1375, 315
_10 = 1240, 350; _11 = 1285, 350; _12 = 1330, 350; _13 = 1375, 350
_20 = 1240, 385; _21 = 1285, 385; _22 = 1330, 385; _23 = 1375, 385
_30 = 1240, 420; _31 = 1285, 420; _32 = 1330, 420; _33 = 1375, 420
_40 = 1240, 455; _41 = 1285, 455; _42 = 1330, 455; _43 = 1375, 455
_50 = 1240, 490; _51 = 1285, 490; _52 = 1330, 490; _53 = 1375, 490
_60 = 1240, 525; _61 = 1285, 525; _62 = 1330, 525; _63 = 1375, 525

# _00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
# _10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
# _20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
# _30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
# _40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
# _50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
# _60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]


spell = [ 1306 , 403 ]
flax = [ 745 , 147 ]
deposit = RR[2]
bank = pg.position()
def cast():
    pg.moveTo(bank[0]+random.randint(-2,2),bank[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.9+(random.random()/10))
    pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.8+random.random()/2)
    print('k')
    pg.moveTo(flax[0]+random.randint(-2,2),flax[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.8+(random.random()/2))
    pg.press('esc')
    time.sleep(.65)
    for i in range(5):

        pg.moveTo(spell[0]+random.randint(-2,2),spell[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(3+random.random()/2)




for i in tqdm(range(invs)):
    t1 = time.time()
    cast()
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
