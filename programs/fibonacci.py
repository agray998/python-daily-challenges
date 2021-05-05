def fib(n):
    x = int(n)
    if x >= 0:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        return fib(x-1) + fib(x-2)
    else:
        return "Negative inputs not accepted!"

