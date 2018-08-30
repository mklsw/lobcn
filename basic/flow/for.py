# -*- coding:utf-8 -*-

# for i in range(1,5):
#
#     print(i)
#
# else:
#     print('The for loop is over')


# for i in range (5):
#     print (i)
#
#

#
#  for letter in 'python':
#      print(letter)
#
#
# fruits = ['banana','apple','mango']
#
# for fruit in fruits :
#     print(fruit)


# ## 通过index遍历
#
# frutis =['banana','apple','mango']
#
# for index in range (len(frutis)):
#     print(frutis[index])


for num in range(10,20):   # 迭代10 -20 之间的数字
    for i in range(2,num): # 根据因子 迭代
        if num%i:          # 计算第二个因子
            j=num%i

            print('%d 等于 %d * %d ' %(num,i,j))
            break
        else:
            print(num,'是一个质数')