def is_prime(x):
    for n in range(2, (x//2)+1):
        if x % n == 0:
            return False
            break
        else:
            pass
    else:
        return True


def check_even(y):
    primefacts = {i for i in range(2, y+1) if is_prime(i) == True and y % i == 0}
    return y == 0 or 2 in primefacts

