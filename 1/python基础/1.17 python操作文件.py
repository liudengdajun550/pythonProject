#打开文件
text = open('../../data/测试文件.txt')
print(text)
text_read = text.read() #全部读取
print(text_read)

text = open('../../data/测试文件.txt')
text_read_lines = text.readlines()#按行读取
print(text_read_lines)

for line in text_read_lines:
    print(line)
# 关闭文件
text.close()

#写文件
txt = open('../../data/writeFile.txt', 'w')#写方式打开一个文件,W操作会覆盖原来内容
txt.write('wo shi yi ge piao liang ren') #写入内容,每次打开写入会覆盖文件内容
txt.write('hui bu hui append ')
txt.write('change lines \n good day') #换行
txt.close() #关闭文件
#追加文件内容
txt = open('../../data/writeFile.txt', 'a')#写方式打开一个文件,a操作会在原来内容后增加
txt.write('wo shi yi ge piao liang ren\n') #写入内容
txt.write('wo shi yi ge piao liang ren')
txt.close() #关闭文件

#文件写完后只有关闭才能读
txt = open('../../data/writeFile.txt', 'w')#写方式打开一个文件,a操作会在原来内容后增加
for i in range(10):
    txt.write(str(i)+'\n')
txt.close()
txt = open('../../data/writeFile.txt', 'r')#写方式打开一个文件,a操作会在原来内容后增加
print(txt.read())
txt.close()#还是要关闭文件，经常操作出问题或者写文件没写完但程序出问题了，导致数据出问题

#为了防止文件忘记关闭，导致抛出异常等问题，可以使用with关键字进行处理
#举个例子,写的麻烦了
txt = open('../../data/writeFile.txt', 'w')#写方式打开一个文件,a操作会在原来内容后增加
try:
    for i in range(10):
        10/i-5
        txt.write(str(i)+'\n')
except Exception:
    print('Error:',i)
finally:
    txt.close()
#使用with,可以帮助我们自动进行文件关闭，并抛出异常
with open('../../data/writeFile.txt', 'w') as f:
    for i in range(10):
        10/i-5
        f.write(str(i)+'\n')
