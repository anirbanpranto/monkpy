from tokens import TokenType
from lexer import new

def test_tokenizer():
    input = "=+(){},;"
    expected_type = "expected_type"
    expected_literal = "expected_literal"
    tests = [
        {
            expected_type : TokenType.ASSIGN,
            expected_literal : "="
        },
        {
            expected_type : TokenType.PLUS,
            expected_literal : "+"
        },
        {
            expected_type : TokenType.LPAREN,
            expected_literal : "("
        },
        {
            expected_type : TokenType.RPAREN,
            expected_literal : ")"
        },
        {
            expected_type : TokenType.LBRACES,
            expected_literal : "{"
        },
        {
            expected_type : TokenType.RBRACES,
            expected_literal : "}"
        },
        {
            expected_type : TokenType.COMMA,
            expected_literal : ","
        },
        {
            expected_type : TokenType.SEMICOLON, 
            expected_literal : ";"
        }
    ]
    l = new(input)
    for i in range(len(tests)):
        t = l.next_token()
        assert(t.type == tests[i]["expected_type"])
