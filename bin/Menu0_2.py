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
    data_arr = textEntry.get('1.0', 'end -1c')
    data_arr = FV.arrString_from_oneString(data_arr)
    encripted_data_arr = EC.ceaserCipher_arr(data_arr, key)
    users_data[pos_data] = encripted_data_arr
    FO.saveData_Users_arr(fname, usernames_encryp_arr, users_data)
    error_msg.set("Saved!")

def clearText():
    textEntry.delete('1.0', 'end')


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


def sign_up():
    if LS.signup(username, password, usernames_encryp_arr):
        error_msg.set("Sign up Successful")
    else:
        error_msg.set("user already exists")


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
#
# text_bar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
#
# text_canvas = tk.Canvas(root)
# text_canvas.config(xscrollcommand=text_bar_x.set)
# text_canvas.config(scrollregion=(0,0,1200,600)) #スクロール範囲
# text_canvas.grid(row=0, column=0)
#
# text_frame = tk.Frame(text_canvas)
# text_canvas.create_window(0, 0, window=text_frame, anchor=tk.NW, width=1200)
#
# textEntry = tk.Text(text_frame, pady=10, padx=10)
# text_bar_y = tk.Scrollbar(text_frame, command=textEntry.yview, orient=tk.VERTICAL)
# textEntry["yscroll"] = text_bar_y.set

###########################################
canvas = tk.Canvas(root)

bar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
bar_x.grid(row=0, column=0, sticky="we")

canvas.config(xscrollcommand=bar_x.set, scrollregion=(0,0,900,270))
canvas.grid(row=1, column=0, sticky="nwse")

# Frame Widgetを 生成
frame = tk.Frame(canvas)

# Frame Widgetを Canvas Widget上に配置
canvas.create_window(0, 0, window=frame, anchor=tk.NW, width=900, height=270)

# 複数の Button Widget 生成し、Frame上に配置
textbox = tk.Text(frame)
text_bar_y = tk.Scrollbar(frame, command=textbox.yview, orient=tk.VERTICAL)
textbox["yscroll"] = text_bar_y.set
text_bar_y.pack(side=tk.LEFT, fill=tk.Y)
textbox.pack(fill=tk.BOTH)


################################3
label1 = tk.Label(root, text="Username")
label2 = tk.Label(root, text="Password")
entry1 = tk.Entry(textvariable=username_str)
entry2 = tk.Entry(textvariable=password_str)
msg1 = tk.Label(textvariable=error_msg)


btn1 = tk.Button(root, text="Print", command=printText)
btn_save = tk.Button(root, text="Save", command=saveText)
btn_clear = tk.Button(root, text="   Clear   ", command=clearText)
btn_login = tk.Button(root, text="Log  In", command=lambda: [getUsernamePassword(), log_in()])
btn_signup = tk.Button(root, text="Sign Up", command=lambda: [getUsernamePassword(), sign_up()])

# text_bar_y.grid(row=0, column=1, sticky="ns")
# text_bar_x.grid(row=1, column=0, sticky="we")
# textEntry.pack(fill=tk.BOTH)
# text_frame.grid(row=0, column=0, rowspan=15, sticky="ns")
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
entry1.grid(row=0, column=2, columnspan=2)
entry2.grid(row=1, column=2, columnspan=2)
btn_login.grid(row=2, column=1)
btn_signup.grid(row=2, column=2, sticky=tk.W)
msg1.grid(row=3, column=1, columnspan=2)
btn_save.grid(row=4, column=1, padx = 3, sticky=tk.W + tk.E)
btn_clear.grid(row=4, column=2, padx = 3, sticky=tk.W)
btn1.grid(row=5, column=1, sticky=tk.W + tk.E)

root.mainloop()

print(username)
print(password)
