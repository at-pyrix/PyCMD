from ast import arguments
import sys

def argparse(args: list=sys.argv):
    argument = ''
    flags = []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            argument = arg
    return argument, flags

arguments, flags = argparse()

print(arguments)