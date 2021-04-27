from programs import evencheck


def even_digits(x, y):
    evendigits = ""
    for num in range(x, y+1):
        strng = str(num)
        for d in strng:
            if not evencheck.check_even(int(d)):
                break
            else:
                pass
        else:
            evendigits += f"{strng},"
    return evendigits


