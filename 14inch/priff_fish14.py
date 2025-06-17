#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 900, 800x600 N UP


# _00 = 1230, 280; _01 = 1275, 280; _02 = 1320, 280; _03 = 1365, 280
# _10 = 1230, 315; _11 = 1275, 315; _12 = 1320, 315; _13 = 1365, 315
# _20 = 1230, 350; _21 = 1275, 350; _22 = 1320, 350; _23 = 1365, 350
# _30 = 1230, 385; _31 = 1275, 385; _32 = 1320, 385; _33 = 1365, 385
# _40 = 1230, 420; _41 = 1275, 420; _42 = 1320, 420; _43 = 1365, 420
# _50 = 1230, 455; _51 = 1275, 455; _52 = 1320, 455; _53 = 1365, 455
# _60 = 1230, 490; _61 = 1275, 490; _62 = 1320, 490; _63 = 1365, 490

_00 = 1240, 315; _01 = 1285, 315; _02 = 1330, 315; _03 = 1375, 315
_10 = 1240, 350; _11 = 1285, 350; _12 = 1330, 350; _13 = 1375, 350
_20 = 1240, 385; _21 = 1285, 385; _22 = 1330, 385; _23 = 1375, 385
_30 = 1240, 420; _31 = 1285, 420; _32 = 1330, 420; _33 = 1375, 420
_40 = 1240, 455; _41 = 1285, 455; _42 = 1330, 455; _43 = 1375, 455
_50 = 1240, 490; _51 = 1285, 490; _52 = 1330, 490; _53 = 1375, 490
_60 = 1240, 525; _61 = 1285, 525; _62 = 1330, 525; _63 = 1375, 525

RR = [ _02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]


fish_spot = pg.position()
# iron_spot_1 = [ 1019 , 243 ]
#
# iron_spot_2 = [ 1134 , 342 ]
# iron_spot_3 = [ 1291 , 427 ]

def fish():
    if random.randint(0,9) == 8:
        print('sleep 4')
        time.sleep(4 + random.random())
    if random.randint(0,20) == 5:
        print('sleep 15')
        time.sleep(15 + random.random())
    pg.moveTo(fish_spot[0]+random.randint(-3,5),fish_spot[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(100,115))
    #
    # if random.randint(0,12) == 7:
    #     print('middle->right->left')
    #     time.sleep(2.8+ random.random()/10)
    #     pg.moveTo(iron_spot_2[0]+random.randint(-3,2),iron_spot_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    #     pg.click()
    #     time.sleep(2.8+random.random()/10)
    #     pg.moveTo(iron_spot_1[0]+random.randint(-2,3),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    #     pg.click()
    #     # time.sleep(1.8+random.random()/10)
    #     # pg.moveTo(iron_spot_1[0]+random.randint(-2,2),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    #     # pg.click()
    #     # time.sleep(3+random.random()/10)
    #     # time.sleep(2+random.random())
    # else:
    #     # print('left->middle->right')
    #     print('normal')
    #     pg.moveTo(iron_spot_1[0]+random.randint(-1,4),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    #     pg.click()
    #     time.sleep(2.5+random.random()/10)
    #     pg.moveTo(iron_spot_2[0]+random.randint(-3,2),iron_spot_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    #     pg.click()
    #     time.sleep(2.4+random.random()/10)
    #     # pg.moveTo(iron_spot_3[0]+random.randint(-2,2),iron_spot_3[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    #     # pg.click()
    #     # time.sleep(1.8+random.random()/10)



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
        if random.randint(1,5) == 2:
            tween_delay = random.random()/7.5

        move_delay = random.random()/2
        pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
        if click == True:
            pg.click()
            if random.randint(1,10) == 8:
                time.sleep(.1+random.random()/5)
                pg.click()
        time.sleep(move_delay)

for i in tqdm(range(invs)):
    t1 = time.time()
    # for k in range(random.randint(8,10)):
    fish()
    if i % 3 == 0:
        move_through_inv(RR[0:],shuffle=True,reverse=True,click=True)
    else:
        chance = random.randint(0,1)
        if chance == 0:
            move_through_inv(RR[0:],shuffle=False,reverse=False,click=True)
        else:
            move_through_inv(RR[0:],shuffle=False,reverse=True,click=True)
    print(i,time.time()-t1, pg.position())
