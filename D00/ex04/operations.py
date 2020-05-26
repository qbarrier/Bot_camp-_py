import sys

arg = sys.argv

if len(sys.argv) == 3 and arg[1].isdecimal() == True and arg[2].isdecimal() == True:
    arg[1] = int(arg[1])
    arg[2] = int(arg[2])
    print("Sum:\t\t" , arg[1]+arg[2])
    print("Difference:\t" , arg[1]-arg[2])
    print("Product:\t" , arg[1]*arg[2])
    if arg[2] != 0:
        print("Quotient:\t" , arg[1]/arg[2])
        print("Remainder:\t" , arg[1]%arg[2])
    else:
        print("Quotient:\t ERROR (div by zero)")
        print("Remainder:\t ERROR (modulo by zero)")
        
    quit()
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n")
elif len(sys.argv) > 1 and len(sys.argv) < 3:
    print("InputError: Not enough arguments\n")
elif len(sys.argv) != 1:
    print("Input Error: only numbers\n")
print("Usage: python operations.py <number1> <number2>")
print("Example:")
print("\tpython operation.py 10 3")

