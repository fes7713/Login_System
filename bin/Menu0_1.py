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


def saveText():
    key = EC.keyGen_string(password)
    encripted_data_arr = EC.ceaserCipher_arr(data_user, key)
    users_data[pos_data] = FV.arrString_from_oneString(encripted_data_arr)
    FO.saveFile_arr(fname, users_data)

def log_in():
    if LS.login(username, password, usernames_encryp_arr):
        key = EC.keyGen_string(password)
        username_encryp = EC.ceaserCipher(username, key)
        pos_data = usernames_encryp_arr.index(username_encryp)

        data_user = users_data[pos_data]
        data_user = EC.ceaserCipher_fix_arr(data_user, key)
        data_user = FV.oneString_from_arrString(data_user)

        textEntry.delete('1.0', 'end')
        textEntry.insert('end', data_user)
        error_msg.set("Log in Successful")
    else:
        error_msg.set("Log in failed")


def file_open(fname):
    data_arr = FO.loadFile_arr(fname)
    usernames_encryp_arr, users_data = FV.separateUsername_UserDataArr(data_arr)
    return usernames_encryp_arr, users_data


username = ""
password = ""
username_encryp = ""
data_user = ""
pos_data = 0

fname = "sample_encripted.txt"
usernames_encryp_arr, users_data = file_open(fname)

root = tk.Tk()

root.geometry("960x480")

username_str = tk.StringVar()
password_str = tk.StringVar()
error_msg = tk.StringVar(value="Login")

# textString = tk.StringVar()
# textString_edit = tk.StringVar()


textEntry = tk.Text(root, height=30)
label1 = tk.Label(root, text="Username")
label2 = tk.Label(root, text="Password")
entry1 = tk.Entry(textvariable=username_str)
entry2 = tk.Entry(textvariable=password_str)
msg1 = tk.Label(textvariable=error_msg)

btn1 = tk.Button(root, text="Print", command=printText())
btn_save = tk.Button(root, text="Save", command=saveText)
btn_login = tk.Button(root, text="Log  In", command=lambda: [getUsernamePassword(), log_in()])
btn_signup = tk.Button(root, text="Sign Up")

textEntry.grid(row=0, column=0, rowspan=15, sticky=tk.N + tk.S)
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
entry1.grid(row=0, column=2, columnspan=2)
entry2.grid(row=1, column=2, columnspan=2)
btn_login.grid(row=2, column=1)
btn_signup.grid(row=2, column=2, sticky=tk.W)
msg1.grid(row=3, column=1)
btn_save.grid(row=4, column=1, sticky=tk.W + tk.E)
btn1.grid(row=5, column=1, sticky=tk.W + tk.E)

root.mainloop()

print(username)
print(password)
