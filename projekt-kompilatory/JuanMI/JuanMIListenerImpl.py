from JuanMI import JuanMIListener, JuanMIParser, JuanMILexer
import antlr4 as antlr
from antlr4.tree import Tree as t


class JuanMIListenerImpl(JuanMIListener.JuanMIListener):

    def __init__(self):

        self.code = ""
        self.indent_level = 0
        self.complement_for = False

    def addIndent(self):
        indent_string = ""
        for i in range(0, self.indent_level):
            indent_string += "\t"
        return indent_string

    def deleteIndent(self, i):
        self.code = self.code[:-i]


    def enterVar_type(self, ctx: JuanMIParser.JuanMIParser.Var_typeContext):
        pass
        # Exit a parse tree produced by JuanMIParser#var_type.


    def exitVar_type(self, ctx: JuanMIParser.JuanMIParser.Var_typeContext):
        pass
        # Enter a parse tree produced by JuanMIParser#value.

    def enterListValue(self, ctx:JuanMIParser.JuanMIParser.ListValueContext):
        pass

    # Exit a parse tree produced by JuanMIParser#listValue.
    def exitListValue(self, ctx:JuanMIParser.JuanMIParser.ListValueContext):
        pass


    # Enter a parse tree produced by JuanMIParser#listExpression.
    def enterListExpression(self, ctx:JuanMIParser.JuanMIParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#listExpression.
    def exitListExpression(self, ctx:JuanMIParser.JuanMIParser.ListExpressionContext):
        pass

    def enterValue(self, ctx: JuanMIParser.JuanMIParser.ValueContext):
        pass
        # Exit a parse tree produced by JuanMIParser#value.


    def exitValue(self, ctx: JuanMIParser.JuanMIParser.ValueContext):
        pass
        # Enter a parse tree produced by JuanMIParser#varDeclaration.

    def enterVarDeclaration(self, ctx: JuanMIParser.JuanMIParser.VarDeclarationContext):
        pass
        # Exit a parse tree produced by JuanMIParser#varDeclaration.


    def exitVarDeclaration(self, ctx: JuanMIParser.JuanMIParser.VarDeclarationContext):
        pass
        # Enter a parse tree produced by JuanMIParser#varAssignment.


    def enterVarAssignment(self, ctx: JuanMIParser.JuanMIParser.VarAssignmentContext):
        pass
        # Exit a parse tree produced by JuanMIParser#varAssignment.


    def exitVarAssignment(self, ctx: JuanMIParser.JuanMIParser.VarAssignmentContext):
        pass

    def enterArithmeticExpression(self, ctx: JuanMIParser.JuanMIParser.ArithmeticExpressionContext):
        pass

        # Exit a parse tree produced by JuanMIParser#arithmeticExpression.

    def exitArithmeticExpression(self, ctx: JuanMIParser.JuanMIParser.ArithmeticExpressionContext):
        pass

        # Enter a parse tree produced by JuanMIParser#stringExpression.

    def enterStringExpression(self, ctx: JuanMIParser.JuanMIParser.StringExpressionContext):
        pass

        # Exit a parse tree produced by JuanMIParser#stringExpression.

    def exitStringExpression(self, ctx: JuanMIParser.JuanMIParser.StringExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#booleanExpression.

    def enterBooleanExpression(self, ctx: JuanMIParser.JuanMIParser.BooleanExpressionContext):
        pass

        # Exit a parse tree produced by JuanMIParser#booleanExpression.

    def exitBooleanExpression(self, ctx: JuanMIParser.JuanMIParser.BooleanExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#printExpression.

    def enterPrintExpression(self, ctx: JuanMIParser.JuanMIParser.PrintExpressionContext):
        pass
        # Exit a parse tree produced by JuanMIParser#printExpression.

    def exitPrintExpression(self, ctx: JuanMIParser.JuanMIParser.PrintExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#expression.

    def enterExpression(self, ctx: JuanMIParser.JuanMIParser.ExpressionContext):
        pass

        # Exit a parse tree produced by JuanMIParser#expression.
    def exitExpression(self, ctx: JuanMIParser.JuanMIParser.ExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#code.

    def enterCode(self, ctx: JuanMIParser.JuanMIParser.CodeContext):
        pass
        # Exit a parse tree produced by JuanMIParser#code.

    def exitCode(self, ctx: JuanMIParser.JuanMIParser.CodeContext):
        pass
        # Enter a parse tree produced by JuanMIParser#program.

    def enterProgram(self, ctx: JuanMIParser.JuanMIParser.ProgramContext):
        pass
        # Exit a parse tree produced by JuanMIParser#program.

    def exitProgram(self, ctx: JuanMIParser.JuanMIParser.ProgramContext):
        pass
        # Enter a parse tree produced by JuanMIParser#forLoopExpression.

    def enterForLoopExpression(self, ctx: JuanMIParser.JuanMIParser.ForLoopExpressionContext):
        pass
        # Exit a parse tree produced by JuanMIParser#forLoopExpression.

    def exitForLoopExpression(self, ctx: JuanMIParser.JuanMIParser.ForLoopExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#whileLoopExpression.

    def enterWhileLoopExpression(self, ctx: JuanMIParser.JuanMIParser.WhileLoopExpressionContext):
        pass
        # Exit a parse tree produced by JuanMIParser#whileLoopExpression.

    def exitWhileLoopExpression(self, ctx: JuanMIParser.JuanMIParser.WhileLoopExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#loopCode.

    def enterLoopCode(self, ctx: JuanMIParser.JuanMIParser.LoopCodeContext):
        pass
        # Exit a parse tree produced by JuanMIParser#loopCode.

    def exitLoopCode(self, ctx: JuanMIParser.JuanMIParser.LoopCodeContext):
        pass
        # Enter a parse tree produced by JuanMIParser#conditionalExpression.

    def enterConditionalExpression(self, ctx: JuanMIParser.JuanMIParser.ConditionalExpressionContext):
        pass
        # Exit a parse tree produced by JuanMIParser#conditionalExpression.

    def exitConditionalExpression(self, ctx: JuanMIParser.JuanMIParser.ConditionalExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#elifExpression.

    def enterElifExpression(self, ctx: JuanMIParser.JuanMIParser.ElifExpressionContext):
        pass
        # Exit a parse tree produced by JuanMIParser#elifExpression.

    def exitElifExpression(self, ctx: JuanMIParser.JuanMIParser.ElifExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#elseExpression.

    def enterElseExpression(self, ctx: JuanMIParser.JuanMIParser.ElseExpressionContext):
        pass
        # Exit a parse tree produced by JuanMIParser#elseExpression.

    def exitElseExpression(self, ctx: JuanMIParser.JuanMIParser.ElseExpressionContext):
        pass
        # Enter a parse tree produced by JuanMIParser#functionDeclaration.

    def enterFunctionDeclaration(self, ctx: JuanMIParser.JuanMIParser.FunctionDeclarationContext):
        pass
        # Exit a parse tree produced by JuanMIParser#functionDeclaration.

    def exitFunctionDeclaration(self, ctx: JuanMIParser.JuanMIParser.FunctionDeclarationContext):
        pass
        # Enter a parse tree produced by JuanMIParser#argList.

    def enterArgList(self, ctx: JuanMIParser.JuanMIParser.ArgListContext):
        pass
        # Exit a parse tree produced by JuanMIParser#argList.

    def exitArgList(self, ctx: JuanMIParser.JuanMIParser.ArgListContext):
        pass
        # Enter a parse tree produced by JuanMIParser#fullArgList.

    def enterFullArgList(self, ctx: JuanMIParser.JuanMIParser.FullArgListContext):
        pass
        # Exit a parse tree produced by JuanMIParser#fullArgList.

    def exitFullArgList(self, ctx: JuanMIParser.JuanMIParser.FullArgListContext):
        pass
        # Enter a parse tree produced by JuanMIParser#functionCall.

    def enterFunctionCall(self, ctx: JuanMIParser.JuanMIParser.FunctionCallContext):
        pass
        # Exit a parse tree produced by JuanMIParser#functionCall.

    def exitFunctionCall(self, ctx: JuanMIParser.JuanMIParser.FunctionCallContext):
        pass
        # Enter a parse tree produced by JuanMIParser#valueList.

    def enterValueList(self, ctx: JuanMIParser.JuanMIParser.ValueListContext):
        pass
        # Exit a parse tree produced by JuanMIParser#valueList.

    def exitValueList(self, ctx: JuanMIParser.JuanMIParser.ValueListContext):
        pass
        # Enter a parse tree produced by JuanMIParser#fullValueList.

    def enterFullValueList(self, ctx: JuanMIParser.JuanMIParser.FullValueListContext):
        pass
        # Exit a parse tree produced by JuanMIParser#fullValueList.

    def exitFullValueList(self, ctx: JuanMIParser.JuanMIParser.FullValueListContext):
        pass

    def visitTerminal(self, node:t.TerminalNode):

        ttype = node.getSymbol().type
        parser = JuanMIParser.JuanMIParser

        immutable_values = [parser.TKN_VAR_ID, parser.TKN_NUMBER_VAL, parser.TKN_STRING_VAL, parser.TKN_LSQUARE,
                            parser.TKN_RSQUARE, parser.TKN_LBRACKET, parser.TKN_RBRACKET]
        immutable_ops = [parser.TKN_PLUS, parser.TKN_MINUS, parser.TKN_MUL, parser.TKN_DIV, parser.TKN_G, parser.TKN_L,
                         parser.TKN_GEQ, parser.TKN_LEQ]
        tokens = {
            parser.TKN_DOTS: ":\n",
            parser.TKN_END_LINE: "\n",
            parser.TKN_POW: " ** ",
            parser.TKN_CONCAT: " + ",
            parser.TKN_ASSIGN: " = ",
            parser.TKN_EQ: " == ",
            parser.TKN_NEQ: " != ",
            parser.TKN_COMMA: ", ",
            parser.TKN_NOT: " not ",
            parser.TKN_AND: " and ",
            parser.TKN_OR: " or ",
            parser.TKN_TRUE: "True",
            parser.TKN_FALSE: "False",
            parser.TKN_WHILE: "while ",
            parser.TKN_PRINT: "print",
            parser.TKN_FOR: "for ",
            parser.TKN_FROM: " in range (",
            parser.TKN_TO: ", ",
            parser.TKN_BREAK: "break",
            parser.TKN_CONTINUE: "continue",
            parser.TKN_RETURN: "return ",
            parser.TKN_FUNCTION: "def ",
            parser.TKN_IF: "if ",
            parser.TKN_ELIF: "elif ",
            parser.TKN_ELSE: "else"
        }

        if ttype in immutable_ops:
            self.code += " " + node.getText() + " "
        if ttype in immutable_values:
            self.code += node.getText()
        if ttype in tokens.keys():

            if ttype == parser.TKN_DOTS and self.complement_for:
                self.complement_for = False
                self.code += ")"
            if ttype == parser.TKN_ELIF or ttype == parser.TKN_ELSE:
                self.indent_level -= 1
                self.deleteIndent(1)

            self.code += tokens[ttype]

            if ttype == parser.TKN_FOR:
                self.complement_for = True
            if ttype == parser.TKN_DOTS:
                self.indent_level += 1
                self.code += self.addIndent()

            if ttype == parser.TKN_END_LINE:
                self.code += self.addIndent()
        if ttype == parser.TKN_END:
            self.indent_level -= 1
        if ttype == parser.TKN_COMMENT:
            self.code += node.getText() + "\n"




