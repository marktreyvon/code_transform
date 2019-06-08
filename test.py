# # # # # # print(2 if 2>1 else 1)
# # # # #
# # # # # # import cgi,html
# # # # # # s = 'asda <>{}&'
# # # # # # a = html.escape(s)
# # # # # # b = html.unescape('%0A')
# # # # # # print(s)
# # # # # # print(a)
# # # # # # print(b)
# # # # #
# # # # # # import urllib.parse
# # # # # #
# # # # # # s = 'asd'
# # # # # # a = urllib.parse.quote(s)
# # # # # # print(len(a),a)
# # # # # # print(1,urllib.parse.unquote('%0A'),1)
# # # # # import binascii,base64
# # # # # def str2hex(s):
# # # # #     return binascii.b2a_hex(s.encode('utf-8'))
# # # # #     pass
# # # # # s = 'abc'
# # # # # print(ord(b'a'))
# # # # # print(bin(97))
# # # # # print(ascii(b's'))
# # # # # print(s,str2hex(s))
# # # # # s = s
# # # # # print(str(base64.b64encode(s.encode('utf-8'))))
# # # # # # print(base64.decode(base64.encode(s)))
# # # # # a = b'aaa'
# # # # # print(a)
# # # # # print(base64.b64encode('a=sdasda'.encode('utf-8')).decode(encoding='utf-8'))
# # # #
# # # # ''':authority: www.cmd5.com
# # # # :method: POST
# # # # :path: /
# # # # :scheme: https
# # # # accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# # # # accept-encoding: gzip, deflate, br
# # # # accept-language: zh-CN,zh;q=0.9,en;q=0.8
# # # # cache-control: max-age=0
# # # # content-length: 1993
# # # # content-type: application/x-www-form-urlencoded
# # # # cookie: ASP.NET_SessionId=atab4gb0t5atibqk2ah3anf3; FirstVisit=2019/6/8 12:55:57; _uab_collina=155996974045963821412973; Hm_lvt_0b7ba6c81309fff7ce4498ec7b107c0b=1559969741; Hm_lpvt_0b7ba6c81309fff7ce4498ec7b107c0b=1559969747
# # # # origin: https://www.cmd5.com
# # # # referer: https://www.cmd5.com/
# # # # upgrade-insecure-requests: 1
# # # # user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36
# # # # __EVENTTARGET:
# # # # __EVENTARGUMENT:
# # # # __VIEWSTATE: rz8AYRFRDjYDE17W0vB0ixRBoyGunvNyaPRCZ7ycWMvI9fXzwt5TgxM+w5hnLeMaOkkBFtrBx1eQrv+NxL359QrqgsPPvA/LHD0lGLGjpssp2f3t29aBaHHjTYRneofv7B0jWlW7W7t8IppkAOdcz/GG88ZOB+zeMYS2FEKu24N34YmIHRQzYMOSnsH6R7Yq2segcxTBOswCBESxs08pwqtOtG+mx7QKrZWqAmIvZNfKCxGceF3nUVQaNzu3QD5dYma5dXZqRRfPOZ+H7I/lI6qWHm8uq59gyMg9b2aunsFzo2ICDzXFNuwViSjm1oo8VVinMl4p0BQJ1WW8BwfCNC8sr1fposdbm/jp21EvISnewJpG0G6rhuRF9DOCIHoQSc86D6AkgQCXElrA7i8+FrgsAyPAM3d/Yp8h13fWQ5iHxN6fi+Yg421tlznsRDYk6KopPr0EDc+6Z/UcVKWPMYg2F+spbVkH4JcVtai0TJTZ4p3Bqub48ABHbKAQ9R0u62zpa8YbMjFpPVQoJQnH6Z85LVwd9gn7apPucvIQlHbYPFmSJwRrgogSlHVtd/j1mIwUZnDaTpobpQAt8QGOWQoG9QRbA2V5c779z75KvoNtrFGMhVo7VkUvbmHh/IKkbPqI+i8fCCTm4u3lUnsFm0lzeCBAgejbJtYoP6W76i7T3b1J4XOAC+q4i1nT0g7rnLKAUFzUMGm60PZ03BiXXn8lJoAOsGy0lNU5m2WDksPqMBn+ax9lP6RIWF0yOsFimwcIdIZS9YlF5TCdDNfFkwcopDisja8cGMQTrTDnC0k6SjHG/CvkKFytzrlKvkIXQH2Ykn3X714v3AkAMohUg0jX8Vg04yR2ifMsglty+gZYuHSo+DpukDoSQrWQ1mquxuFwRXRZGjf1XXGbys+vHDUIfMtD48XE5gAHToE205hQiLB/PWDFD5Pxdq+nB2QygfjPtX1+k3M4UX/lKhaNG87hTS18PYMGt6X/ePleVoEQjgWSAbUiyG2Ow1VIHzEv49TfGS2h91v5vfmba6XAiUrXOviTaZADUGBDsfXKL3sel+tVCAAgLTm8dz879QqC7xM63C3mOCLpYHHXJLC4Pp/bx9BDdqPTvWuD1Jb1qNKTY974I7+SLo6iZ8TbyniwWCgDEXnN9p3V6dfSZF9zV2gAWAvLInS59d7Xoc9N1V3Sy/ObgbAuJf/pZ1f67/aU9E43mZv4vJpHn+uCtrfSX3YYadvHTR7Ejyvi/Ax2/JNX7hS7Xa9DdEcfa8Azvgmntj/VoGlKA8FdW0YUgoe7EbkBej41nBMaPY3oneW2G2+bBRtFrMOGtonjXr88fmptxKf85GqGYP920QABMB9GusiuATv4J00ulD+31syLgmjZKQ75bClM+5ZEpjykun2muvUC7FbAadveoRNHhMgghLwy0Wjgjt5YXByqKQ==
# # # # __VIEWSTATEGENERATOR: CA0B0334
# # # # ctl00$ContentPlaceHolder1$TextBoxInput: ab9e80519195ce8eb88058e57191ccf5
# # # # ctl00$ContentPlaceHolder1$InputHashType: md5
# # # # ctl00$ContentPlaceHolder1$Button1: 查询
# # # # ctl00$ContentPlaceHolder1$HiddenFieldAliCode:
# # # # ctl00$ContentPlaceHolder1$HiddenField1:
# # # # ctl00$ContentPlaceHolder1$HiddenField2: EO6xou0z988FpGdRtgdPAhfsMQF1I8xeVtCEQp8K9Iu2amW3Wnd905h4TJMPS98I
# # # # '''
# # # #
# # # # import requests
# # # #
# # # # url = 'https://www.cmd5.com'
# # # # hdr = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# # # # accept-encoding: gzip, deflate, br
# # # # accept-language: zh-CN,zh;q=0.9,en;q=0.8
# # # # cache-control: max-age=0
# # # # content-length: 1993
# # # # content-type: application/x-www-form-urlencoded
# # # # cookie: ASP.NET_SessionId=atab4gb0t5atibqk2ah3anf3; FirstVisit=2019/6/8 12:55:57; _uab_collina=155996974045963821412973; Hm_lvt_0b7ba6c81309fff7ce4498ec7b107c0b=1559969741; Hm_lpvt_0b7ba6c81309fff7ce4498ec7b107c0b=1559969747
# # # # origin: https://www.cmd5.com
# # # # referer: https://www.cmd5.com/
# # # # upgrade-insecure-requests: 1
# # # # user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'''
# # # #
# # # # req = requests.get(url)
# # # # req = requests.post()
# # # # print(req.text)
# # # #
# # # import struct
# # #
# # # s = ''
# # # # print(ord(b'a'))
# # # # print(bin(97))
# # # # print(ascii(b's'))
# # # def str2bin(s):
# # #     return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
# # #
# # # def bin2str(s):
# # #     return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
# # #
# # # # print(encode('abc'))
# # # a = u'啊'
# # # print(a)
# # # print(type(a))
# # # s = 'π排球の'
# # # b1 = s.encode('utf-8').decode('unicode-escape')
# # # b2 = s.encode()
# # # print(b1)
# # # print(b2)
# # # q = ascii('安达')
# # # print(len(q),q)
# # # # chr(ascii('ksdj奥安达'))
# # # print('\u5b89')
# # # def str_encode(s):
# # #     return ascii(s)
# # # def str_decode(s):
# # #     return s.encode('utf-8').decode('unicode_escape')
# # #
# # # print(str_decode(q),len(str_decode(q)))
# #
# # def sayName(func):
# #     def inner():
# #         print("I'm Yu")
# #         return func
# #     return inner
# #
# # def sayHi():
# #     print('Hello, World')
# # s = sayName(sayHi)
# # s()
# #
#
#
# s = 'aslkjl;vv;;<>'
# import html
# a = html.escape(s)
# # print(a)
# # print(html.unescape(a))
#

import binascii,base64
# def str2bin(s):
#     return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
# def bin2str(s):
#     return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
#
# s ='asd'
#
# print(s)
# a = str2bin(s)
# print(a)
# print(bin2str(a))
s = '三个'
print(s)
a = bytes(s,encoding='utf-8')
# print(a)
b = a.decode(encoding='gbk')
print(b)
c = a.decode(encoding='utf-8')
print(c)
w = '涓変釜'
ww = w.encode(encoding='gbk').decode('utf-8')
print(ww)
