import warnings
warnings.filterwarnings("ignore")
import random
import pyautogui as pg
import time
time.sleep(1.5)
pg.click()
#50 zoom limit north out

saw = [ 1315 , 349 ]
run_to = [ 1104 , 187 ]
#7 secs
bank = [ 1545 , 545 ]

logs = [ 1039 , 153 ]

deposit = [ 1573 , 344 ]

# deposit = [ 1578 , 353 ]

#start at bank
def make_plank():
    pg.moveTo(run_to[0],run_to[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(11.5 + random.random()/3)

    pg.moveTo(saw[0],saw[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)
    pg.press('4')
    time.sleep(1.5 + random.random()/3)

    pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(12 + random.random()/2)

    pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)

    pg.moveTo(logs[0],logs[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)

    pg.press('esc')
    time.sleep(1.5 + random.random()/3)
for j in range(100):
    make_plank()
    if random.randint(0,15) == 3:
        time.sleep(3)
        print('sleep 3')
    if random.randint(0,15) == 3:
        time.sleep(random.randint(8,13))
        print('sleep 15')

    # pg.hotkey('command','right')
    # time.sleep(7 + random.random()/2)
