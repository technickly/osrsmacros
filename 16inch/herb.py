import time
import pyautogui as pg
import sys
import random
import math
from tqdm import tqdm

#WT NORTH ZOOMED IN
#SET BANK_LOC
#CLIENT 765x550
#DEFINE UNF OR FIN


# type_ = 'fin'
# num_herbs = 700
num_herbs = int(sys.argv[2])
# type_ = 'unf'
type_ = str(sys.argv[1])

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



num_ = math.floor(num_herbs/14)
if type_ == 'unf':
    waiter = 9
elif type_ == 'fin':
    waiter = 18

# bank_loc = [ 1412 , 355 ]
#CW FACE N ())
# bank_loc = [ 1407 , 380 ]
bank_loc = pg.position()

bank_1 = [ 1020 , 160 ]
bank_2 = [ 1066 , 162 ]
inv_14 = RR[13]
inv_15 = RR[14]
#bank_deposit = [ 1387 , 455 ]
bank_deposit = [ 1368 , 475 ]

noise = 1
move_noise = .1

for i in tqdm(range(num_)):

# for i in range(num_):
    noise = random.randint(-2,2)
    move_noise = random.randint(1,2)/10
#open bank
    pg.moveTo(bank_loc[0]+noise*3,bank_loc[1]+noise*3,.5+move_noise,pg.easeInQuad)
    time.sleep(.5)
    pg.click()
#deposit all
    pg.moveTo(bank_deposit[0]+noise,bank_deposit[1]+noise,.5+move_noise,pg.easeInQuad)
    time.sleep(.5)
    pg.click()
#withdraw 14 from spot 1
    pg.moveTo(bank_1[0],bank_1[1],.5+move_noise,pg.easeInQuad)
    time.sleep(.5)
    pg.click()
#withdraw 14 from spot 2
    pg.moveTo(bank_2[0]+noise,bank_2[1]+noise,.5+move_noise,pg.easeInQuad)
    time.sleep(.5)
    pg.click()
#escape bank tab
    time.sleep(1)
    pg.press('esc')
#click inv 14
    pg.moveTo(inv_14[0]+noise,inv_14[1]+noise,.5+move_noise,pg.easeInQuad)
    time.sleep(.5)
    pg.click()
#click inv 14
    pg.moveTo(inv_15[0]+noise,inv_15[1]+noise,.5+move_noise,pg.easeInQuad)
    time.sleep(.5)
    pg.click()
#press space to make
    time.sleep(1.5)
    pg.press('space')
# Done
    time.sleep(waiter)
    # pg.moveTo(bank_loc[0]+noise,bank_loc[1]+noise,.5,pg.easeInQuad)




# print(pyautogui.position())
