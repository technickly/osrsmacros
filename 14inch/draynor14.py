#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys
laps = int(sys.argv[1])

#16 Inch
#Camera 40
_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR16 = [  _00,_01,_02,_03,_10,_11,_12,_13,_20,_21,_22,_23,
          _30,_31,_32,_33,_40,_41,_42,_43,_50,_51,_52,_53,
          _60,_61,_62,_63 ]

#14 Inch
_00 = 1230, 280; _01 = 1275, 280; _02 = 1320, 280; _03 = 1365, 280
_10 = 1230, 315; _11 = 1275, 315; _12 = 1320, 315; _13 = 1365, 315
_20 = 1230, 350; _21 = 1275, 350; _22 = 1320, 350; _23 = 1365, 350
_30 = 1230, 385; _31 = 1275, 385; _32 = 1320, 385; _33 = 1365, 385
_40 = 1230, 420; _41 = 1275, 420; _42 = 1320, 420; _43 = 1365, 420
_50 = 1230, 455; _51 = 1275, 455; _52 = 1320, 455; _53 = 1365, 455
_60 = 1230, 490; _61 = 1275, 490; _62 = 1320, 490; _63 = 1365, 490

RR14 = [  _00,_01,_02,_03,_10,_11,_12,_13,_20,_21,_22,_23,
          _30,_31,_32,_33,_40,_41,_42,_43,_50,_51,_52,_53,
          _60,_61,_62,_63 ]

import time
import pyautogui as pg
import sys
import random
import os
from tqdm import tqdm

t1 = time.time()

def run_laps(laps_):
    # laps_ = 9
    wall_1 = [ 1023 , 151 ]
    rope_1 = [ 982 , 364 ]
    rope_2 = [ 1044 , 344 ]
    wall_2 = [ 995 , 364 ]
    wall_3 = [ 1023 , 398 ]
    gap_1 = [ 1096 , 340 ]
    finish = [ 1091 , 289 ]
    noise = 0
    move_noise = .1

    for i in tqdm(range(laps_)):
        run_loop = time.time()
        noise = random.randint(-1,1)
        noise = 0
        move_noise = random.randint(1,2)/10

    #FROM TILE MARKER TO WALL
        pg.moveTo(wall_1[0]+noise,wall_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(9+random.random()/10.)

    #JUMP FIRST GAP
        pg.moveTo(rope_1[0]+noise,rope_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(10+random.random()/10.)


    #CROSS ROPE
        pg.moveTo(rope_2[0]+noise,rope_2[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(10+random.random()/10.)


    #JUMP SECOND GAP
        pg.moveTo(wall_2[0]+noise,wall_2[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(8+random.random()/10.)

    #JUMP THIRD GAP
        pg.moveTo(wall_3[0]+noise,wall_3[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(7+random.random()/10.)

    #JUMP EDGE
        pg.moveTo(gap_1[0]+noise,gap_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(8+random.random()/10.)

    #RUN TO START TO FINISH
        pg.moveTo(finish[0]+noise,finish[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(10+random.random()/10.)

        print('Run Loop: ',((time.time()-run_loop)))


for j in range(laps):
    loop = time.time()
    # laps_ = random.randint(0,3)
    print("Laps: ",laps)
    run_laps(laps)
    # print("Picking up marks")
    # pickup_marks()
    # print('Iter Loop: ',((time.time()-loop)/60))
print('Finished in: ',(time.time()-t1)/60)
os.system('say finished')
