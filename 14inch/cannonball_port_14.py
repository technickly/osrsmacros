#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

# _00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
# _10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
# _20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
# _30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
# _40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
# _50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
# _60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

_00 = 1230, 280; _01 = 1275, 280; _02 = 1320, 280; _03 = 1365, 280
_10 = 1230, 315; _11 = 1275, 315; _12 = 1320, 315; _13 = 1365, 315
_20 = 1230, 350; _21 = 1275, 350; _22 = 1320, 350; _23 = 1365, 350
_30 = 1230, 385; _31 = 1275, 385; _32 = 1320, 385; _33 = 1365, 385
_40 = 1230, 420; _41 = 1275, 420; _42 = 1320, 420; _43 = 1365, 420
_50 = 1230, 455; _51 = 1275, 455; _52 = 1320, 455; _53 = 1365, 455
_60 = 1230, 490; _61 = 1275, 490; _62 = 1320, 490; _63 = 1365, 490


RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]

deposit_gold = RR[1]

#ZOOM 40, 800x600 N UP

click_bank = [ 1027 , 585 ]
furnace = [1046,110]

bank_0 = [ 750 , 150 ]
# bank_1 = [ 1066 , 163 ]
run = True
if run == True:
    sleeper = 7
else:
    sleeper = 13
def smith():
    #start at furnace
    if random.randint(0,10) == 3:
        print('pause')
        time.sleep(2 + random.random())
    pg.moveTo(click_bank[0]+random.randint(-1,1),click_bank[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(sleeper+random.random()/10)

    # pg.moveTo(deposit_gold[0]+random.randint(-1,1),deposit_gold[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(1.2+random.random()/10)

    pg.moveTo(bank_0[0]+random.randint(-2,2),bank_0[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.65+random.random()/10)

    # pg.moveTo(bank_1[0]+random.randint(-2,2),bank_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(.5+random.random()/10)
    #
    pg.press('esc')

    pg.moveTo(furnace[0]+random.randint(-2,2),furnace[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(sleeper+random.random()/10)


    # pg.moveTo(bracelet[0]+random.randint(-2,2),bracelet[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    pg.press('space')

    time.sleep(77+random.random()/10)

for i in tqdm(range(invs)):
    t1 = time.time()
    # for k in range(9):
    smith()
    # if i % 3 == 0:
    #     move_through_inv(RR[1:],shuffle=True,reverse=True,click=True)
    # else:
    #     chance = random.randint(0,1)
    #     if chance == 0:
    #         move_through_inv(RR[1:],shuffle=False,reverse=False,click=True)
    #     else:
    #         move_through_inv(RR[1:],shuffle=False,reverse=True,click=True)
    # print(i,time.time()-t1, pg.position())
