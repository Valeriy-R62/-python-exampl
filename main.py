def test(*params):
    print(params)


test(2, False, 'крот')
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)


print(faktorial(9))
