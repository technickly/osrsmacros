#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(int(sys.argv[1])/27)
time.sleep(1)
click_bank = pg.position()
# click_bank = [ 1287 , 445 ]

#ZOOM 900, 800x600 N UP


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

# move_to_sand = [ 1537 , 278 ]
# click_bank = [ 1287 , 445 ]

bank_1 = [ 746 , 150 ]
# bank_2 = [ 1065 , 159 ]
# furnace = [ 941 , 421 ]
# s_1 = [ 1298 , 345 ]
# s_2 = [ 1320 , 370 ]
# deposit = [ 986 , 485 ]

def blow():
    # for i in range(10):
    #start at furnace
    if random.randint(0,10) == 5:
        print('pause')
        time.sleep(3 + random.random())
    if random.randint(0,20) == 5:
        print('long pause')
        time.sleep(12 + random.random())
    if random.randint(0,50) == 5:
        print('longest pause')
        time.sleep(65 + random.random())

    pg.moveTo(click_bank[0]+random.randint(-2,2),click_bank[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(1.5+random.random()/10)
    deposit_glass_item = RR[random.randint(2,3)]

    pg.moveTo(deposit_glass_item[0]+random.randint(-2,2),deposit_glass_item[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(1.2+random.random()/10)

    pg.moveTo(bank_1[0]+random.randint(-2,2),bank_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(1.2+random.random()/10)

    # pg.moveTo(bank_2[0]+random.randint(-2,2),bank_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(.65+random.random()/10)

    pg.press('esc')
    time.sleep(.8)
    pg.moveTo(_00[0]+random.randint(-2,2),_00[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(1.2+random.random()/10)

    pg.moveTo(_01[0]+random.randint(-2,2),_01[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.8+random.random()/10)

    pg.press('space')
    time.sleep(49+random.random()/10)
    #
    # for j in range(10):
    #     pg.moveTo(s_1[0]+random.randint(-2,2),s_1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    #     pg.click()
    #     time.sleep(3.6+random.random()/10)
    #     pg.moveTo(s_2[0]+random.randint(-2,2),s_2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    #     pg.click()
    #     time.sleep(3.6+random.random()/10)
    # pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(5+random.random()/10)


#
# def move_through_inv(RR,shuffle,reverse,click):
#     tween_delay = random.random()/7.5
#     # IF WANT TO SHUFFLE
#     if shuffle == True:
#         coin_flip = random.randint(0,1)
#         if coin_flip == 0:
#             random.shuffle(RR)
#     # IF WANT TO REVERSE
#     if reverse == True:
#         coin_flip = random.randint(0,1)
#         if coin_flip == 0:
#             RR.reverse()
#
#     for pos in RR:
#         move_delay = random.random()/2
#         pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
#         if click == True:
#             pg.click()
#         time.sleep(move_delay)

for i in tqdm(range(invs)):
    t1 = time.time()
    for k in range(9):
        blow()
    # if i % 3 == 0:
    #     move_through_inv(RR[1:],shuffle=True,reverse=True,click=True)
    # else:
    #     chance = random.randint(0,1)
    #     if chance == 0:
    #         move_through_inv(RR[1:],shuffle=False,reverse=False,click=True)
    #     else:
    #         move_through_inv(RR[1:],shuffle=False,reverse=True,click=True)
    # print(i,time.time()-t1, pg.position())
