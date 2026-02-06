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
def buy_coal():
    pg.moveTo(ordan[0],ordan[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(7.5 + random.random()/3)

    pg.moveTo(coal[0],coal[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)
    pg.press('esc')
    time.sleep(.8 + random.random()/3)

    pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(7.5 + random.random()/3)

    pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)
    pg.press('esc')
    time.sleep(.8 + random.random()/3)
def buy_iron():
    pg.moveTo(ordan[0],ordan[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(5.5 + random.random()/3)

    pg.moveTo(iron[0],iron[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)
    pg.press('esc')
    time.sleep(.8 + random.random()/3)

    pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(5.5 + random.random()/3)

    pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)
    pg.press('esc')
    time.sleep(.8 + random.random()/3)

for j in range(100):
    for i in range(2):
        buy_iron()
        buy_coal()

        if random.randint(0,15) == 3:
            time.sleep(3)
            print('sleep 3')
    if random.randint(0,15) == 3:
        time.sleep(random.randint(8,13))
        print('sleep 15')

    pg.hotkey('command','right')
    time.sleep(7 + random.random()/2)
