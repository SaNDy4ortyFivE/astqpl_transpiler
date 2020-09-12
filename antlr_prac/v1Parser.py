# Generated from v1.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\4\5\4)\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\5\t;\n\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\6\fF\n\f\r\f\16\fG\3\f\2\2\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\6\3\3\3\3\3\2\4\5\4\2\n\n\16\16")
        buf.write("\3\2\13\r\2F\2\33\3\2\2\2\4#\3\2\2\2\6(\3\2\2\2\b*\3\2")
        buf.write("\2\2\n-\3\2\2\2\f\61\3\2\2\2\16\66\3\2\2\2\20:\3\2\2\2")
        buf.write("\22<\3\2\2\2\24A\3\2\2\2\26C\3\2\2\2\30\31\5\4\3\2\31")
        buf.write("\32\t\2\2\2\32\34\3\2\2\2\33\30\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\33\3\2\2\2\35\36\3\2\2\2\36\3\3\2\2\2\37$\5\6\4\2")
        buf.write(" $\5\20\t\2!$\5\26\f\2\"$\7\t\2\2#\37\3\2\2\2# \3\2\2")
        buf.write("\2#!\3\2\2\2#\"\3\2\2\2$\5\3\2\2\2%)\5\b\5\2&)\5\n\6\2")
        buf.write("\')\5\f\7\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2)\7\3\2\2\2")
        buf.write("*+\5\16\b\2+,\7\n\2\2,\t\3\2\2\2-.\7\n\2\2./\7\13\2\2")
        buf.write("/\60\7\16\2\2\60\13\3\2\2\2\61\62\5\16\b\2\62\63\7\n\2")
        buf.write("\2\63\64\7\13\2\2\64\65\7\16\2\2\65\r\3\2\2\2\66\67\t")
        buf.write("\3\2\2\67\17\3\2\2\28;\5\22\n\29;\7\b\2\2:8\3\2\2\2:9")
        buf.write("\3\2\2\2;\21\3\2\2\2<=\7\7\2\2=>\t\4\2\2>?\5\24\13\2?")
        buf.write("@\t\4\2\2@\23\3\2\2\2AB\t\5\2\2B\25\3\2\2\2CE\7\6\2\2")
        buf.write("DF\7\n\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\27")
        buf.write("\3\2\2\2\7\35#(:G")
        return buf.getvalue()


class v1Parser ( Parser ):

    grammarFileName = "v1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTEGER", "NUMBER", "OUTPUT", 
                      "IF", "ELSE", "END", "VARIABLE", "EQUAL", "GREATER", 
                      "LESS", "NUMB", "TEXT", "WHITESPACE", "NEWLINE" ]

    RULE_stmt = 0
    RULE_line = 1
    RULE_v_init = 2
    RULE_decl = 3
    RULE_assign = 4
    RULE_both = 5
    RULE_d_type = 6
    RULE_conditional = 7
    RULE_r_if = 8
    RULE_relation = 9
    RULE_output = 10

    ruleNames =  [ "stmt", "line", "v_init", "decl", "assign", "both", "d_type", 
                   "conditional", "r_if", "relation", "output" ]

    EOF = Token.EOF
    T__0=1
    INTEGER=2
    NUMBER=3
    OUTPUT=4
    IF=5
    ELSE=6
    END=7
    VARIABLE=8
    EQUAL=9
    GREATER=10
    LESS=11
    NUMB=12
    TEXT=13
    WHITESPACE=14
    NEWLINE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(v1Parser.LineContext)
            else:
                return self.getTypedRuleContext(v1Parser.LineContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(v1Parser.EOF)
            else:
                return self.getToken(v1Parser.EOF, i)

        def getRuleIndex(self):
            return v1Parser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = v1Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.line()
                self.state = 23
                _la = self._input.LA(1)
                if not(_la==v1Parser.EOF or _la==v1Parser.T__0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << v1Parser.INTEGER) | (1 << v1Parser.NUMBER) | (1 << v1Parser.OUTPUT) | (1 << v1Parser.IF) | (1 << v1Parser.ELSE) | (1 << v1Parser.END) | (1 << v1Parser.VARIABLE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_init(self):
            return self.getTypedRuleContext(v1Parser.V_initContext,0)


        def conditional(self):
            return self.getTypedRuleContext(v1Parser.ConditionalContext,0)


        def output(self):
            return self.getTypedRuleContext(v1Parser.OutputContext,0)


        def END(self):
            return self.getToken(v1Parser.END, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = v1Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [v1Parser.INTEGER, v1Parser.NUMBER, v1Parser.VARIABLE]:
                self.state = 29
                self.v_init()
                pass
            elif token in [v1Parser.IF, v1Parser.ELSE]:
                self.state = 30
                self.conditional()
                pass
            elif token in [v1Parser.OUTPUT]:
                self.state = 31
                self.output()
                pass
            elif token in [v1Parser.END]:
                self.state = 32
                self.match(v1Parser.END)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(v1Parser.DeclContext,0)


        def assign(self):
            return self.getTypedRuleContext(v1Parser.AssignContext,0)


        def both(self):
            return self.getTypedRuleContext(v1Parser.BothContext,0)


        def getRuleIndex(self):
            return v1Parser.RULE_v_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_init" ):
                listener.enterV_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_init" ):
                listener.exitV_init(self)




    def v_init(self):

        localctx = v1Parser.V_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_v_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 35
                self.decl()
                pass

            elif la_ == 2:
                self.state = 36
                self.assign()
                pass

            elif la_ == 3:
                self.state = 37
                self.both()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def d_type(self):
            return self.getTypedRuleContext(v1Parser.D_typeContext,0)


        def VARIABLE(self):
            return self.getToken(v1Parser.VARIABLE, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = v1Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.d_type()
            self.state = 41
            self.match(v1Parser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(v1Parser.VARIABLE, 0)

        def EQUAL(self):
            return self.getToken(v1Parser.EQUAL, 0)

        def NUMB(self):
            return self.getToken(v1Parser.NUMB, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = v1Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(v1Parser.VARIABLE)
            self.state = 44
            self.match(v1Parser.EQUAL)
            self.state = 45
            self.match(v1Parser.NUMB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BothContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def d_type(self):
            return self.getTypedRuleContext(v1Parser.D_typeContext,0)


        def VARIABLE(self):
            return self.getToken(v1Parser.VARIABLE, 0)

        def EQUAL(self):
            return self.getToken(v1Parser.EQUAL, 0)

        def NUMB(self):
            return self.getToken(v1Parser.NUMB, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_both

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoth" ):
                listener.enterBoth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoth" ):
                listener.exitBoth(self)




    def both(self):

        localctx = v1Parser.BothContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_both)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.d_type()
            self.state = 48
            self.match(v1Parser.VARIABLE)
            self.state = 49
            self.match(v1Parser.EQUAL)
            self.state = 50
            self.match(v1Parser.NUMB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class D_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(v1Parser.INTEGER, 0)

        def NUMBER(self):
            return self.getToken(v1Parser.NUMBER, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_d_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD_type" ):
                listener.enterD_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD_type" ):
                listener.exitD_type(self)




    def d_type(self):

        localctx = v1Parser.D_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_d_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==v1Parser.INTEGER or _la==v1Parser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_if(self):
            return self.getTypedRuleContext(v1Parser.R_ifContext,0)


        def ELSE(self):
            return self.getToken(v1Parser.ELSE, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = v1Parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [v1Parser.IF]:
                self.state = 54
                self.r_if()
                pass
            elif token in [v1Parser.ELSE]:
                self.state = 55
                self.match(v1Parser.ELSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(v1Parser.IF, 0)

        def relation(self):
            return self.getTypedRuleContext(v1Parser.RelationContext,0)


        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(v1Parser.VARIABLE)
            else:
                return self.getToken(v1Parser.VARIABLE, i)

        def NUMB(self, i:int=None):
            if i is None:
                return self.getTokens(v1Parser.NUMB)
            else:
                return self.getToken(v1Parser.NUMB, i)

        def getRuleIndex(self):
            return v1Parser.RULE_r_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_if" ):
                listener.enterR_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_if" ):
                listener.exitR_if(self)




    def r_if(self):

        localctx = v1Parser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(v1Parser.IF)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==v1Parser.VARIABLE or _la==v1Parser.NUMB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 60
            self.relation()
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==v1Parser.VARIABLE or _la==v1Parser.NUMB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER(self):
            return self.getToken(v1Parser.GREATER, 0)

        def LESS(self):
            return self.getToken(v1Parser.LESS, 0)

        def EQUAL(self):
            return self.getToken(v1Parser.EQUAL, 0)

        def getRuleIndex(self):
            return v1Parser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)




    def relation(self):

        localctx = v1Parser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << v1Parser.EQUAL) | (1 << v1Parser.GREATER) | (1 << v1Parser.LESS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(v1Parser.OUTPUT, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(v1Parser.VARIABLE)
            else:
                return self.getToken(v1Parser.VARIABLE, i)

        def getRuleIndex(self):
            return v1Parser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)




    def output(self):

        localctx = v1Parser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(v1Parser.OUTPUT)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.match(v1Parser.VARIABLE)
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==v1Parser.VARIABLE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





