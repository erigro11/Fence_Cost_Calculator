
# checks input is a number more than zero
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

# **** Main routine starts here ****

print()
print("***** Fence Cost Calculator *****")


# program loops so we can do more than one calculation per session
keep_going = ""
while keep_going == "":


    # Quetion
    print()
    print("What is the size of the")
    print("area you are fenceing?")
    print()

    3
    # get width,lenght and cost, checking they are numbers more than zero
    width = num_check("width: ")
    length = num_check("length: ")
    cost = num_check("Cost per meter: ")

# Calculate perimeter and total 
    perimeter = 2 * (width + length)

    total = perimeter * cost

# Output results to user
    print()
    print("the perimeter of the area you are fencing is {} meters".format(perimeter))
    print("the cost of the fence is ${} square units".format(total))
    print()

    keep_going = input("press <enter> to keep going or any other key to quit")

print()
print("Thanks for using the fence cost calculator")