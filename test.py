print(2 if 2>1 else 1)

# import cgi,html
# s = 'asda <>{}&'
# a = html.escape(s)
# b = html.unescape('%0A')
# print(s)
# print(a)
# print(b)

import urllib.parse

s = 'asd'
a = urllib.parse.quote(s)
print(len(a),a)
print(1,urllib.parse.unquote('%0A'),1)

