def add(*args):
    # <class 'tuple'>
    return sum(args)


def sub(*args):
    '''subtraction'''
    subt = 0
    for n in args:
        subt = subt - n
    return subt


print(sub(1, 2))
