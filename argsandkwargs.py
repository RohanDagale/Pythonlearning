def function(*args):
    print(type(args))
    if(len(args) ==3):

        print('my name is ', args[0], "and the age " , args[1], "and rollno", args[2])
    else:
        print('my name is ', args[0], "and the age " , args[1])

lis = ['harry', 22, 10]
def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
def master(noraml, *args, **kwargs):
    print(noraml)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

marklist = {'harry' : 90, 'loki':50, 'rohan':80, 'harsh' : 90, 'bali':50, 'think':80}
# printmarks(**marklist)
# lis = ['harry', 18, 2080]


# function(*lis)
master('noraml arg', *lis, **marklist)