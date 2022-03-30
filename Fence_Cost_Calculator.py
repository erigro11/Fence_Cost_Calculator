
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

print()
print("***** Fence Cost Calculator *****")


keep_going = ""
while keep_going == "":
    print()
    print("What is the size of the")
    print("area you are fenceing?")
    print()
    width = num_check("width: ")
    length = num_check("length: ")
    cost = num_check("Cost per meter: ")

    perimeter = 2 * (width + length)

    total = perimeter * cost

    print()
    print("the perimeter of the area you are fencing is {} meters".format(perimeter))
    print("the cost of the fence is ${} square units".format(total))
    print()

    keep_going = input("press <enter> to keep going or any other key to quit")

print()
print("Thanks for using the fence cost calculator")