from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    IDENT = "IDENTIFIER"
    INT = "INTEGER"

    ASSIGN = "="
    PLUS = "+"

    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACES = "{"
    RBRACES = "}"

    MINUS= "-"
    BANG= "!"
    ASTERISK = "*"
    SLASH = "/"
    LT = "<"
    GT = ">"

    FUNCTION = "FUNCTION"
    LET = "LET"

    TRUE= "TRUE"
    FALSE= "FALSE"
    IF= "IF"
    ELSE= "ELSE"
    RETURN= "RETURN"

@dataclass
class Token:
    type : TokenType
    literal : str

keywords = {
    "fn" : TokenType.FUNCTION,
    "let" : TokenType.LET,
    "true" : TokenType.TRUE,
    "false" : TokenType.FALSE,
    "if" : TokenType.IF,
    "else" : TokenType.ELSE,
    "return" : TokenType.RETURN
}
