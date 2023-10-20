var = 99


def local():
    var = 0


def glob1():
    global var
    var += 1


def glob2():
    var = 0
    from . import thismod
    thismod.var += 1


def glob3():
    var = 0
    import sys
    glob = sys.modules['other.thismod']
    glob.var += 1


def test():
    x = 1
    a = x
    x = 20
    print(a)
    # print(var)
    # local();
    # glob1();
    # glob2();
    # glob3()
    # print(var)
