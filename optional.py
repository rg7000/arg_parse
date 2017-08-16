#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("display", help="Display string")
parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")

args=parser.parse_args()
print(args.display)

if args.verbose:
    print("Verbose mode turned ON")
