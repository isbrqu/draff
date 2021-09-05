import os
import win32gui
import win32api
import win32con
from time import sleep
from pyscreenshot import grab as screenshot

ORIENTATION = {'left': 270, 'down': 180, 'right': 90, 'up': 0}
MY_SCREEN_NUMBER = 0

def loadwindowslist(hwnd, topwindows):
	topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))

def showwindowslist():
	topwindows = []
	win32gui.EnumWindows(loadwindowslist, topwindows)
	for hwin in topwindows:
		sappname = str(hwin[1])
		nhwnd = hwin[0]
		print(str(nhwnd) + ": " + sappname)

def select(swinname, bshow = True, bbreak = True):
	topwindows = []
	win32gui.EnumWindows(loadwindowslist, topwindows)
	for hwin in topwindows:
		sappname = str(hwin[1])
		if swinname in sappname.lower():
			nhwnd = hwin[0]
			if (bshow):
				win32gui.ShowWindow(nhwnd, 5)
				win32gui.SetForegroundWindow(nhwnd)
			if (bbreak):
				break

def rotate(direction):
	degree = ORIENTATION[direction]
	device = win32api.EnumDisplayDevices(None, MY_SCREEN_NUMBER)
	dm = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
	new_orientation = int(degree / 90)
	current_orientation = dm.DisplayOrientation
	if (new_orientation + current_orientation) % 2 == 1:
		dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
	dm.DisplayOrientation = new_orientation
	return win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)

def rotateUp():
	return rotate('up')

def rotateRight():
	return rotate('right')

def capture(i, name, delay=2, dim=(0, 164, 900, 1435)):
	name = f'{i}-{name}.png'
	fail = True
	while fail:
		sleep(delay)
		img = screenshot(bbox=dim)
		img.save(name)
		bbytes = os.path.getsize(name)
		fail = bbytes < 15000
		print(f'screenshot: {name}\t{bbytes} bytes')
	return img
