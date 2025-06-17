import warnings
warnings.filterwarnings("ignore")

import pyautogui as pg
import random
import time
import sys
from tqdm import tqdm

num_ = int(sys.argv[1])*2
t1 = time.time()
x,y = pg.position()
print('[',x,',',y,']')
# x, y = [ 1034 , 261 ]
pg.moveTo(x , y)

pg.click()
time.sleep(.3)
pg.press('f1')
pg.click()
time.sleep(.3)

#pg.moveTo(1661 , 378
#)
# x,y = [ 1657 , 885 ]
for i in tqdm(range(num_)):

    noise = random.randint(-1,1)
    if random.randint(0,15) == 5:

        pg.moveTo(x+noise , y+noise)

    time.sleep(.8 + random.random()/5)
    pg.click()
    if random.randint(0,8) == 1:
        pg.press('f1')
        pg.click()
        time.sleep(1.4 + random.random()/5)
        pg.press('f1')
        pg.click()
        time.sleep(1.4 + random.random()/5)
    pg.moveTo(x,y)
pg.press('f1')
