from dataclasses import dataclass
from tokens import Token, TokenType

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

    def next_token(self) -> Token:
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
                tok = Token(TokenType.EOF, "")
        self.read_char()
        return tok

def new(input : str):
    l = Lexer(input=input, position=0, read_position=0, ch="")
    l.read_char()
    return l
