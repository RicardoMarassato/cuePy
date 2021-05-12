#!/usr/bin/python3
import re
import tkinter as tk
from tkinter import filedialog


def generateGUI():
    # getFilePath()
    # generateFileArray()
    # getFileName()
    # getCueFileName()
    # getOutputPath()
    # getCueFileFormat()
    # getOutputPath()
    # getCueFileFormat()
    # generateCueFile()
    pass


def getFilePath():
    filePath = filedialog.askopenfilename()
    print("File path > " + filePath)
    return filePath


def generateFileArray():
    filePath = getFilePath()
    fileNameArray = filePath.split('/')
    for file in fileNameArray:
        match = re.search("\.bin$", file)
        if match:
            binFile = file
    print("File name array > " + str(fileNameArray))
    return binFile


def getFileName():
    binFile = generateFileArray()
    fileName = binFile.replace(".bin", "")
    return fileName


def getCueFileName():
    binFile = generateFileArray()
    cueFileName = binFile.replace(".bin", ".cue")
    return cueFileName


def getOutputPath():
    writePath = filedialog.askdirectory()
    return writePath


def getCueFileFormat():
    binFile = generateFileArray()
    writeFileTypeToCue = 'FILE "%s" BINARY\n' % (binFile)
    writeTrackToCue = '  TRACK 01 MODE2/2352\n'
    writeIndexToCue = '    INDEX 01 00:00:00'
    writeToCue = writeFileTypeToCue + writeTrackToCue + writeIndexToCue
    print(writeToCue)
    # writePath = filedialog.askdirectory()
    return writeToCue


def generateCueFile():
    writePath = getOutputPath()
    cueFileName = getCueFileName()
    writeToCue = getCueFileFormat()
    createCueFile = writePath + "/%s" % cueFileName
    writeCueFile = open(createCueFile, "w")
    writeCueFile.write(writeToCue)
    writeCueFile.close()


def main():
    print("Python cue file generator!")
    root = tk.Tk()
    root.withdraw()
    generateGUI()


if __name__ == '__main__':
    main()
