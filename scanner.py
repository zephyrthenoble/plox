import error
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
token_types = tokens.split()

class Token(object):
    def __init__(self, lexeme, token_type, literal, line_num):
        assert token_type in token_types
        self.lexeme = str(lexeme)
        self.type = token_type
        self.literal = literal
        self.line = int(line_num)
    def __str__(self):
        return "%s %s %s"%(self.type, self.lexeme, self.literal)
######
class Scanner(object):
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
    def isAtEnd(self):
        return self.current >= len(self.source)
    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken();

        self.tokens.append(Token("","EOF", None, self.line))
        return self.tokens
    
    def scanToken(self):
        c = self.advance()

        if c is "(":
            self.addTokenType("LEFT_PAREN")
        elif c is ")":
            self.addTokenType("RIGHT_PAREN")
        elif c is "{":
            self.addTokenType("LEFT_BRACE")
        elif c is "}":
            self.addTokenType("RIGHT_BRACE")
        elif c is ",":
            self.addTokenType("COMMA")
        elif c is ".":
            self.addTokenType("DOT")
        elif c is "-":
            self.addTokenType("MINUS")
        elif c is "+":
            self.addTokenType("PLUS")
        elif c is ";":
            self.addTokenType("SEMICOLON")
        elif c is "*":
            self.addTokenType("STAR")
        elif c is "!":
            if self.match("="):
                self.addTokenType("BANG_EQUAL")
            else:
                self.addTokenType("BANG")
        # TODO =:
        elif c is "=":
            if self.match("="):
                self.addTokenType("EQUAL_EQUAL")
            else:
                self.addTokenType("EQUAL")
        elif c is "<":
            if self.match("="):
                self.addTokenType("LESS_EQUAL")
            else:
                self.addTokenType("LESS")
        elif c is ">":
            if self.match("="):
                self.addTokenType("GREATER_EQUAL")
            else:
                self.addTokenType("GREATER")
        elif c is "/":
            # comment
            if self.match("/"):
                while self.peek() != '\n' and not self.isAtEnd():
                    self.advance()
        elif c is '"':
            self.string()
        elif c.isdigit():
            self.number()
        elif c in ' \r\t':
            pass
        elif c in '\n':
            self.line += 1
        else:
            error.report(self.line, "Unexpected character", repr(c))
            
    def number(self):
        while self.peek().isdigit():
            self.advance()
        if self.peek() is '.' and self.peekNext().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
        self.addToken("NUMBER", float(self.source[self.start:self.current]))

    def string(self):
        #iterate until we find another "
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() is '\n':
                self.line += 1
            self.advance()

        if self.isAtEnd():
            error.exception(self.line, "Unterminated string.")
        self.advance()
        value = self.source[self.start + 1:self.current - 1]
        self.addToken("STRING", value)

    def peek(self):
        """Returns next character without advancing"""
        if self.current >= len(self.source):
            return '\0'
        return self.source[self.current]

    def peekNext(self):
        """Returns the next next character without advancing"""
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def advance(self):
        """Returns next character while consuming"""
        self.current += 1
        return self.source[self.current - 1]

    def match(self, expected):
        """Advance if we match the expecte value (c='!', check for '=')"""
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def addTokenType(self, mytype):
        self.addToken(mytype, None)

    def addToken(self, mytype, literal):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(text, mytype, literal, self.line))

