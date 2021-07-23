def printData(data):
    print(data)


def printDataArr(dataArr):
    for data in dataArr:
        print(data)

def printData2DArr(data2DArr):
    for dataArr in data2DArr:
        for data in dataArr:
            print(data)

def printUsername_UserData(username, user_dataArr):
    print(username)
    printDataArr(user_dataArr)

def printUsername_UserDataArr(usernames, users_dataArr):
    for i in range(len(usernames)):
        printUsername_UserData(usernames[i], users_dataArr[i])
        print()

def printFile(fname):
    test = 0


def printUsernames(fname):
    test = 0


def printHackFile(fname, cracker=0, key=0):
    test = 0


def returnUsernames(fname):
    test = 0


def printDataInUser(fname, username):
    test = 0


def printUsernamesFromData(data):
    test = 0


def separateUsername_UserDataArr(dataArr):
    usernames = []
    users_data = []
    one_user_data = []
    previous = 0
    cnt = 0
    for i in range(len(dataArr)):
        if i == previous:
            continue
        if dataArr[i] == "":
            usernames.append(dataArr[previous])
            users_data.append([])
            for j in range(previous + 1, i):
                users_data[cnt].append(dataArr[j - previous])
            previous = i + 1
            cnt += 1

    return usernames, users_data

def oneString_from_arrString(dataArr):
    result = ""
    for data in dataArr:
        result += data + "\n"
    return result

def arrString_from_oneString(string):
    if string[-1:] == "\n":
        string = string[:-1]
    return string.split("\n")

def usernames_datas_to_oneString(usernames, users_dataArr):
    result = ""
    for i in range(len(usernames)):
        result += usernames[i] + "\n"
        for dataArr in users_dataArr[i]:
            result += dataArr + "\n"

    return result