import time 
import pyautogui 
import random 
from datetime import datetime 


def saver() :
	screenWidth, screenHeight = pyautogui.size() 
	#화면 전체 크기를 출력(화면 해상도) 
	print('{}, {}'.format(screenWidth, screenHeight)) 
	cnt = 0 

	while True : 
		ran_width = random.randint(1, screenWidth) 
		ran_height = random.randint(1, screenHeight) 
		#마우스를 2초동안 ran_width, ran_height 위치로 옮김 
		pyautogui.moveTo(ran_width, ran_height, 2) 
		#키보드로 2초동안 'test' 글자를 입력 
		pyautogui.typewrite("test", interval=2) 
		cnt += 1 
		print('{} 번째 동작중 {} {}'.format(cnt, ran_width, ran_height)) 
		time.sleep(60) 
		print(datetime.now())

if __name__ =="__main__" : 
	saver()
