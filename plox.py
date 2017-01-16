#!/usr/bin/env python
import sys
import os

### Tokenization ###
# Single-character tokens.
tokens = ""
tokens += "LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE "
tokens += "COMMA DOT MINUS PLUS SEMICOLON SLASH STAR "

# One or two character tokens.
tokens += "BANG BANG_EQUAL "
tokens += "EQUAL EQUAL_EQUAL "
tokens += "GREATER GREATER_EQUAL "
tokens += "LESS LESS_EQUAL "

# Literals.
tokens += "IDENTIFIER STRING NUMBER "

# Keywords.
tokens += "AND CLASS ELSE FALSE FUN FOR IF NIL OR "
tokens += "PRINT RETURN SUPER THIS TRUE VAR WHILE "
tokens += "EOF "
token_types = {}
for i, e in enumerate(enums.split()):
    token_types[e] = i

class Token(object):
    def __init__(self, lexeme, token_type, literal, line_num):
        assert token_type in token_types.tokens.keys()
        self.lexeme = str(lexeme)
        self.type = token_type
        self.literal = literal
        self.line = int(line_num)
    def __str__(self):
        return "%s %s %s"%(self.type, self.lexeme, self.literal)
######

### Exceptions ###
hadError = False
def exception(line, message):
    report(message, line)
def report(message, line, where=""):
    err("[line %d] Error %s: %s" % (message, line, where))
    hadError = True
#######

### Output and input ###
def err(msg):
    sys.stderr.write(str(msg))

def out(msg):
    sys.stdout.write(str(msg))
#######

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
    tokens = data.split()
    for t in tokens:
        print t
if __name__ == "__main__":
    main(sys.argv[1:])
