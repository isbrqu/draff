from pdfrw import PdfReader
from glob import glob

getInfoPdf():
	for file in glob('*.pdf'):
		reader = PdfReader(file)
		print(file)
		print(reader.Info)
		print()
