from antlr4 import *
from v1Lexer import v1Lexer
from v1Listener import v1Listener
from v1Parser import v1Parser
import sys



def main():
    inp = FileStream(sys.argv[1])
    lexer = v1Lexer(inp)
    stream = CommonTokenStream(lexer)
    tokens = CommonTokenStream(lexer)
    parser = v1Parser(stream)
    tree = parser.stmt()
    printer = v1Listener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # Print tokens as text (EOF is stripped from the end)


if __name__ == '__main__':
    main()
