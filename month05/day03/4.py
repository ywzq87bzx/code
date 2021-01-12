# 实现用窗口翻译
from tkinter import *
from tkinter import messagebox
import requests
import json


# 爬取有道云翻译
def get_request():
    # 获取用户输入的
    key = entry.get()
    key = key.strip()
    if key == "":
        messagebox.showinfo("提示", message='输入要翻译的内容')
    else:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
        data = {}
        data['i'] = key
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        # data['salt'] = 15555921036950
        # data['sign'] = '8325b6617b1cbc8d1d9e5e48f87c971d'
        # data['ts'] = 1555592103695
        # data['bv'] = 'e2a78ed30c66e16a857c5b6486a1d326'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        response = requests.post(url, data=data).json()
        entry1.delete(0, END)
        entry1.insert(0, response['translateResult'][0][0]['tgt'])
        # return response[translateResult][0][0]['tgt']
        # print(response)


# 创建窗口
window = Tk()
# 窗体大小
window.geometry('370x100+930+430')
# 标签控件
lable = Label(window, text="输入要翻译的内容")
lable.grid()
lable1 = Label(window, text="翻译后的结果")
lable1.grid()
# 输入控件
entry = Entry(window, font=("微软雅黑", 15))
entry.grid(row=0, column=1)
entry1 = Entry(window, font=("微软雅黑", 15))
entry1.grid(row=1, column=1)

button = Button(window, text="翻译", width=10, command=get_request)
# 对齐方式
button.grid(row=2, column=0, sticky=W)
button1 = Button(window, text="退出", command=window.quit)
button1.grid(row=2, column=1, sticky=E)
# 消息循环显示界面
window.mainloop()