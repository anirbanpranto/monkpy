from tokens import TokenType
from lexer import new

def test_next_token():
    input = """
    let five = 5;
    let ten = 10;
    let add = fn(x, y){
        x + y;
    };
    let result = add(five, ten);
    """
    tests = [
            TokenType.LET, 
            TokenType.IDENT, 
            TokenType.ASSIGN,
            TokenType.INT,
            TokenType.SEMICOLON,
            TokenType.LET,
            TokenType.IDENT,
            TokenType.ASSIGN,
            TokenType.INT, 
            TokenType.SEMICOLON,
            TokenType.LET, 
            TokenType.IDENT, 
            TokenType.ASSIGN, 
            TokenType.FUNCTION, 
            TokenType.LPAREN, 
            TokenType.IDENT, 
            TokenType.COMMA, 
            TokenType.IDENT, 
            TokenType.RPAREN, 
            TokenType.LBRACES, 
            TokenType.IDENT, 
            TokenType.PLUS,
            TokenType.IDENT,
            TokenType.SEMICOLON,
            TokenType.RBRACES,
            TokenType.SEMICOLON,
            TokenType.LET,
            TokenType.IDENT,
            TokenType.ASSIGN,
            TokenType.IDENT, 
            TokenType.LPAREN,
            TokenType.IDENT,  
            TokenType.COMMA,
            TokenType.IDENT,
            TokenType.RPAREN,
            TokenType.SEMICOLON,
            TokenType.EOF,
    ]
    l = new(input)
    for i in range(len(tests)):
        t = l.next_token()
        if(t):
            assert(t.type == tests[i])

test_next_token()

