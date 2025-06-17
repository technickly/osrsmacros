import pyautogui
import cv2
import numpy as np
import time
import mss
import random
from tqdm import tqdm
import sys
iters_ = int(sys.argv[1])
essence = [ 744 , 146 ]
p1,p2,p3 = [ 1236 , 320 ],[ 1280 , 316 ],[ 1323 , 316]
flax = [ 899 , 69 ]
altar1 = [ 688 , 185 ]
craft_altar = [ 1007 , 349 ]
def find_pixels(template_path, confidence=0.6):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Full screen
        screenshot = np.array(sct.grab(monitor))[:, :, :3]  # RGB image

    screenshot_bgr = screenshot
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    h, w, _ = template.shape

    result = cv2.matchTemplate(screenshot_bgr, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        # Get match center in retina coordinates
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2

        # Convert retina to macOS logical coordinates
        center_x //= 2
        center_y //= 2

        return (center_x, center_y)
    else:

        return None


for i in tqdm(range(iters_)):
    #Lunar Tele

    bank = find_pixels('lunar_bank.png')
    if bank != None:
        #Run to bank
        pyautogui.moveTo(bank[0]+random.randint(-1,1), bank[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
        pyautogui.click()
        # if random.randint(0,5) == 3:
        #     time.sleep(3.1+(random.random()/10))
        #     pyautogui.click()

        time.sleep(6+ random.random()/2)
        if i % 7 == 0 and i != 0:
            time.sleep(90)

    #withdraw essence
    pyautogui.moveTo(essence[0]+random.randint(-1,1), essence[1]+random.randint(-1,1), duration=(.3+(random.random()/10)))
    time.sleep(1.2+(random.random()/5))
    pyautogui.click()


    #fill pouches
    pyautogui.moveTo(p1[0]+random.randint(-1,1), p1[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(.9+(random.random()/5))
    pyautogui.click()
    pyautogui.moveTo(p2[0]+random.randint(-1,1), p2[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(.9+(random.random()/5))
    pyautogui.click()
    pyautogui.moveTo(p3[0]+random.randint(-1,1), p3[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(.9+(random.random()/5))
    pyautogui.click()
    pyautogui.moveTo(essence[0]+random.randint(-1,1), essence[1]+random.randint(-1,1), duration=(.3+(random.random()/10)))
    time.sleep(.5+(random.random()/5))
    pyautogui.click()
    time.sleep(1.6)
    pyautogui.press('esc')
    #exit bank
    time.sleep(.9+random.random()/5)

    # flax = [ 1151 , 89 ]
    # altar = [ 964 , 195 ]

    pyautogui.moveTo(flax[0]+random.randint(-1,1), flax[1]+random.randint(-1,1), duration=(.3+(random.random()/10)))
    pyautogui.click()
    time.sleep(18.2+(random.random()/5))
    pyautogui.moveTo(altar1[0]+random.randint(-1,1), altar1[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(1.5+(random.random()/5))

    pyautogui.click()
    time.sleep(16.2+(random.random()/5))

    time.sleep(1.2+(random.random()/5))
    pyautogui.press('f1')

    # craft_altar = [ 1275 , 375 ]
    pyautogui.moveTo(craft_altar[0]+random.randint(-1,1), craft_altar[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(1.5+(random.random()/5))
    pyautogui.click()
    time.sleep(1.2 + random.random()/2)
    pyautogui.moveTo(p1[0]+random.randint(-1,1), p1[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(1.2+(random.random()/5))
    pyautogui.click()
    pyautogui.moveTo(p2[0]+random.randint(-1,1), p2[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(.5+(random.random()/5))
    pyautogui.click()
    pyautogui.moveTo(p3[0]+random.randint(-1,1), p3[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(.5+(random.random()/5))
    pyautogui.click()

    pyautogui.moveTo(craft_altar[0]+random.randint(-1,1), craft_altar[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    time.sleep(.5+(random.random()/5))
    pyautogui.click()
    time.sleep(.8 + random.random()/2)

    pyautogui.press('f3')
    time.sleep(.9)
    #browfa
    tele = [ 1236 , 410 ]
    # tele = [ 1236 , 412 ]
    pyautogui.moveTo(tele[0]+random.randint(-1,1), tele[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
    pyautogui.click()
    time.sleep(4.5+(random.random()/5))
