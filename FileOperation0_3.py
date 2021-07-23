import os
import shutil

def makeFile(fname):
    file1 = open(fname, "w")
    file1.close()

def saveFile(fname, data):
    file1 = open(fname, "w") #w == writing mode, r =readinf more, a = adding data into file
    file1.write(data + "\n")
    file1.close()

def saveFile_arr(fname, data_arr):
    file1 = open(fname, "w")
    for data in data_arr:
        if '\n' not in data:
            data = data + '\n'
        file1.write(data)
    file1.close()

def saveData_Users_arr(fname, usernames, data_arr):
    file1 = open(fname, "w")
    file1.close()
    for i in range(len(usernames)):
        addDataFile(fname, usernames[i])
        addDataFile_arr(fname, data_arr[i])
        addDataFile(fname, "")

def addDataFile(fname, data):
    file1 = open(fname, "a")  # w == writing mode, r =readinf more, a = adding data into file
    file1.write(data + "\n")
    file1.close()


def addDataFile_arr(fname, data_arr):
    file1 = open(fname, "a")
    for data in data_arr:
        if '\n' not in data:
            data = data + '\n'
        file1.write(data)
    file1.close()

def loadFile(fname):
    file1 = open(fname, "r")
    data = file1.read()
    file1.close()
    return data

def loadFile_arr(fname):
    file1 = open(fname, "r")
    data = file1.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace('\n', '')
    file1.close()
    return data

def deleteFile(fname, complete = True):
    if(complete == False):
        lstDir = os.listdir()
        print(lstDir)
        for str in lstDir:
            if "bin" == str:
                shutil.move(fname, "bin/" + fname)
                break
        os.mkdir("bin")
        shutil.move(fname, "bin/" + fname)

def file_checker(fname):
    if "\\" in fname:
        last_pos = fname.rindex("\\")
        os.chdir(fname[:last_pos])
        fname = fname[last_pos+1:]
    listDir = os.listdir()
    if not fname in listDir:
        return False
    return True
    # == make bin and move file there:
# def deleteFileComp(fname):
# def addData_end(fname, data):
# def addData_top(fname, data):
# def deleteData_from(fname, line_from):

# data = loadFile("info.txt")

# print(data)
# lstDir = os.listdir()
# print(lstDir)

# deleteFile("info.txt", False)


