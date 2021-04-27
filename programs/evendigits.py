import evencheck


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


num_1 = int(input("Enter a lower bound: "))
num_2 = int(input("Enter an upper bound: "))
print(even_digits(num_1, num_2))
