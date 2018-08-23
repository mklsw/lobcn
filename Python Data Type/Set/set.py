# S = {11,22,33,44}
#
# print(type(S))
#
# s1 = {'a','b','c','d','e'}
#
# print(s1)
#
# s2 =set('hello') # 使用set() 接收一个字符串
#
# print(s2)
#
# print(type(s2))
#
# s4 = "hello"  # 这个是字符串
#
# print(s4)
#
# print(type(s4))
#
# s5 = set(['.mp3','.mp4','.avi']) # 使用set () 接收一个list
#
# print(s5)
#
# print(type(s5))
#
#
# print(help(set))


a = {1,2,3,4,5}

b = {1,2,3,4,5,6}

print(a&b)  #  & 并集

print(a|b)  #  | 合集

print(a.issubset(b))  # a 是否是b的子集

print(a.issuperset(b))  # a 是否是b的超集

print(b.issuperset(a))  # b是否是a的超集

