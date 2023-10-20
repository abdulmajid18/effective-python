def genSquares(N):
    for i in range(N):
        yield i ** 2


a = genSquares(5)
for i in a:
    print(i, end=" : ")
