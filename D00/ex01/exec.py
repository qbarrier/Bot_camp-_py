import sys

arg = sys.argv
del arg[0]

arg.reverse();
for index, val in enumerate(arg, 0):
    arg[index] = arg[index].swapcase();
    arg[index] = arg[index][::-1]

print(*arg)
