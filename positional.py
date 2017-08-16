#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
#===The arguments need to specified in the same order as they are added here=====#
 
parser.add_argument("display", help="display the string you use here") #argument name display
parser.add_argument("square", help="Square the element", type=int)

args = parser.parse_args() #parses the args specified plus stores them in args

print(args.display) 	#.display tells that the arguments related to display i.e. 1st positional arg
print(args.square**2)	#.square helps prog know that this line is to be performed on arguments of square i.e. 2nd positional args
