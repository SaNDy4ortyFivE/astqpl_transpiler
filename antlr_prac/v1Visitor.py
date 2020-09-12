# Generated from v1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .v1Parser import v1Parser
else:
    from v1Parser import v1Parser

# This class defines a complete generic visitor for a parse tree produced by v1Parser.

class v1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by v1Parser#stmt.
    def visitStmt(self, ctx:v1Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by v1Parser#line.
    def visitLine(self, ctx:v1Parser.LineContext):
        return self.visitChildren(ctx)

del v1Parser
