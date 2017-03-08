#coding:utf-8

import re
str = '/watch?v=cSGny5Xfoa8&list=PLO5e_-yXpYLBO6ZaDgV7YH4drssQCSw5n&index=18'
# str = u'/watch?v=cSGny5Xfoa8&index=18&list=PLO5e_-yXpYLBO6ZaDgV7YH4drssQCSw5n'
b = re.findall(ur'/watch\?(v=\w+)',str)
f = re.findall(ur'(\&list=[\_\-\w]+)',str)
h = re.split('&',str)
print f[0]+b[0]
print h