import tkinter as tk

root = tk.Tk()
root.title(u"Software Title")
root.geometry("600x400")

# Canvas Widget を生成
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

root.mainloop()