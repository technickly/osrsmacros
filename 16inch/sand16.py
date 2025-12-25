import time
import random
import os
import sys
from tqdm import tqdm
import pyautogui as pg
#CAMERA 0
#RUNELITE N ZOOMED OUT 765X550
#START AT DKP RING
# karam_fish = [1051,264]

run_to_mine = [ 1422 , 312 ]

# run_to_sand = [ 1423 , 309 ]

sand_n = [ 1297 , 355 ]

sand_e = [ 1309 , 366 ]


grinder = [ 1138 , 433 ]


invs_ = int(sys.argv[1])
# for
for i in tqdm(range(invs_)):
    # sand_e = [ 1312 , 367 ]
    pg.moveTo(run_to_mine[0]+random.randint(-1,1),run_to_mine[1]+random.randint(-1,1),.5+random.random()/2.5,pg.easeInQuad)
    pg.click()
    time.sleep(random.randint(6,7)+random.random()/2)

    for j in range(random.randint(5,6)):
        pg.moveTo(sand_e[0]+random.randint(-1,1),sand_e[1]+random.randint(-1,2),.5+random.random()/2.5,pg.easeInQuad)
        pg.click()
        time.sleep(random.randint(4,5)+random.random()/2)
        pg.moveTo(sand_n[0]+random.randint(-1,1),sand_n[1]+random.randint(-1,2),.5+random.random()/2.5,pg.easeInQuad)
        pg.click()
        time.sleep(random.randint(4,5)+random.random()/2)
    pg.moveTo(grinder[0]+random.randint(-2,2),grinder[1]+random.randint(-2,2),.5+random.random()/2.5,pg.easeInQuad)
    pg.click()

    time.sleep(random.randint(6,7)+random.random()/2)

# karam_fish = [ 1287 , 285 ]
# karam_to_ring = [ 1310 , 453 ]
# DJR = [ 1568 , 389 ]
# ring_to_bank = [ 1604 , 495 ]
# # fish_barrel = [ 1604 , 294 ]
# karam_inv = [ 1617 , 354 ]
# bank_to_ring = [ 918 , 222 ]
# DKP = [ 1552 , 425 ]
# #DJR = D-1,J-1,R-2 CHASM
# #DKP = D-1, K-2, P-0
# # d = [ 1079 , 255 ]
# # j = [ 1154 , 255 ]
# # r = [ 1323 , 258 ]
# # k = [ 1251 , 258 ]
# teleport = [ 1187 , 394 ]
#
#
# # ring_to_mid_x,ring_to_mid_y = 917, 220
# # mid_to_bank_x,mid_to_bank_y = 1014, 260
# # deposit_x, deposit_y = 1359,250
# # bank_to_mid_x,bank_to_mid_y = 1186,372
# # mid_to_ring_x,mid_to_ring_y = 1103,362
#
# # Point(x=1041, y=262)
#
# #start at fairy ring at karamja, north zoomed out fixed
# # import warnings
# # warnings.filterwarnings("ignore")
# import pyautogui
#
# #
# for i in range(30):
#     print(i)
#     #From Fairy Ring on Karajama
#     pyautogui.moveTo(karam_fish[0],karam_fish[1],.5+random.random()/2.5,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(random.randint(130,135))
#     # os.system('say done fishing')
#
#     #From fish to Ring
#     pyautogui.moveTo(karam_to_ring[0],karam_to_ring[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(4+random.random()/5)
#
#     #Set to Chasm of Fire
#     pyautogui.moveTo(DJR[0],DJR[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(3+random.random())
#     # pyautogui.moveTo(j[0],j[1],random.random()/2,pyautogui.easeInQuad)
#     # pyautogui.click()
#     # time.sleep(.69)
#     # pyautogui.moveTo(r[0],r[1],random.random()/2,pyautogui.easeInQuad)
#     # pyautogui.click()
#     # time.sleep(.65)
#     # pyautogui.click()
#     # time.sleep(.60)
#
#     pyautogui.moveTo(teleport[0],teleport[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(4.5+random.random()/5)
#
#
#
#     pyautogui.moveTo(ring_to_bank[0],ring_to_bank[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(15+random.random())
#
#     # pyautogui.moveTo(fish_barrel[0],fish_barrel[1],random.random()/2,pyautogui.easeInQuad)
#     # pyautogui.click()
#     # time.sleep(1.2+random.random()/10)
#
#     pyautogui.moveTo(karam_inv[0],karam_inv[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(1.2+random.random()/10)
#
#     print("Deposited")
#     pyautogui.press('esc')
#     time.sleep(.6+random.random()/10)
#     pyautogui.moveTo(bank_to_ring[0],bank_to_ring[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(15+random.random())
#
#     pyautogui.moveTo(DKP[0],DKP[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(4.6)
#
#     pyautogui.moveTo(teleport[0],teleport[1],random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(4+random.randint(-1,1))
#
#
# #     #Done Fishing, To Zanaris
# #     pyautogui.moveTo(fish_to_fairy_x,fish_to_fairy_y,random.random()/2,pyautogui.easeInQuad)
# #     pyautogui.click()
# #     print("At Zanaris")
# #     time.sleep(6)
# #     #At Zanaris, Move halfway to bank
# #     pyautogui.moveTo(ring_to_mid_x,ring_to_mid_y,random.random()/2,pyautogui.easeInQuad)
# #     pyautogui.click()
# #     print("Halfway To Bank")
# #     time.sleep(11)
# #     #At Zanaris halfway, move to bank
# #     pyautogui.moveTo(mid_to_bank_x,mid_to_bank_y,random.random(),pyautogui.easeInQuad)
# #     pyautogui.click()
# #     print("To the bank")
# #     time.sleep(7)
# #
# #     #At bank tab deposit karawambam
# #     pyautogui.moveTo(deposit_x,deposit_y,random.random(),pyautogui.easeInQuad)
# #     pyautogui.click()
# #     time.sleep(1.2)
# #     print("Deposited")
# #     pyautogui.press('esc')
# #
# #     #At bank, move halfway to ring
# #     pyautogui.moveTo(bank_to_mid_x,bank_to_mid_y,random.random(),pyautogui.easeInQuad)
# #     pyautogui.click()
# #     time.sleep(11)
# #
# #     #Halfway to ring, move to ring
# #     pyautogui.moveTo(mid_to_ring_x,mid_to_ring_y,random.random()/2,pyautogui.easeInQuad)
# #     pyautogui.click()
# #     time.sleep(8)
# #
#
#
#
#


#
#
# move_to_fish()
# pyautogui.click()
# time.sleep(20)
# move_fish_to_fairy()
# pyautogui.click()
