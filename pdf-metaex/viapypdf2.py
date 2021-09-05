import os
import glob
import subprocess

import selenium
import time

import PyPDF2
import signal

import win32gui
import win32api
import win32con

def ensayo():
	driver = selenium.webdriver.Firefox()
	pdfs = glob.glob('*.pdf')
	pdfs.sort()
	if not os.path.isdir('ensayo'):
		os.mkdir('ensayo')
	if not os.path.isdir('libro'):
		os.mkdir('libro')
	for pdf in pdfs:
		time.sleep(3)
		print()
		print(f'file: {pdf}')
		print('='*200)
		driver.get(f'file:///F:/Libros/liberalismo/{pdf}')
		print('0-Ensayo u otro')
		print('1-Libro')
		print()
		resp = int(input('Respuesta: '))
		invalid = True
		while invalid:
			invalid = False
			if resp == 0:
				movefile('ensayo', pdf)
			elif resp == 1:
				movefile('libro', pdf)
			else:
				invalid = True
				print('entrada invalida!')
				resp = int(input('Respuesta: '))

def movefile(path, pdf):
	if os.path.isfile(f'{path}/{pdf}'):
		os.remove(pdf)
	else:
		os.rename(pdf, f'{path}/{pdf}')

def loadwindowslist(hwnd, topwindows):
	topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))

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

def getinfo(file):
	with open(file, 'rb') as pdf:
		try:
			reader = PyPDF2.PdfFileReader(pdf)
			print(file.replace(path, ''))
			print(reader.getDocumentInfo())
		except Exception as e:
			print('FAIL: ' + file)
		print()

def ccmetadata(file, metadata):
	os.rename(file, file.replace(' ', '_'))
	file = file.replace(' ', '_')
	time.sleep(2)
	origin_name = file
	copy_name = f'copy_{file}'
	# copy file
	try:
		with open(origin_name, 'rb') as origin:
			reader = PyPDF2.PdfFileReader(origin)
			if reader.isEncrypted:
			    reader.decrypt('')
			writer = PyPDF2.PdfFileWriter()
			writer.appendPagesFromReader(reader)
			writer.addMetadata(metadata)
			with open(copy_name, 'wb') as copy:
				writer.write(copy)
		# move file
		os.rename(origin_name, f"old/{origin_name.replace('_', ' ')}")
		os.rename(copy_name, f"new/{copy_name.replace('copy_', '', 1).replace('_', ' ')}")
	except Exception as e:
		print(f'error: {origin_name}')
		raise e
readers = []
writer = PyPDF2.PdfFileWriter()
for pdf, i in zip(pdfs, range(0, len(pdfs))):
	file = open(pdf, 'rb')
	reader = PyPDF2.PdfFileReader(file)
	readers.append(reader)
	writer.appendPagesFromReader(readers[i])
	file.close()
with open('completo.pdf', 'wb') as copy:
	writer.write(completo)

if not os.path.isdir('old'):
	os.mkdir('old')
if not os.path.isdir('new'):
	os.mkdir('new')
files = glob.glob('*.pdf')
for file in files:
	try:
		author, title = file.replace('.pdf', '', 1).split(' - ', 1)
	except ValueError as e:
		author, title = file.replace('.pdf', '', 1).split('_-_', 1)
	ccmetadata(file, {
		'/Title': title.title(),
		'/Author': author,
		'/Producer': '',
		'/Tag': 'Libro'
	})

def delete_page(file, pages=[]):
	inputfile = PyPDF2.PdfFileReader(file, 'rb')
	outputfile = PyPDF2.PdfFileWriter()
	for i in range(inputfile.getNumPages()):
		if i not in pages:
			page = inputfile.getPage(i)
			outputfile.addPage(page)
	with open('copy ' + file, 'wb') as f:
		outputfile.write(f)

def robo(author=None):
	if author == None:
		author = input('autor: ')
	for file in glob.glob('*.pdf'):
		sep = file.replace('.pdf', '').split(' - ', 1)
		print(f'\npdf: {file}')
		print('='*100)
		print(f'0 - {sep[0]}')
		print(f'1 - {sep[1]}')
		print(f'2 - todo')
		print(f'3 - voltear sin autor\n')
		invalid = True
		while invalid:
			try:
				invalid = False
				pos = int(input('conservar: '))
				if pos < 2:
					newname = f'{author} - {sep[pos]}'
					os.rename(file, f'{newname}.pdf')
					print(f'renombrado: {newname}')
				elif pos == 2:
					print(f'nombre: {file}')
				elif pos == 3:
					newname = f'{sep[1]} - {sep[0]}'
					os.rename(file, f'{newname}.pdf')
					print(f'renombrado: {newname}')
				else:
					invalid = True
					print('entrada invalida')
			except FileExistsError:
				os.rename(file, f'{newname} (2).pdf')
		print()

def reversedguion():
	for file in glob.glob('*.pdf'):
		if file.count(' - ') > 0:
			title, author = file.replace('.pdf', '').split(' - ', 1)
			try:
				os.rename(file, f'{author} - {title}.pdf')
			except FileExistsError:
				os.rename(file, f'{author} - {title} (2).pdf')