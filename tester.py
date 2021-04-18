from antlr4 import *
from rulesLexer import rulesLexer
from rulesListener import rulesListener
from rulesParser import rulesParser
import sys
import time
import handleNode
import asyncio

def main():
    start_time = time.perf_counter()
    inp = FileStream(sys.argv[1])
    lexer = rulesLexer(inp)
    stream = CommonTokenStream(lexer)
    tokens = CommonTokenStream(lexer)
    parser = rulesParser(stream)
    tree = parser.stmt()
    printer = rulesListener()
    walker = ParseTreeWalker()
    transpilation_start = time.perf_counter()
    walker.walk(printer, tree)
    finish_time = time.perf_counter()
    # Print tokens as text (EOF is stripped from the end)
    ##result analysis
    print("Setup time:{0:.5f}".format(transpilation_start-start_time))
    print("Transpilation time:{0:.5f}".format(finish_time-transpilation_start))
    print("Total time:{0:.5f}".format(finish_time-start_time))

    return handleNode.getLines()


if __name__ == '__main__':
    main()
