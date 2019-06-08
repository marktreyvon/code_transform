'''
需要实现：
    URL编解码、HTML编解码；
    MD5查询，base64编解码；
    16进制编解码，ascii码查询转换；
    字节码，UTF-8，GBK编解码；
更高级功能：
    对应字符高亮
    大量文本点击放大对比
    初始化时从粘贴板导入
    复制到粘贴板
'''
'''
编码解码之间的转换，提供部分在线工具，其余再说
'''

import tkinter as tk,tkinter.messagebox
import urllib.parse,html,binascii,base64

# def crypto():
#     f1 = tk.Frame(mainframe)
#     e1_name = tk.Label(f1, text='MD5:')
#     e1_data = tk.Entry(f1)
#     e1_name.grid(row=0, column=0)
#     e1_data.grid(row=0, column=1)
#     f1.grid()
#
#     f2 = tk.Frame(mainframe)
#     e2_name = tk.Label(f2, text='HTML encode')
#     e2_data = tk.Entry(f2)
#     e2_name.grid(row=0, column=0)
#     e2_data.grid(row=0, column=1)
#     f2.grid()
#     pass

def fresh_raw1(event):
    s1 = e1_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = urllib.parse.unquote(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw2(event):
    s1 = e2_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = html.unescape(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw3(event):
    s1 = e3_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = gb23122utf(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw4(event):
    s1 = e4_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = gbk2utf(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw5(event):
    s1 = e5_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = hex2str(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw6(event):
    s1 = e6_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = base642str(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw7(event):
    s1 = e7_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = bin2str(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
def fresh_raw8(event):
    s1 = e8_data.get(1.0, 'end')[:-1]
    # raw = t.get(1.0,'end')[:-1]
    # if s1 == get_url(raw):
    #     return
    # else:
    #     result = urllib.parse.unquote(s1)
    result = str_decode(s1)
    t.delete('1.0','end')
    t.insert('insert',result)
    fresh(None)
# def fresh_raw(event):
#     result='a'
#     raw = t.get(1.0,'end')[:-1]
#     s1 = e1_data.get(1.0, 'end')[:-1]
#     s2 = e2_data.get(1.0, 'end')[:-1]
#     s3 = e3_data.get(1.0, 'end')[:-1]
#     s4 = e4_data.get(1.0, 'end')[:-1]
#     s5 = e5_data.get(1.0, 'end')[:-1]
#     s6 = e6_data.get(1.0, 'end')[:-1]
#     s7 = e7_data.get(1.0, 'end')[:-1]
#     s8 = e8_data.get(1.0, 'end')[:-1]
#
#     if s1 != get_url(raw) or not s1:
#         result = urllib.parse.unquote(s1)
#     elif s2 != get_html(raw) or not s2:
#         result = html.unescape(s2)
#     elif s3 != utf2gb2312(raw) or not s3:
#         result = gb23122utf(raw)
#     elif s4 != utf2gbk(raw) or not s4:
#         result = gbk2utf(s4)
#     elif s5 != str2hex(raw) or not s5:
#         result = hex2str(s5)
#     elif s6 != str2base64(raw) or not s6:
#         result = base642str(s6)
#     elif s7 != str2bin(raw) or not s7:
#         result = bin2str(s7)
#     elif s8 != str_encode(raw) or not s8:
#         result = str_decode(s8)
#
#     t.delete('1.0','end')
#     t.insert('insert',result)
#     fresh_all()
#     pass

def fresh(event):
    s = t.get(1.0,'end')[:-1]
    e1_data.delete('1.0','end')
    e1_data.insert('insert',get_url(s))
    e2_data.delete('1.0','end')
    e2_data.insert('insert',get_html(s))
    e3_data.delete('1.0','end')
    e3_data.insert('insert',utf2gb2312(s))
    e4_data.delete('1.0','end')
    e4_data.insert('insert',utf2gbk(s))
    e5_data.delete('1.0','end')
    e5_data.insert('insert',str2hex(s))
    e6_data.delete('1.0','end')
    e6_data.insert('insert',str2base64(s))
    e7_data.delete('1.0','end')
    e7_data.insert('insert',str2bin(s))
    e8_data.delete('1.0','end')
    e8_data.insert('insert',str_encode(s))

def get_url(s):
    return urllib.parse.quote(s)
def get_html(s):
    return html.escape(s)
def utf2gbk(s):
    try:
        gbk = s.encode('utf-8').decode('gbk')
    except Exception as e:
        gbk = e
    return gbk
def utf2gb2312(s):
    try:
        gb2312 = s.encode('utf-8').decode('gb2312')
    except Exception as e:
        gb2312 = e
    return gb2312
def gbk2utf(s):
    try:
        utf = s.encode(encoding='gbk').decode('utf-8')
    except Exception as e:
        utf = e
    return utf
def gb23122utf(s):
    try:
        utf = s.encode('gb2312').decode('utf-8')
    except Exception as e:
        utf = e
    return utf
def str2hex(s):
    return binascii.b2a_hex(s.encode('utf-8')).decode(encoding='utf-8')
def hex2str(s):
    return binascii.a2b_hex(s.encode('utf-8')).decode(encoding='utf-8')
def str2base64(s):
    return base64.b64encode(s.encode('utf-8')).decode(encoding='utf-8')
def base642str(s):
    return base64.b64decode(s.encode('utf-8')).decode(encoding='utf-8')
def str2bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
def bin2str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
def str_encode(s):
    return ascii(s)[1:-1]
def str_decode(s):
    return s.encode('utf-8').decode('unicode_escape')

def online_msg():
    a = tk.messagebox.askokcancel('在线工具', '待更新')

def all_clear():
    t.delete('1.0','end')
    e1_data.delete('1.0','end')
    e2_data.delete('1.0','end')
    e3_data.delete('1.0','end')
    e4_data.delete('1.0','end')
    e5_data.delete('1.0','end')
    e6_data.delete('1.0','end')
    e7_data.delete('1.0','end')
    e8_data.delete('1.0','end')


    pass
if __name__ == '__main__':

    app = tk.Tk()
    app.option_add("*Font", "Consolas 14")
    app.geometry('800x450')
    app.title('Code Transform')
    t = tk.Text(app,width=60,height=2)
    t.grid(row=0,column=0)

    app1 = tk.Frame(app)
    b = tk.Button(app1,text='在线工具',width=7,height=2,command=online_msg,font="微软雅黑 9")
    b.grid(row=0,column=1)
    bb = tk.Button(app1,text='清空',width=7,height=2,command=all_clear,font="微软雅黑 9")
    bb.grid(row=0,column=0)
    # b1 = tk.Button(app1,text='加密/解密',width=10,height=3,command=crypto,font="微软雅黑 10")
    # b1.grid(row=0,column=0)
    # b2 = tk.Button(app1,text='编码/解码',width=10,height=3,command=code,font="微软雅黑 10")
    # b2.grid(row=0,column=1)
    app1.grid(row=0,column=1)
    mainframe = tk.Frame(app,width=100,height=80)
    mainframe.grid(row=1,column=0,columnspan=2)

    f1 = tk.Frame(mainframe)
    e1_name = tk.Label(f1, text='URL encode: ')
    e1_data = tk.Text(f1,width=60,height=2)
    e1_name.grid(row=0, column=0)
    e1_data.grid(row=0, column=1)
    f1.grid()

    f2 = tk.Frame(mainframe)
    e2_name = tk.Label(f2, text='HTML encode: ')
    e2_data = tk.Text(f2,width=60,height=2)
    e2_name.grid(row=0, column=0)
    e2_data.grid(row=0, column=1)
    f2.grid()

    f3 = tk.Frame(mainframe)
    e3_name = tk.Label(f3, text='GB-2312 encode: ')
    e3_data = tk.Text(f3,width=60,height=2)
    e3_name.grid(row=0, column=0)
    e3_data.grid(row=0, column=1)
    f3.grid()

    f4 = tk.Frame(mainframe)
    e4_name = tk.Label(f4, text='GBK encode: ')
    e4_data = tk.Text(f4,width=60,height=2)
    e4_name.grid(row=0, column=0)
    e4_data.grid(row=0, column=1)
    f4.grid()

    f5 = tk.Frame(mainframe)
    e5_name = tk.Label(f5, text='Hex encode: ')
    e5_data = tk.Text(f5,width=60,height=2)
    e5_name.grid(row=0, column=0)
    e5_data.grid(row=0, column=1)
    f5.grid()

    f6 = tk.Frame(mainframe)
    e6_name = tk.Label(f6, text='Base64 encode: ')
    e6_data = tk.Text(f6,width=60,height=2)
    e6_name.grid(row=0, column=0)
    e6_data.grid(row=0, column=1)
    f6.grid()

    f7 = tk.Frame(mainframe)
    e7_name = tk.Label(f7, text='Binary encode: ')
    e7_data = tk.Text(f7,width=60,height=2)
    e7_name.grid(row=0, column=0)
    e7_data.grid(row=0, column=1)
    f7.grid()

    f8 = tk.Frame(mainframe)
    e8_name = tk.Label(f8, text='Ascii encode: ')
    e8_data = tk.Text(f8,width=60,height=2)
    e8_name.grid(row=0, column=0)
    e8_data.grid(row=0, column=1)
    f8.grid()

    e1_data.bind('<KeyRelease>',fresh_raw1)
    e2_data.bind('<KeyRelease>',fresh_raw2)
    e3_data.bind('<KeyRelease>',fresh_raw3)
    e4_data.bind('<KeyRelease>',fresh_raw4)
    e5_data.bind('<KeyRelease>',fresh_raw5)
    e6_data.bind('<KeyRelease>',fresh_raw6)
    e7_data.bind('<KeyRelease>',fresh_raw7)
    e8_data.bind('<KeyRelease>',fresh_raw8)

    t.bind('<KeyRelease>',fresh)
    app.mainloop()

    pass