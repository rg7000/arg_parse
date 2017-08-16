#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="Squares the given number", type=int)
parser.add_argument("-v", "--verbose", help="Increases verbosity of output", choices=[0,1,2], type=int)

args=parser.parse_args()
answer = args.square**2

if args.verbose == 2:
    print("{}^2 is equal to {}".format(args.square, answer))
elif args.verbose == 1:
    print("{}^2 = {}".format(args.square, answer))
else:
    print(answer)
