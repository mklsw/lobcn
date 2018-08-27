# print 输出object后默认用的是空格，sep 可以用来修改

# print(1,2,3,4)
#
# print(1,2,3,4,sep="*")
#
# print(1,2,3,4,sep='#')
#
# print(1,2,3,4,sep='#',end='&')


# 将输出的数据 格式化 .format 参数

x = 5

y = 10

print('The value of x is {} and y is {}'.format(x,y))


print('i love {0} and {1}'.format('bread','butter'))

print('i love {1} amd {0}'.format ('bread','butter'))


print('hello {name},{greeting}'.format(greeting ='goodmorning',name = 'tom'))

