import warnings
warnings.filterwarnings("ignore")
import random
import pyautogui as pg
import time
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import sys
# ick()

#zoomed out, face south, equipemnt shown, verz start


bank = [ 1273 , 90 ]

deposit = [ 1368 , 473 ]

verztele = [ 1593 , 388 ]

mushroom = [ 1120 , 615 ]

prayer_tele = [ 1550 , 387 ]
bloom  = [ 1536 , 428 ]
m1 = [ 1288 , 356 ]
m2 = [ 1321 , 354 ]
m3 = [ 1310 , 391 ]
m4 = [ 1274 , 368 ]


import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import sys
def find_and_click_template(template_path, threshold=0.3, scale_factor=2):
    """
    Find a template image on screen and click it.

    Args:
        template_path: Path to the template image (bounding box image)
        threshold: Matching confidence threshold (0-1)
        scale_factor: Retina display scale factor (usually 2 for Retina)
    """

    # Capture the screen
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Load the template image
    template = cv2.imread(template_path)
    if template is None:
        print(f"Error: Could not load template image from {template_path}")
        return False

    # Convert to grayscale for better matching
    screenshot_gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Get template dimensions
    h, w = template_gray.shape

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Find the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print(f"Best match confidence: {max_val:.3f}")

    if max_val >= threshold:
        # Get the center of the matched region
        top_left = max_loc
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2

        # Adjust for Retina display scaling
        click_x = center_x / scale_factor
        click_y = center_y / scale_factor

        print(f"Match found at: ({top_left[0]}, {top_left[1]})")
        print(f"Clicking at: ({click_x:.0f}, {click_y:.0f})")

        # Move cursor and click
        pyautogui.moveTo(click_x, click_y, duration=0.5)
        pyautogui.click()

        return True
    else:
        print(f"No match found above threshold {threshold}")
        return False

# if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python script.py <template_image_path> [threshold] [scale_factor]")
    #     print("Example: python script.py button.png 0.8 2")
    #     sys.exit(1)
    #


def recharge_pray():
    template_path = 'images/altar.png'
    threshold = .6
    scale_factor = 2
    pg.moveTo(prayer_tele[0],prayer_tele[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*6) + random.random()/5)

    success = find_and_click_template(template_path, threshold, scale_factor)
    time.sleep(random.randint(6,7))

def return_to_middle():
    template_path = 'images/return_loc.png'
    threshold = .6
    scale_factor = 2
    # pg.moveTo(prayer_tele[0],prayer_tele[1],.25,pg.easeInQuad)
    # pg.click()
    time.sleep((.6*3) + random.random()/5)

    success = find_and_click_template(template_path, threshold, scale_factor)
    time.sleep(random.randint(6,7))

def bloom_shrooms():
    pg.moveTo(bloom[0],bloom[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*4) + random.random()/5)

def pick_shrooms():
    pg.moveTo(m1[0],m1[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*3) + random.random()/3)
    pg.moveTo(m2[0],m2[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*3) + random.random()/3)
    pg.moveTo(m3[0],m3[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*3) + random.random())

    pg.moveTo(m4[0],m4[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((.6*3) + random.random()/3)

def tele_verz():
    pg.moveTo(verztele[0],verztele[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((3) + random.random()/3)


def go_to_bank():
    pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((8) + random.random()/3)
    pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((2) + random.random()/3)
    pg.press('esc')
    time.sleep(1.9)


def go_to_shrooms():
    pg.moveTo(mushroom[0],mushroom[1],.25,pg.easeInQuad)
    pg.click()
    time.sleep((20) + random.random()/3)
    # pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
    # pg.click()
    # time.sleep((2) + random.random()/3)

# mushroom = [ 1120 , 615 ]

for i in range(10):
    recharge_pray()
    for j in range(2):
        tele_verz()
        go_to_bank()
        tele_verz()
        go_to_shrooms()
        bloom_shrooms()
        bloom_shrooms()
        pick_shrooms()
        return_to_middle()
        bloom_shrooms()
        bloom_shrooms()
        pick_shrooms()
        return_to_middle()
        bloom_shrooms()
        bloom_shrooms()
        pick_shrooms()
        return_to_middle()

#start at bank
# def buy_coal():
#     pg.moveTo(ordan[0],ordan[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(7.5 + random.random()/3)
#
#     pg.moveTo(coal[0],coal[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
#
#     pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(7.5 + random.random()/3)
#
#     pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
# def buy_iron():
#     pg.moveTo(ordan[0],ordan[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(5.5 + random.random()/3)
#
#     pg.moveTo(iron[0],iron[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
#
#     pg.moveTo(bank[0],bank[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(5.5 + random.random()/3)
#
#     pg.moveTo(deposit[0],deposit[1],.25,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2 + random.random()/3)
#     pg.press('esc')
#     time.sleep(.8 + random.random()/3)
#
# for j in range(100):
#     for i in range(2):
#         buy_iron()
#         buy_coal()
#
#         if random.randint(0,15) == 3:
#             time.sleep(3)
#             print('sleep 3')
#     if random.randint(0,15) == 3:
#         time.sleep(random.randint(8,13))
#         print('sleep 15')
#
#     pg.hotkey('command','right')
#     time.sleep(7 + random.random()/2)
