# number = 90
#
# running = True
#
# while running:
#
#     guess = int(input('Enter an integer:'))
#
#     if guess == number:
#         print('Congratulations, You guessed it!')
#
#         running = False
#
#     elif guess < number:
#         print('No , it is a little higher than that.')
#
#     else :
#
#         print('No, it is a little lower than that.')
#
# else:
#
#     print('The while loop is over.')
#
# print('Done.')
#

# 费式数列

a , b = 0,1

while a < 10000:
    print(a,end=',')

    a,b = b, a+b



