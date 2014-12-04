import re
import collections

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self._expr()

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected' + toktype)

    # def _expr(self):
    #     "expr ::= term { ('+'|'-') term }*"
    #     exprval = self._term()
    #     while self._accept('PLUS') or self._accept('MINUS'):
    #         op = self.tok.type
    #         right = self._term()
    #         if op == 'PLUS':
    #             exprval += right
    #         elif op == 'MINUS':
    #             exprval -= right
    #     return exprval
    def _expr(self):
        exprval = self._term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self._term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    # def _term(self):
    #     "term ::= factor {('*'|'/') factor}*"
    #     termval = self._factor()
    #     while self._accept('TIMES') or self._accept('DIVIDE'):
    #         op = self.tok.type
    #         right = self._factor()
    #         if op == 'TIMES':
    #             termval *= right
    #         elif op == 'DIVIDE':
    #             termval /= right
    #     return termval
    def _term(self):
        termval = self._factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self._factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def _factor(self):
        "factor ::= NUM | (expr)"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            expval = self._expr()
            self._expect('RPAREN')
            return expval
        else:
            raise SyntaxError('Expected number or laparen')

if __name__ == '__main__':
    e = ExpressionEvaluator()
    print(e.parse('(2 + 2) * 4 / 3'))
    # ('/', ('*', ('+', 2, 2), 4), 3)