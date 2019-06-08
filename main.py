'''
需要实现：
    URL编解码、HTML编解码；
    MD5查询，base64编解码；
    16进制编解码，ascii码查询转换；
    字节码，UTF-8，GBK编解码；
'''

import tkinter as tk
import urllib.parse,html

def crypto():
    f1 = tk.Frame(mainframe)
    e1_name = tk.Label(f1, text='MD5:')
    e1_data = tk.Entry(f1)
    e1_name.grid(row=0, column=0)
    e1_data.grid(row=0, column=1)
    f1.grid()

    f2 = tk.Frame(mainframe)
    e2_name = tk.Label(f2, text='HTML encode')
    e2_data = tk.Entry(f2)
    e2_name.grid(row=0, column=0)
    e2_data.grid(row=0, column=1)
    f2.grid()
    pass

def code():

    pass

def fresh(event):
    s = t.get(1.0,'end')
    # print((s))
    if not s:
        t.insert('insert',s)
    else:
        e1_data.delete('1.0','end')
        e2_data.delete('1.0','end')
        e3_data.delete('1.0','end')
        e4_data.delete('1.0','end')
        e1_data.insert('insert',get_url(s))
        e2_data.insert('insert',get_html(s))
        e3_data.insert('insert',get_utf_8(s))
        e4_data.insert('insert',get_gbk(s))

def get_url(s):
    s = s[:-1]
    encode = urllib.parse.quote(s)
    decode = urllib.parse.unquote(s)
    return encode if decode == s else decode
def get_html(s):
    encode = html.escape(s)
    decode = html.unescape(s)
    return encode if decode == s else decode
def get_gbk(s):
    try:
        gbk = s.encode('gbk').decode('gbk')
    except Exception as e:
        gbk = e
    return gbk
def get_utf_8(s):
    try:
        utf = s.encode('utf-8').decode('utf-8')
        print('utf-8: ', utf)
    except Exception as e:
        utf = e
    return utf


if __name__ == '__main__':

    app = tk.Tk()
    # app.option_add("*Font", "微软雅黑")
    app.option_add("*Font", "Consolas 14")
    app.geometry('800x500')
    app.title('Code Transform')
    t = tk.Text(app,width=60,height=2)
    t.grid(row=0,column=0)

    app1 = tk.Frame(app)
    b1 = tk.Button(app1,text='加密/解密',width=10,height=3,command=crypto,font="微软雅黑 10")
    b1.grid(row=0,column=0)
    # b2 = tk.Button(app1,text='编码/解码',width=10,height=3,command=code,font="微软雅黑 10")
    # b2.grid(row=0,column=1)
    app1.grid(row=0,column=1)
    mainframe = tk.Frame(app,width=100,height=80)
    mainframe.grid(row=1,column=0,columnspan=2)

    f1 = tk.Frame(mainframe)
    e1_name = tk.Label(f1, text='URL : ')
    e1_data = tk.Text(f1,width=60,height=2)
    e1_name.grid(row=0, column=0)
    e1_data.grid(row=0, column=1)
    f1.grid()

    f2 = tk.Frame(mainframe)
    e2_name = tk.Label(f2, text='HTML : ')
    e2_data = tk.Text(f2,width=60,height=2)
    e2_name.grid(row=0, column=0)
    e2_data.grid(row=0, column=1)
    f2.grid()

    f3 = tk.Frame(mainframe)
    e3_name = tk.Label(f3, text='UTF-8 : ')
    e3_data = tk.Text(f3,width=60,height=2)
    e3_name.grid(row=0, column=0)
    e3_data.grid(row=0, column=1)
    f3.grid()

    f4 = tk.Frame(mainframe)
    e4_name = tk.Label(f4, text='GBK : ')
    e4_data = tk.Text(f4,width=60,height=2)
    e4_name.grid(row=0, column=0)
    e4_data.grid(row=0, column=1)
    f4.grid()
    # e4_data.insert('insert','asfffffffffffffffffffsdgdfhdfhdhdfhdvxcv')

    crypto_lis = []
    code_lis = []

    t.bind('<KeyRelease>',fresh)
    app.mainloop()

    pass