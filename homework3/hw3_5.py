number: int = int(input("please enter a random number: "))
if number % 5 == 0 and number % 3 == 0:
    print("fizz buzz")
elif number % 5 == 0 or number % 3 == 0:
    print("fizz")
else:
    print("invalid number")