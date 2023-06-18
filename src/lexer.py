from dataclasses import dataclass
from typing import Optional
from tokens import Token, TokenType, keywords

def lookup_ident(ident) -> Optional[TokenType]:
    return keywords.get(ident)

@dataclass
class Lexer:
    input : str
    position : int
    read_position : int
    ch : str
    
    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = "\0"
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def next_token(self) -> Optional[Token]:
        self.skip_white_space()
        tok = None
        match self.ch:
            case "=":
                tok = Token(TokenType.ASSIGN, self.ch)
            case ",":
                tok = Token(TokenType.COMMA, self.ch)
            case ";":
                tok = Token(TokenType.SEMICOLON, self.ch)
            case "(":
                tok = Token(TokenType.LPAREN, self.ch)
            case ")":
                tok = Token(TokenType.RPAREN, self.ch)
            case "{":
                tok = Token(TokenType.LBRACES, self.ch)
            case "}":
                tok = Token(TokenType.RBRACES, self.ch)
            case "+":
                tok = Token(TokenType.PLUS, self.ch)
            case "\0":
                tok = Token(TokenType.EOF, "")
            case other:
                if self.is_letter(self.ch):
                    tok = Token(TokenType.IDENT, "")
                    tok.literal = self.read_identifier()
                    tok.type = lookup_ident(tok.literal) or TokenType.IDENT
                    return tok
                elif self.is_digit(self.ch):
                    tok = Token(TokenType.INT, "")
                    tok.literal = self.read_number()
                    return tok
                else:
                    tok = Token(TokenType.ILLEGAL, self.ch)
        self.read_char()
        return tok
    
    def is_digit(self, ch):
        return ('0' <= ch and ch <= '9')

    def is_letter(self, ch):
        return 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z' or ch == '_'
    
    def skip_white_space(self):
        while self.ch.isspace(): 
            self.read_char()
        

    def read_identifier(self):
        position = self.position
        while(self.is_letter(self.ch)):
            self.read_char()
        return self.input[position : self.position]
    
    def read_number(self):
        position = self.position
        while(self.is_digit(self.ch)):
            self.read_char()
        return self.input[position : self.position]

def new(input : str):
    l = Lexer(input=input, position=0, read_position=0, ch="")
    l.read_char()
    return l
