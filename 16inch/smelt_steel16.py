import warnings
warnings.filterwarnings("ignore")
import random
import pyautogui as pg
import time
time.sleep(1.5)
pg.click()
#50 zoom limit north out

belt = [ 1235 , 238 ]
bank = [ 1363 , 489 ]

#7 secs
dispenser = [ 1275 , 411 ]

#6
bank2 = [ 1390 , 462 ]

coal = [ 1306 , 194 ]
coal_bank = [ 1020 , 163 ]
iron_bank = [ 1066 , 165 ]
iron = [ 1117 , 193 ]

deposit = [ 1577 , 354 ]
deposit_all = [ 1372 , 478 ]
#start at bank with open
def smith():
    pg.moveTo(coal_bank[0],coal_bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1 + random.random()/3)
    pg.press('esc')
    time.sleep(.25)


    pg.moveTo(belt[0],belt[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(13.5 + random.random()/3)

    pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(13.5 + random.random()/3)

    pg.moveTo(iron_bank[0],iron_bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(1.2 + random.random()/3)
    pg.press('esc')
    time.sleep(.3)

    pg.moveTo(belt[0],belt[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(16.5 + random.random()/3)


    pg.moveTo(dispenser[0],dispenser[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(8 + random.random()/3)
    pg.press('space')
    time.sleep(1)

    pg.moveTo(bank2[0],bank2[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep(7 + random.random()/3)
    # pg.press('space')
    pg.moveTo(deposit_all[0],deposit_all[1],.25,pg.easeInQuad)
    time.sleep(.2)
    pg.click()
    pg.click()
    time.sleep(3 + random.random()/3)

for j in range(1000000):
    smith()
    if random.randint(0,15) == 3:
        time.sleep(5)
        print('sleep 5')

    # pg.hotkey('command','right')
    # time.sleep(7 + random.random()/2)
