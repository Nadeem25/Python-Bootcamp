# try and except and Finally
try:
    value = 1/0
    #a = b
except ZeroDivisionError as zero_divide_exc:
    print(f"Please enter the denominator value greater than 0")
except Exception as exception:
    print(f"Error message: {exception}")
finally:
    print('Inside print block')


# try, else and except
try:
    value = 1/0
    #a = b
except ZeroDivisionError as zero_divide_exc:
    print(f"Please enter the denominator value greater than 0")
else:
    print(f"Inside else block")


try:
    value = 1/0
    #a = b
except ZeroDivisionError as zero_divide_exc:
    print(f"Please enter the denominator value greater than 0")
except Exception as exception:
    print(f"Error message: {exception}")
else:
    print(f"Inside else block")
finally:
    print('Inside print block')