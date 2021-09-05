import os
import winscreen
import keyboard
from pyscreenshot import grab as screenshot
from time import sleep

DIM = (0, 164, 900, 1435)
nro = input('numero de captura: ')
name = input('nombre de carpeta: ')
os.chdir(f'C:\\Users\\isbrq\\Downloads\\{name}')

winscreen.select('firefox')
keyboard.send('f11')
winscreen.rotateRight()

sleep(5)
img = screenshot(bbox=DIM)
img.save(f'{nro}-{name}.png')

keyboard.send('f11')
winscreen.rotateUp()
print('successful!')
