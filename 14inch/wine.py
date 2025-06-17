#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys


deposit = [ 1092 , 443 ] #[ 1100 , 438 ]
climb_up = [ 1137 , 422 ]
climb_up2 = [ 1072 , 332 ]
go_wine = [ 1014 , 333 ]
wine = [ 1025 , 345 ]
climb_down = [ 1045 , 356 ]
climb_down2 = [ 980 , 354 ]
chest =[ 907 , 280 ]
#start upstairs, north 0 zoom
invs = int(sys.argv[1])

def pick(k):
    pg.moveTo(wine[0],wine[1])

    pg.click()
    time.sleep(random.random()/5)
    # pg.click()
    time.sleep(random.randint(1,2)+ random.random()/10)
    if random.randint(0,10) == 0:
        print('sleep')
        # pg.hotkey('command','left')
        time.sleep(random.randint(7,12))
        # pg.hotkey('command','left')
    # if random.randint(3,5) == 4:
        # pg.hotkey('command','right')
        # time.sleep(5)
        # pg.hotkey('command','right')
        # time.sleep(5)

    else:
        pg.hotkey('command','right')


    time.sleep(10)
    # pg.hotkey('f1')

def up():
    #start at bank
    pg.press('esc'); time.sleep(random.random()/3)
    time.sleep(.5+ random.random()/10)
    pg.moveTo(climb_up[0],climb_up[1],.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(8.5+ random.random()/10)
    pg.moveTo(climb_up2[0],climb_up2[1],.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(3.5+ random.random()/10)
    pg.moveTo(go_wine[0],go_wine[1],.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(4.5+ random.random()/10)

def down():
    #start at bank
    # pg.press('esc'); time.sleep(random.random()/3)
    pg.click()
    time.sleep(3.5+ random.random()/10)
    pg.moveTo(climb_down[0]+random.randint(-1,1),climb_down[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(6.5+ random.random()/10)
    pg.moveTo(climb_down2[0]+random.randint(-1,1),climb_down2[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(6.5+ random.random()/10)
    pg.moveTo(chest[0]+random.randint(-1,1),chest[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(9.5+ random.random()/10)

    pg.press('0'); time.sleep(.6+random.random()/2)
    pg.press('8'); time.sleep(.6+random.random()/2)
    pg.press('0'); time.sleep(.6+random.random()/2)
    pg.press('8'); time.sleep(.6+random.random()/2)
    time.sleep(1)
    pg.moveTo(deposit[0]+random.randint(-2,3),deposit[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(2.5+ random.random()/10)

    # pg.press('f1')
    # time.sleep(random.)
    # pg.press('f1')


for i in tqdm(range(invs)):
    # up()
    pg.moveTo(wine[0]+random.randint(-1,1),wine[1]+random.randint(-1,1))

    for k in range(random.randint(22,27)):
        pick(k)
    print('inv done')
    down()
    up()

    # if i % 3 == 0:
    #     move_through_inv(RR[1:],shuffle=True,reverse=True,click=True)
    # else:
    #     chance = random.randint(0,1)
    #     if chance == 0:
    #         move_through_inv(RR[1:],shuffle=False,reverse=False,click=True)
    #     else:
    #         move_through_inv(RR[1:],shuffle=False,reverse=True,click=True)
    # print(i,time.time()-t1, pg.position())
