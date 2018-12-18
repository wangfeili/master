# from time import ctime,sleep
#
#
# def test(func):
#     def wrappedFunc():
#         print('[%s] %s() called' %(
#             ctime(),func.__name__))
#         return func()
#     return wrappedFunc
#
#
# @test
# def foo():
#     pass
#
# foo()
# sleep(4)
#
# for i in range(2):
#     sleep(1)
#     foo()

# def aa(arg1,arg2='defaultB',**theRest):
#     print('formal arg 1:',arg1)
#     print('formal arg 2:',arg2)
#     for eaacX in theRest.keys():
#         print('another arg:',eaacX)
#
# aa(23,d=333)

# true = lambda :True
# print(true())

from random import randint

allNums = []
for eachNum in range(9):
    allNums.append(randint(1,99))

print(allNums)
a =list(filter(lambda n: n % 2, allNums))
'''
python3在这里需要加一个list()函数才能print filter返回的list
'''
print(a)



