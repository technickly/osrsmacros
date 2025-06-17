import pyautogui as pg
import time
import sys
import random
import os
start = time.time()

_00 = 1240, 315; _01 = 1285, 315; _02 = 1330, 315; _03 = 1375, 315
_10 = 1240, 350; _11 = 1285, 350; _12 = 1330, 350; _13 = 1375, 350
_20 = 1240, 385; _21 = 1285, 385; _22 = 1330, 385; _23 = 1375, 385
_30 = 1240, 420; _31 = 1285, 420; _32 = 1330, 420; _33 = 1375, 420
_40 = 1240, 455; _41 = 1285, 455; _42 = 1330, 455; _43 = 1375, 455
_50 = 1240, 490; _51 = 1285, 490; _52 = 1330, 490; _53 = 1375, 490
_60 = 1240, 525; _61 = 1285, 525; _62 = 1330, 525; _63 = 1375, 525

RR = [  _00,_01,_02,_03,
		_10,_11,_12,_13,
		_20,_21,_22,_23,
		_30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]

cake = [ 1243 , 316 ]
quick_pray = [ 1225 , 154 ]

super_pot = [ _01,_02,_03,
			  _10,_11,_12,_13 ]
# absorptions = [ _10,_11,_12,_13 ,
# 			_20,_21,_22,_23]
cake = _00
quick_pray = [ 1225 , 154 ]

super_pot = [ _01,_02,_03,
			  _10,_11,_12,_13 ]
absorptions = [_13,_12,_20,_21,_22,_23,
			_30,_31,_32,_33,
	        _40,_41,_42,_43,
	        _50,_51,_52,_53,
	        _60,_61,_62,_63 ]

def flick_pray():
	print('Flicked pray')
	pg.moveTo(quick_pray[0],quick_pray[1],.2+random.random()/2,pg.easeInQuad)
	pg.click()
	time.sleep(1 + random.random()/5)
	pg.click()
	time.sleep(1 + random.random()/5)

	if random.randint(0,2) == 1:
		print('cake eat')
		pg.moveTo(cake[0],cake[1],.2+random.random()/2,pg.easeInQuad)
		pg.click()
		time.sleep(1 + random.random()/5)
		pg.click()
		time.sleep(1 + random.random()/5)

def absorption():
	if random.randint(0,3) == 1:
		# print('o')
		pg.moveTo(cake[0],cake[1],.2+random.random()/2,pg.easeInQuad)
		pg.click()
		time.sleep(1 + random.random()/5)
		pg.click()
		time.sleep(1 + random.random()/5)

	r_num = random.randint(0,len(absorptions)-1)
	if random.randint(0,10) == 1:
		print('Triple Absorption')
		for j in range(3):

			random_spot = absorptions[r_num]
			pot_x,pot_y = random_spot[0]+random.randint(-2,2), random_spot[1]+random.randint(-2,2)
			# print(pot_x)
			pg.moveTo(pot_x,pot_y,.3+random.random()/2,pg.easeInQuad)
			pg.click()
			time.sleep(1.4 + random.random()/3)
	if random.randint(0,10) == 3:
		print('Double Absorption Same Spot')
		random_spot = absorptions[r_num]

		for j in range(2):
			pot_x,pot_y = random_spot[0]+random.randint(-2,2), random_spot[1]+random.randint(-2,2)
			# print(pot_x)

			pg.moveTo(pot_x,pot_y,.5+random.random()/2,pg.easeInQuad)
			pg.click()
			time.sleep(3 + random.random()/3)
	# if random.randint(0,3) == 3:
	# 	time.sleep(20)

	else:
		for j in range(1):
		# print('Double Absorption')
			random_spot = absorptions[r_num]
			pot_x,pot_y = random_spot[0]+random.randint(-2,2), random_spot[1]+random.randint(-2,2)
			pg.moveTo(pot_x,pot_y,.9+random.random()/2,pg.easeInQuad)
			pg.click()
			time.sleep(1 + random.random()/3)

	# print('Drinking Singleabsorption, ',r_num)

# def pray_flick():
# 	pg.moveTo(quick_pray[0],quick_pray[1],.9+random.random()/2,pg.easeInQuad)
# 	pg.click()
# 	time.sleep(.5+random.uniform(.2,.4))



# quick_pray

#
# def click_in_place():
#     for i in range(5):
#         time.sleep(1.2)
#         pg.click()
#
# kko
#
# def move_through_inv(RR):
#     for pos in RR:
#         move_delay = random.random()/5
#         tween_delay = random.random()/2
#         pg.moveTo(pos[0],pos[1],tween_delay,pg.easeInQuad)
#         time.sleep(move_delay)
#
#

# def absorption():
# 	n1 = random.randint(-1,1)
# 	n2 = random.randint(-1,1)
# 	r_num = random.randint(0,len(RR)-1)
# 	random_spot = RR[r_num]
# 	print('Drinking absorption, ',r_num)
# 	pot_x,pot_y = random_spot[0]+n1, random_spot[1]+n2
# 	pg.moveTo(pot_x,pot_y)
# 	pg.click()
# 	click_delay = random.random()/10
# 	# print(click_delay)
# 	time.sleep(1.2 + click_delay)
# 	pg.click()
# 	time.sleep(1.2 + click_delay)
#


def nmz(mins_):
	for i in range(mins_):
		if i % 2 == 0:
			time.sleep(.4)
			absorption()
		flick_pray()
		# # # n1 = random.randint(-2,2)
		# # # n2 = random.randint(-2,2)
		# # # pray_x,pray_y = 1553+n1, 168+n2
		# # # crnt_x,crnt_y = pg.position()[0],pg.position()[1]
		# # #pg.moveTo(rock_x,rock_y))
		# # pg.moveTo(pray_x,pray_y)
		# # pg.click()
		# # click_delay = random.random()/5
		# # print(click_delay)
		# time.sleep(click_delay)
		# time.sleep(.6)
		# pg.click()
		# pg.moveTo(crnt_x,crnt_y)
		random_secs = random.randint(30,45)
		time.sleep(random_secs)
		print(i,round((time.time()-start)/60),'minutes')


start = time.time()
# for i in range(5):
mins_ = int(sys.argv[1])
nmz(mins_)
	# absorption()
os.system('say done running')
