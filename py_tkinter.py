import tkinter as tk
import os
import time


# 记录事件的函数
def record_time():
    global kinds
    local_time = time.strftime('%H:%M:%S  %Y-%m-%d ', time.localtime())
    content = kinds[kind_value.get()][0] + ':\t' + methods[method_value.get()][0] + '时间     ' + '\t' + local_time + '\n'
    text_1.insert(tk.END, content)


def save_time():
    path = os.getcwd()
    src_path = os.path.join(path, 'time1.txt')
    contents = text_1.get(0.0, tk.END)
    if os.path.exists(src_path):
        with open(src_path, 'ab') as file:
            file.seek(0)
            file.write(contents.encode('utf-8'))
    else:
        with open(src_path, 'wb') as file:
            file.close()


if __name__ == "__main__":

    # 创建一个窗口
    root = tk.Tk()
    root.title('record_time')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    win_width = 1000
    win_height = 618  # 黄金分割比例：0.618
    distance_x = (screen_width - win_width) / 2
    distance_y = (screen_height - win_height) / 2
    root.geometry('%dx%d+%d+%d' % (win_width, win_height, distance_x, distance_y))

    # 创建标签
    label_1 = tk.Label(root, text='选择当前投料的种类：', width=20, padx=10, pady=6, font=16)
    label_1.place(x=20, y=20)
    label_2 = tk.Label(root, text='投料时间记录：', width=20, padx=10, pady=6, font=16)
    label_2.place(x=500, y=20)

    # 创建radio
    kind_value = tk.IntVar()
    kinds = [('OK料', 0), ('NG料', 1), ('素材', 2)]
    for kind, num in kinds:
        tk.Radiobutton(root, text=kind, font=16, value=num, variable=kind_value).place(x=((num + 1) * 80 - 40), y=60)
    method_value = tk.IntVar()
    methods = [('送洗', 0), ('投料', 1), ('投完', 2)]
    for kind, num in methods:
        tk.Radiobutton(root, text=kind, font=16, value=num, variable=method_value).place(x=((num + 1) * 80 - 40), y=120)

    # 创建Button
    button_1 = tk.Button(root, text='记录', padx=10, pady=6, font=16, bg='#6495ED', fg='white',
                         activebackground='#6495ED', command=record_time)
    button_1.place(x=40, y=180)
    button_2 = tk.Button(root, text='保存', padx=10, pady=6, font=16, bg='#6495ED', fg='white',
                         activebackground='#6495ED', command=save_time)
    button_2.place(x=200, y=180)

    # 创建一个text
    text_1 = tk.Text(root, font=18, width=50, height=20)
    text_1.place(x=350, y=80)

    root.mainloop()
