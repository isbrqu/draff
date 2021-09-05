import os
import winscreen
import keyboard
from time import sleep
from PIL import ImageChops
# import pyautogui as mouse

# amazon
# DIM = (70, 50, 1470, 850)

# premiun users
DIM = (0, 164, 900, 1435)
second = 5
i = 0
nro = 13
diff = True

name = input('nombre de carpeta:')
os.mkdir(f'C:\\Users\\isbrq\\Downloads\\{name}')
os.chdir(f'C:\\Users\\isbrq\\Downloads\\{name}')

winscreen.select('firefox')
winscreen.rotateRight()
keyboard.send('f11')

print('screenshots!')
while diff is not None:
	i += 1
	img1 = winscreen.capture(i, name)
	keyboard.send('right')
	i += 1
	img2 = winscreen.capture(i, name)
	keyboard.send('right')

	diff = ImageChops.difference(img1, img2).getbbox()

winscreen.rotateUp()
keyboard.send('f11')

os.remove(f'{i}-{name}.png')
# os.remove(f'{i-1}-{name}.png')
