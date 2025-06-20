import pyautogui
import cv2
import numpy as np
import time
import mss
import random
from tqdm import tqdm
import sys
iters_ = int(sys.argv[1])
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

circles = ['boxtrap.jpg','green1.jpg', 'green2.jpg','green3.jpg',
            'green4.jpg','red1.jpg','red2.jpg','red3.jpg']

for i in tqdm(range(iters_)):

    for circle in circles:
        # try:
        circle_loc = find_pixels('greyimg/' + circle)
        dead_loc = find_pixels('greyimg/' + 'boxtrap.jpg')
        if dead_loc != None:
            # print(f"Clicking Screen at {circle_loc}")
            pyautogui.moveTo(dead_loc[0]+random.randint(-1,1), dead_loc[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
            pyautogui.click()
            if random.randint(0,15) == 3:
                time.sleep(.1+(random.random()/10))
                pyautogui.click()

            time.sleep(9+ random.random()/2)

        if circle_loc != None:
            # print(f"Clicking Screen at {circle_loc}")
            pyautogui.moveTo(circle_loc[0]+random.randint(-1,1), circle_loc[1]+random.randint(-1,1), duration=(.1+(random.random()/10)))
            pyautogui.click()
            if random.randint(0,15) == 3:
                time.sleep(.1+(random.random()/10))
                pyautogui.click()

            time.sleep(9+ random.random()/2)

        # elif red_loc != None:
        #             # if green_loc != None:

        #     print(f"Clicking Red at {red_loc}")
        #     pyautogui.moveTo(red_loc[0], red_loc[1], duration=0.2)
        #     pyautogui.click()
        #     time.sleep(9)
        # except:
                # print('Nothing')
                # pass
            # time.sleep(1)

# if __name__ == "__main__":
# template_file = "greencircle.png"
# main_loop()
