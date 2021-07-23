import random

#for single string
def ceaserCipher(data, key):
    encrypted = ""
    for i in range(len(data)):
        char = data[i]
        if char == '\n':
            continue
        encrypted += chr(
            (ord(char) + key - 32) % 95 + 32)  # ASCII charactors from 32 (Space) to 127 (Delete) 95 charactors

    return encrypted

#for string array
def ceaserCipher_arr(dataArr, key):
    encryptedArr = []
    for data in dataArr:
        encrypted = ceaserCipher(data, key)
        encryptedArr.append(encrypted)

    return encryptedArr

#for single string
def ceaserCipher_fix(data, key):
    fixed = ""
    for i in range(len(data)):
        char = data[i]
        if char == '\n':
            continue
        fixed += chr((ord(char) - key - 32) % 95 + 32)
    return fixed

#for string array
def ceaserCipher_fix_arr(dataArr, key):
    fixed_Arr = []
    for data in dataArr:
        fixed = ceaserCipher_fix(data, key)
        fixed_Arr.append(fixed)

    return fixed_Arr

def ceaserCipher_fix_2Darr(data2Darr, key):
    fixed_2DArr = []
    for dataArr in data2Darr:
        fixed_Arr = ceaserCipher_fix_arr(dataArr, key)
        fixed_2DArr.append(fixed_Arr)

    return fixed_2DArr

def keyGen_random(seed=0):
    if seed != 0:
        random.seed(seed)
    ran = random.randrange(1, 95)
    return ran


def keyGen_string(passWord):
    sum = 0
    for char in passWord:
        sum += ord(char)
    return sum % 95
