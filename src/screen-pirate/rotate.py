import win32api as win32
import win32con
import sys
from time import sleep

# dmdo = {'left': win32con.DMDO_270, 'down': win32con.DMDO_180, 'right': win32con.DMDO_90, 'up': win32con.DMDO_DEFAULT}
orientation = {'left': 270, 'down': 180, 'right': 90, 'up': 0}

# def printAllScreen():
#     i = 0
#     while True:
#         try:
#             device = win32.EnumDisplayDevices(None,i);
#             print(f'[{i}] {device.DeviceString} ({device.DeviceName})');
#             i += 1;
#         except:
#             break;
#     return i

# # screen_count = printAllScreen()
# # x = int(input(f'\nEnter a display number [0-{screen_count - 1}]: '))
# x = 0
# rotation = dmdo[sys.argv[1]]

# device = win32.EnumDisplayDevices(None, x);
# print(f'Rotate device {device.DeviceString} ({device.DeviceName})');

# dm = win32.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
# # if (dm.DisplayOrientation + rotation) % 2 == 1:
# dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
# #     print('pass')
# dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
# dm.DisplayOrientation = win32con.DMDO_90
# win32.ChangeDisplaySettingsEx(device.DeviceName, dm)

# def printAllScreen():
#     i = 0
#     while True:
#         try:
#             device = win32.EnumDisplayDevices(None,i);
#             print(f"[{i}] {device.DeviceString} ({device.DeviceName})");
#             i += 1;
#         except:
#             break;
#     return i

# screen_count = printAllScreen()
# x = int(input(f"\nEnter a display number [0-{screen_count-1}]: "))


# device = win32.EnumDisplayDevices(None, x);
# print(f"Rotate device {device.DeviceString} ({device.DeviceName})")

# dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
# dm.DisplayOrientation = win32con.DMDO_90
# dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
# dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
# win32.ChangeDisplaySettingsEx(device.DeviceName,dm)

def rotate(direction):
	degree = orientation[direction]
	MY_SCREEN_NUMBER = 0
	device = win32.EnumDisplayDevices(None, MY_SCREEN_NUMBER)
	dm = win32.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
	new_orientation = int(degree / 90)
	current_orientation = dm.DisplayOrientation
	if (new_orientation + current_orientation) % 2 == 1:
		dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
	dm.DisplayOrientation = new_orientation
	return win32.ChangeDisplaySettingsEx(device.DeviceName, dm)

rotate(sys.argv[1])

# print('degree 0')
# rotateTo(0)
# sleep(2)
# print('degree 90')
# rotateTo(90)
# sleep(2)
# print('degree 180')
# rotateTo(180)
# sleep(2)
# print('degree 270')
# rotateTo(270)
# sleep(2)
# print('degree 0')
# rotateTo(0)
# sleep(2)