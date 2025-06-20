import warnings
warnings.filterwarnings("ignore")
import random
import pyautogui as pg
import time
time.sleep(1.5)
pg.click()
#50 zoom limit north out

a0,a1 = [ 1232 , 317 ]
b0,b1 = [ 1291 , 304 ]
c0,c1 =  [ 1238 , 367 ]
d0,d1 =   [ 1226 , 422 ]
e0,e1 =   [ 1287 , 449 ]
f0,f1 = [ 1320 , 402 ]
EAST_ = [ 1549 , 365 ]
g0,g1 = [ 1325 , 369 ]
h0,h1 = [ 1297 , 290 ]

for i in range(5):
    pg.moveTo(a0,a1,.25,pg.easeInQuad);pg.click()
    time.sleep(8)
    print('5')

    pg.moveTo(b0,b1,.25,pg.easeInQuad);pg.click()
    time.sleep(6)

    pg.moveTo(c0,c1,.25,pg.easeInQuad);pg.click()
    time.sleep(6)

    pg.moveTo(d0,d1,.25,pg.easeInQuad);pg.click()
    time.sleep(5)

    pg.moveTo(e0,e1,.25,pg.easeInQuad);pg.click()
    time.sleep(6)

    pg.moveTo(f0,f1,.25,pg.easeInQuad);pg.click()
    time.sleep(8)


    for k in range(random.randint(2,4)):
        pg.moveTo(EAST_[0],EAST_[1],.25,pg.easeInQuad)
        pg.click()
        time.sleep(.2+random.random()/10)

    time.sleep(8)
    pg.moveTo(g0,g1,.25,pg.easeInQuad);pg.click()
    time.sleep(8)

    pg.moveTo(h0,h1,.25,pg.easeInQuad);pg.click()
    time.sleep(2)
