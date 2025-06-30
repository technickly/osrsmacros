#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 100, 800x600 E UP


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


w1 = [ 1156 , 324 ]
# w1 = pg.position()
campfire = [ 1296 , 368 ]
# w2 = [ 1233 , 363 ]

tind = RR[0]
knife = RR[0]
log = RR[1]
log2 = RR[2]
    # pg.moveTo(log[0]+random.randint(-1,1),log[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)

move_to_fire = [ 1345 , 366 ]
# run_tree = [ 1378 , 136 ]
def cut():
    if random.randint(0,3) == 8:
        print('pause')
        time.sleep(5 + random.random())
    else:
        # iters_ = random.randint(4,5)
        for j in range(1):
            # print(iters_)
            pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
            pg.click()
            time.sleep(33.+(random.random()*3.5))
            # pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
            # pg.click()
            # time.sleep(13.+(random.random()*3.5))
            # time.sleep()
# def start_fire():
#     pg.moveTo(tind[0]+random.randint(-1,1),tind[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(.65+(random.random()/2))
#     pg.moveTo(log[0]+random.randint(-1,1),log[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     # pg.click()
#     time.sleep(.6+random.random()/2)
#     pg.moveTo(move_to_fire[0]+random.randint(-1,1),move_to_fire[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     pg.keyDown('shift')
#     pg.click()
#     pg.keyUp('shift')
#     time.sleep(1.3+(random.random()/2))

def fire():
    pg.moveTo(campfire[0]+random.randint(2,4),campfire[1]+random.randint(2,4),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.65+(random.random()/2))
    # pg.moveTo(log[0]+random.randint(2,4),log[1]+random.randint(2,4),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    time.sleep(.6+random.random()/2)
    pg.press('space')
    time.sleep(20+random.random())

def fletch():
    print ('fletch')
    pg.moveTo(knife[0]+random.randint(2,4),knife[1]+random.randint(2,4),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.65+(random.random()/2))
    pg.moveTo(log[0]+random.randint(2,4),log[1]+random.randint(2,4),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.6+random.random()/2)
    pg.press('space')

    time.sleep(random.randint(10,15)+(random.random()))
    print('done')

for i in tqdm(range(invs)):
    t1 = time.time()
    cut()
    fletch()
    # fire()

    #






    print(i,time.time()-t1, pg.position())
