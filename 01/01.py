
print(12)
print('ok')
print('\"ok\"')
print(True)
print(True and False)
print(True or False)
print(not False)
age = 19
if age > 18:
    print('audit')
else:
    print('child')

a = 12
print(a)
a = 'hello'
print(a)

#ord()函数获取字符的整数表示
print(ord('A'))  
print(ord('中'))

#chr()函数把编码转换为对应的字符
print(chr(65))

#要计算str包含多少个字符，可以用len()函数
print(len('wo de'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print(len('中文de'.encode('utf-8')))