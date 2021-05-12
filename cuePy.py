#!/usr/bin/python3
import re
import tkinter as tk
from tkinter import filedialog


def main():
	print("Python cue file generator!")
	root = tk.Tk()
	root.withdraw()

	filePath = filedialog.askopenfilename()
	fileNameArray = filePath.split('/')

	for file in fileNameArray:
		match = re.search("\.bin$", file)
		if match:
			binFile = file
            
	cueFileName = binFile.replace(".bin",".cue")
	fileName = binFile.replace(".bin","")

	writeFileTypeToCue = 'FILE "%s" BINARY\n' %(binFile)
	writeTrackToCue    = '  TRACK 01 MODE2/2352\n'
	writeIndexToCue    = '    INDEX 01 00:00:00'
	writeToCue = writeFileTypeToCue + writeTrackToCue + writeIndexToCue
	print(writeToCue)
	writePath = filedialog.askdirectory()

	createCueFile = writePath + "/%s" %cueFileName
	writeCueFile = open(createCueFile,"w")
	writeCueFile.write(writeToCue)
	writeCueFile.close()

if __name__ == '__main__':
	main()
