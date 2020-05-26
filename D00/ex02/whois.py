import sys

arg = sys.argv

if len (arg) < 2:
    quit();
if len (arg) > 2 or arg[1].isdigit() == False:
    print("ERROR")
    quit();

number = int(arg[1])
if number == 0:
    print("I'm Zero")
elif (number % 2) == 0:
    print("I'm Even")
else:
    print("I'm Odd")

