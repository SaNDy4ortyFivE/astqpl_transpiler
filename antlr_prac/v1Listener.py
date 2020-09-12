#custom import
import handleNode

# Generated from v1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .v1Parser import v1Parser
else:
    from v1Parser import v1Parser

# This class defines a complete listener for a parse tree produced by v1Parser.
class v1Listener(ParseTreeListener):

    # Enter a parse tree produced by v1Parser#stmt.
    def enterStmt(self, ctx:v1Parser.StmtContext):
        print('entering stmt')
        pass

    # Exit a parse tree produced by v1Parser#stmt.
    def exitStmt(self, ctx:v1Parser.StmtContext):
        print('exiting stmt')
        handleNode.printTree()
        pass


    # Enter a parse tree produced by v1Parser#line.
    def enterLine(self, ctx:v1Parser.LineContext):
        print('entering line')
        if not ctx.END() is None:
            handleNode.addNodeEnd()
        pass

    # Exit a parse tree produced by v1Parser#line.
    def exitLine(self, ctx:v1Parser.LineContext):
        print('exiting line')
        pass


    # Enter a parse tree produced by v1Parser#v_init.
    def enterV_init(self, ctx:v1Parser.V_initContext):
        print('entering v_init')
        pass

    # Exit a parse tree produced by v1Parser#v_init.
    def exitV_init(self, ctx:v1Parser.V_initContext):
        print('exiting v_init')
        pass


    # Enter a parse tree produced by v1Parser#decl.
    def enterDecl(self, ctx:v1Parser.DeclContext):
        print('entering decl')
        var = ctx.VARIABLE().getText()
        i = ctx.d_type().INTEGER()
        n = ctx.d_type().NUMBER()
        d_type = i.getText() if not i is None else n.getText()
        handleNode.addDecl(d_type, var)
        pass

    # Exit a parse tree produced by v1Parser#decl.
    def exitDecl(self, ctx:v1Parser.DeclContext):
        print('exiting decl')
        pass


    # Enter a parse tree produced by v1Parser#assign.
    def enterAssign(self, ctx:v1Parser.AssignContext):
        print('entering assign')
        var = ctx.VARIABLE().getText()
        value = ctx.NUMB().getText()
        handleNode.addAssign(var, value)
        pass

    # Exit a parse tree produced by v1Parser#assign.
    def exitAssign(self, ctx:v1Parser.AssignContext):
        print('exiting assgn')
        pass


    # Enter a parse tree produced by v1Parser#both.
    def enterBoth(self, ctx:v1Parser.BothContext):
        print('entering both')
        i = ctx.d_type().INTEGER()
        n = ctx.d_type().NUMBER()
        d_type = i.getText() if not i is None else n.getText()
        var = ctx.VARIABLE().getText()
        val = ctx.NUMB().getText()
        handleNode.addBoth(d_type,var,val)
        pass

    # Exit a parse tree produced by v1Parser#both.
    def exitBoth(self, ctx:v1Parser.BothContext):
        print('exiting both')
        pass


    # Enter a parse tree produced by v1Parser#d_type.
    def enterD_type(self, ctx:v1Parser.D_typeContext):
        print('entering d_type')
        pass

    # Exit a parse tree produced by v1Parser#d_type.
    def exitD_type(self, ctx:v1Parser.D_typeContext):
        print('exiting d_type')
        pass


    # Enter a parse tree produced by v1Parser#conditional.
    def enterConditional(self, ctx:v1Parser.ConditionalContext):
        print('entering conditional')
        pass

    # Exit a parse tree produced by v1Parser#conditional.
    def exitConditional(self, ctx:v1Parser.ConditionalContext):
        print('entering conditional')
        if not ctx.ELSE() is None:
            handleNode.addNodeElse()
        pass


    # Enter a parse tree produced by v1Parser#r_if.
    def enterR_if(self, ctx:v1Parser.R_ifContext):
        print('entering r_if')
        val1,val2=0,0
        rel = ctx.relation().GREATER()
        if rel is None:
            rel = ctx.relation().LESS()
        if rel is None:
            rel = ctx.relation().EQUAL()
        if len(ctx.VARIABLE())==2:
            val1 = ctx.VARIABLE(0)
            val2 = ctx.VARIABLE(1)
        elif len(ctx.NUMB())==2:
            val1 = ctx.NUMB(0)
            val2 = ctx.NUMB(1)
        else:
            varb = ctx.VARIABLE(0).getSymbol()
            numb = ctx.NUMB(0).getSymbol()
            ##check indices
            if varb.tokenIndex < numb.tokenIndex:
                val1 = ctx.VARIABLE(0)
                val2 = ctx.NUMB(0)
            else:
                val1 = ctx.NUMB(0)
                val2 = ctx.VARIABLE(0)
        handleNode.addIf(val1.getText(),val2.getText(),rel.getText())
        pass

    # Exit a parse tree produced by v1Parser#r_if.
    def exitR_if(self, ctx:v1Parser.R_ifContext):
        print('exiting r_if')
        pass


    # Enter a parse tree produced by v1Parser#relation.
    def enterRelation(self, ctx:v1Parser.RelationContext):
        print('entering relation')
        pass

    # Exit a parse tree produced by v1Parser#relation.
    def exitRelation(self, ctx:v1Parser.RelationContext):
        print('exiting relation')
        pass


    # Enter a parse tree produced by v1Parser#output.
    def enterOutput(self, ctx:v1Parser.OutputContext):
        print('Entering output')
        handleNode.addNodeOutput(ctx.VARIABLE()[-1].getText())
        pass

    # Exit a parse tree produced by v1Parser#output.
    def exitOutput(self, ctx:v1Parser.OutputContext):
        print('Exiting output')
        pass



del v1Parser
