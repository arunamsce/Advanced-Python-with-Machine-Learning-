
def fun(x):
    print(f"x :{x}")

    def fun1(y):
        nonlocal x
        print(f"y :{y}")
        print(f"before Inside fun1 x: {x}")
        x += 100
        print(f"after Inside fun1 x: {x}")


    return fun1

ref = fun(100)
ref(200)

print("-" * 60)

x = 100

# Section 1: nonlocal keyword (lines 2-16)
# fun(100) is called with parameter x=100, prints "x :100"
# Returns fun1 which has a closure over x
# ref(200) calls fun1(y=200)
# nonlocal x allows fun1 to modify the outer function's x variable
# x starts at 100, gets incremented by 100, becomes 200

# Section 2: global keyword (lines 20-29)
# Global variable x = 100 is created
# fun2() uses global x to access and modify the global variable
# Initially prints global x as 100
# Modifies it to 500
# After function call, global x remains 500 (persists)
def fun2():
    global x
    print("hello world")
    print(f"x :{x}")
    x = 500         # local variable
    print(f"x :{x}")

fun2()
print(f"Afer the function call x: {x}")

print("-" * 60)
# variables declared inside the function cannot be accessed outside the function
# they are local variable with lexical scope


# Section 3: local variable scope (lines 42-51)
# fun3() declares local variable z = 250
# z is only accessible within fun3()
# After function call, z is not accessible (NameError)
def fun3():
    print("hello world")
    z = 250
    print(f"z :{z}")

fun3()
print(f"z :{z}")


# Key Concepts Demonstrated
# nonlocal: Allows nested functions to modify variables from enclosing (non-global) scopes
# global: Allows functions to modify variables at the module/global scope
# Local scope: Variables declared inside functions are only accessible within that function