def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
factorial(5)
#print(f"__name__ == '{__name__}'")