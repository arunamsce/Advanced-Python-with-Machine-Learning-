def make_multiplier(factor):

    def multiplier(number):
        # factor is a variable declared in outer function
        return number * factor

    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# Line 9: double = make_multiplier(2)
# Creates a closure where factor = 2
# Returns a multiplier function that will multiply any number by 2

# Line 10: triple = make_multiplier(3)
# Creates a separate closure where factor = 3
# Returns a different multiplier function that will multiply any number by 3
