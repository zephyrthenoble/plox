#!/usr/bin/env python
import sys
import os
from io import out, err

from scanner import Scanner
hadError = False
def main(args):
    if len(args) > 1:
        out("Usage: plox [script]\n")
    elif len(args) == 1:
        runFile(args)
    else:
        runPrompt()

def runPrompt():
    while True:
        hadError = False
        run(raw_input("> "))

def runFile(args):
    filename = args[0]
    if not os.path.isfile(filename):
        err("%s is not a file" % (filename))
    with open(filename, "rb") as f:
        run(f.read())
    if hadError:
        sys.exit(15)

def run(data):
    tokens = Scanner(data).scanTokens()
    for t in tokens:
        print t
if __name__ == "__main__":
    main(sys.argv[1:])
