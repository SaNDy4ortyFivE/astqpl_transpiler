from antlr4 import *
from rulesLexer import rulesLexer
from rulesListener import rulesListener
from rulesParser import rulesParser
import sys



def main():
    inp = FileStream(sys.argv[1])
    lexer = rulesLexer(inp)
    stream = CommonTokenStream(lexer)
    tokens = CommonTokenStream(lexer)
    parser = rulesParser(stream)
    tree = parser.stmt()
    printer = rulesListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # Print tokens as text (EOF is stripped from the end)


if __name__ == '__main__':
    main()
