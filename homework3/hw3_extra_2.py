friends = 4
slices: int = int(input("Please enter the amount of pizza slices: "))

if slices % friends == 0:
    each_gets = slices / friends
    print(f"Each friend got {each_gets} slices")
else:
    each_gets = slices // friends
    leftovers = slices % friends
    print(f"Each friend got {each_gets} slices, with {leftovers} slices leftover")



friends: int = int(input("please enter how many friends came: "))
slices: int = int(input("please enter the amount of pizza slices ordered: "))
if slices % friends == 0:
    each_gets = slices / friends
    print(f"Each friend got {each_gets} slices")
else:
    each_gets = slices // friends
    leftovers = slices % friends
    print(f"Each friend got {each_gets} slices, with {leftovers} slices leftover")