def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print(number, first)
    if len(str_number) < 2:
        return number
    return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
print(get_multiplied_digits(5021367))