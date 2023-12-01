from random import randint

while True:
    length = int(input("Enter the amount of numbers: "))
    begin = int(input("Enter the Beginning Number: "))
    end = int(input("Enter the Ending Number: "))

    # show an error if distance is less than length 
    if end - begin < length:
        print(f"The distance between two numbers is less than {length}")
    else:
        break

randNum = []
while len(randNum) < length:

    # make random numbers
    num = randint(begin, end)
    if num not in randNum:
        # add numbers to lists
        randNum.append(num)

# print random numbers
for numbers in randNum:
    print(numbers)
