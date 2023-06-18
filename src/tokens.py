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

    FUNCTION = "FUNCTION"
    LET = "LET"

@dataclass
class Token:
    type : TokenType
    literal : str

keywords = {
    "fn" : TokenType.FUNCTION,
    "let" : TokenType.LET
}
