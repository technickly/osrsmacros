import time
import pyautogui as pg
import sys
import random
import os
from tqdm import tqdm

t1 = time.time()
laps = int(sys.argv[1])
#camera 900
# camera 200
def run_lap():
    # laps_ = 9
    ladder_1 = [ 1116 , 367 ]
    rope_1 = [ 1048 , 415 ]
    # rope_2 = [ 1014 , 356 ]
    ladder_2 = [ 1015 , 357 ]
    edge_1 = [ 1003 , 355 ]
    rope_3 = [ 1003 , 334 ]
    zipeline = [ 1046 , 324 ]
    move_noise = .1


    run_loop = time.time()
    n1 = random.randint(-1,1)
    n2 = random.randint(-1,1)
    move_noise = random.randint(1,2)/10

    pg.moveTo(ladder_1[0]+n2,ladder_1[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(5+random.random()/10.)
    if random.randint(0,5) == 1:
        time.sleep(1+random.random())
    pg.moveTo(rope_1[0]+n2,rope_1[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(22.5+random.random()/10.)
    if random.randint(0,20) == 1:
        time.sleep(1+random.random())

    pg.moveTo(ladder_2[0]+n1,ladder_2[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(3.5+random.random()/10.)
    if random.randint(0,30) == 1:
        time.sleep(1+random.random())


    pg.moveTo(edge_1[0]+n2,edge_1[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(8+random.random()/10.)
    if random.randint(0,25) == 1:
        time.sleep(1+random.random())

    pg.moveTo(rope_3[0]+n1,rope_3[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(22.5+random.random()/10.)
    if random.randint(0,35) == 1:
        time.sleep(1+random.random())


    pg.moveTo(zipeline[0]+n2,zipeline[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(12+random.random()/10.)
    if random.randint(0,25) == 1:
        time.sleep(1+random.random())


    print('Run Loop: ',((time.time()-run_loop)))


for j in tqdm(range(laps)):
    loop = time.time()
    run_lap()
    print('Iter Loop: ',((time.time()-loop)/60))
    if random.randint(0,5) == 4:
        time.sleep(random.randint(3,5))
        print('sleep')
print('Finished in: ',(time.time()-t1)/60)
os.system('say finished')
