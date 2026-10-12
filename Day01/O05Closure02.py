def outerFun(info): # HOF - Higher Order Function
    inf = "Mr." + info

    def innerFun():
        print(inf)

    return innerFun

outerFun("Rohit")
print("-" * 60)

print(outerFun.__name__)
print(outerFun("Rohit").__name__)
print("-" * 60)

outerFun("Rohit")()
print("-" * 60)

inref = outerFun("Rohit")
inref()

# Key Concepts
# Closure: The inner function innerFun "remembers" the value of inf from its enclosing scope even after outerFun has finished executing
# Higher-Order Function: A function that returns another function
# Lexical Scoping: Inner functions have access to variables from outer functions in their scope chain
