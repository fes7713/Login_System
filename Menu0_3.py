import tkinter as tk
import FileOperation0_3 as FO, Encoder as EC, login_signup0_1 as LS, FileViewer as FV

test = 0


def sayHello():
    print("Hello")


def getUsername():
    username = input("Type Username here :")
    return username


def getPassword():
    password = input("Type password here :")
    return password


def printString():
    print(str.get())


def getUsernamePassword():
    global username, password
    username = username_str.get()
    password = password_str.get()


def printText():
    print(textEntry.get('1.0', 'end-1c'))


def changeFile():
    global fname
    temp = fname_str.get()
    # if not FO.file_checker(temp):
    #     error_msg.set("File Not Found")
    #     return
    fname = temp
    fname_str_now.set(fname)
    error_msg.set("File Changed")


def viewFile():
    if not FO.file_checker(fname):
        error_msg.set("File Not Found")
        return
    textEntry.delete('1.0', 'end')
    data = FO.loadFile(fname)
    textEntry.insert('end', data)
    error_msg.set("Viewing " + fname)


def saveText():
    global pos_data, data_user, username_encryp
    print(pos_data)
    key = EC.keyGen_string(password)
    data_arr = textEntry.get('1.0', 'end -1c')
    data_arr = FV.arrString_from_oneString(data_arr)
    encripted_data_arr = EC.ceaserCipher_arr(data_arr, key)
    users_data[pos_data] = encripted_data_arr
    FO.saveData_Users_arr(fname, usernames_encryp_arr, users_data)
    error_msg.set("Saved!")


def clearText():
    textEntry.delete('1.0', 'end')
    error_msg.set("Text Cleared")


def log_in():
    global pos_data, data_user, username_encryp
    usernames_encryp_arr, users_data = file_open(fname)
    if LS.login(username, password, usernames_encryp_arr):
        key = EC.keyGen_string(password)
        username_encryp = EC.ceaserCipher(username, key)
        pos_data = usernames_encryp_arr.index(username_encryp)
        print(pos_data)
        data_user = users_data[pos_data]
        data_user = EC.ceaserCipher_fix_arr(data_user, key)
        data_user = FV.oneString_from_arrString(data_user)

        textEntry.delete('1.0', 'end')
        textEntry.insert('end', data_user)
        error_msg.set("Log in Successful")
    else:
        error_msg.set("Log in failed")


def sign_up():
    global pos_data, data_user, username_encryp, usernames_encryp_arr, users_data
    usernames_encryp_arr, users_data = file_open(fname)
    if LS.signup(username, password, usernames_encryp_arr):
        pos_data = len(usernames_encryp_arr)
        key = EC.keyGen_string(password)
        username_encryp = EC.ceaserCipher(username, key)
        usernames_encryp_arr.append(username_encryp)
        data_user = ["Welcome to Log in System!"]
        users_data.append(data_user)
        print(users_data)
        textEntry.delete('1.0', 'end')
        textEntry.insert('end', data_user)
        error_msg.set("Sign up Successful")
    else:
        error_msg.set("user already exists")


def file_open(fname):
    import os

    if not FO.file_checker(fname):
        FO.makeFile(fname)
        return [], []

    data_arr = FO.loadFile_arr(fname)
    usernames_encryp_arr, users_data = FV.separateUsername_UserDataArr(data_arr)
    return usernames_encryp_arr, users_data


username = ""
password = ""
username_encryp = ""
data_user = ""
pos_data = 0

fname = "sample_encrypted.txt"
usernames_encryp_arr, users_data = file_open(fname)
print(usernames_encryp_arr)

root = tk.Tk()

root.geometry("960x560")

username_str = tk.StringVar()
password_str = tk.StringVar()
error_msg = tk.StringVar(value="Login")
fname_str = tk.StringVar(value=fname)
fname_str_now = tk.StringVar(value=fname)

canvas = tk.Canvas(root, height=530, width=550)

bar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
bar_x.grid(row=15, column=0, sticky="we")

canvas.config(xscrollcommand=bar_x.set, scrollregion=(0, 0, 800, 280))
canvas.grid(row=0, column=0, rowspan=15, sticky="nwse")

# Frame Widgetを 生成
frame = tk.Frame(canvas)

# Frame Widgetを Canvas Widget上に配置
canvas.create_window(0, 0, window=frame, anchor=tk.NW, width=1000, height=535)

# 複数の Button Widget 生成し、Frame上に配置
textEntry = tk.Text(frame, height=33)
text_bar_y = tk.Scrollbar(frame, command=textEntry.yview, orient=tk.VERTICAL)
textEntry["yscroll"] = text_bar_y.set
text_bar_y.pack(side=tk.LEFT, fill=tk.Y)
textEntry.pack(fill=tk.BOTH)

################################
label_fname = tk.Label(root, text="File")
label_fname_curr = tk.Label(root, textvariable=fname_str_now)
label1 = tk.Label(root, text="Username")
label2 = tk.Label(root, text="Password")
fname_entry = tk.Entry(textvariable=fname_str)
entry1 = tk.Entry(textvariable=username_str)
entry2 = tk.Entry(textvariable=password_str)
msg1 = tk.Label(textvariable=error_msg)

btn1 = tk.Button(root, text="Print", command=printText)
btn_save = tk.Button(root, text="Save", command=saveText)
btn_clear = tk.Button(root, text="   Clear   ", command=clearText)
btn_login = tk.Button(root, text="Log  In", command=lambda: [getUsernamePassword(), log_in()])
btn_signup = tk.Button(root, text="Sign Up", command=lambda: [getUsernamePassword(), sign_up()])
btn_file_dir = tk.Button(root, text="Change", command=changeFile)
btn_view_file = tk.Button(root, text="View File", command=viewFile)

label_fname.grid(row=0, column=1)
label_fname_curr.grid(row=0, column=5)
label1.grid(row=1, column=1)
label2.grid(row=2, column=1)
fname_entry.grid(row=0, column=2)
entry1.grid(row=1, column=2, columnspan=2)
entry2.grid(row=2, column=2, columnspan=2)
btn_file_dir.grid(row=0, column=4)
btn_login.grid(row=1, column=4, padx=5)
btn_signup.grid(row=2, column=4, padx=5)
msg1.grid(row=3, column=1, columnspan=2)
btn_view_file.grid(row=4, column=1, columnspan=1, padx=3)
btn_save.grid(row=5, column=1, padx=3, sticky=tk.W + tk.E)
btn_clear.grid(row=5, column=2, padx=3, sticky=tk.W)
btn1.grid(row=6, column=1, sticky=tk.W + tk.E)

root.mainloop()

print(username)
print(password)
