import warnings
warnings.filterwarnings("ignore")

import pyautogui as pg
import random
import time
import sys
from tqdm import tqdm

num_ = int(sys.argv[1])*2
t1 = time.time()
# home = True
home = False
if home:
    x,y = [ 1528 , 560 ]
else :
    x,y = pg.position()
#pg.moveTo(1661 , 378
#)
# x,y = [ 1657 , 885 ]
for i in tqdm(range(num_)):
    # if random.rand
    noise = random.randint(-1,1)
    if random.randint(0,100) == 20:
        print('sleep 8')
        time.sleep(8+random.random())
    if random.randint(0,30) == 4:
        print('moved')
        pg.moveTo(x+noise , y+noise)
        time.sleep(3)
    if random.randint(0,35) == 10:
        print('sleep 5')

        time.sleep(5+random.random())
    if random.randint(0,200) == 20:
        print('long sleep')

        time.sleep(25)
    else:
        pg.moveTo(x,y)
    time.sleep(1.4 + random.random()/5)
    pg.click()
