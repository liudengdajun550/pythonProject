deng = 124
xiaofan =deng
#id用于查看空间
print(id(deng))
print(id(xiaofan))
print(deng is xiaofan) #判断是否是同一个东西

xiaofan = 234
print(id(xiaofan))
print(deng is xiaofan) #判断是否是同一个东西

#python中内存重用机制，在值比较小时相同值会公用统一空间，值比较大则会分别构建地址,并没有，还是共享内存

deng =1
xiao = 1
print(id(xiao))
print(id(deng))
deng = 2354531213414212414111111111111111111111
xiao =2354531213414212414111111111111111111111
print(id(xiao))
print(id(deng))
