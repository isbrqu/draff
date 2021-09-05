import os
import re

i = 1
name = input('nombre de carpeta: ')
path = f'C:\\Users\\isbrq\\Downloads\\{name}'
os.chdir(path)
imgs = os.listdir()
# imgs.sort(key=lambda i: os.path.getmtime(os.path.join(path, i)))
imgs.sort(key=lambda i: int(re.search(r'(\d+)-', i).group(1)))
for img in imgs:
	os.rename(f'{path}\\{img}', f'{path}\\{i}-{name}.png')
	i += 1
print('successful!')
