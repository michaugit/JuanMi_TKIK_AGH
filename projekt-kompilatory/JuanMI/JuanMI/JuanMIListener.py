# Generated from JuanMI.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JuanMIParser import JuanMIParser
else:
    from JuanMIParser import JuanMIParser

# This class defines a complete listener for a parse tree produced by JuanMIParser.
class JuanMIListener(ParseTreeListener):

    # Enter a parse tree produced by JuanMIParser#var_type.
    def enterVar_type(self, ctx:JuanMIParser.Var_typeContext):
        pass

    # Exit a parse tree produced by JuanMIParser#var_type.
    def exitVar_type(self, ctx:JuanMIParser.Var_typeContext):
        pass


    # Enter a parse tree produced by JuanMIParser#value.
    def enterValue(self, ctx:JuanMIParser.ValueContext):
        pass

    # Exit a parse tree produced by JuanMIParser#value.
    def exitValue(self, ctx:JuanMIParser.ValueContext):
        pass


    # Enter a parse tree produced by JuanMIParser#varDeclaration.
    def enterVarDeclaration(self, ctx:JuanMIParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by JuanMIParser#varDeclaration.
    def exitVarDeclaration(self, ctx:JuanMIParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by JuanMIParser#varAssignment.
    def enterVarAssignment(self, ctx:JuanMIParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by JuanMIParser#varAssignment.
    def exitVarAssignment(self, ctx:JuanMIParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by JuanMIParser#listValue.
    def enterListValue(self, ctx:JuanMIParser.ListValueContext):
        pass

    # Exit a parse tree produced by JuanMIParser#listValue.
    def exitListValue(self, ctx:JuanMIParser.ListValueContext):
        pass


    # Enter a parse tree produced by JuanMIParser#listExpression.
    def enterListExpression(self, ctx:JuanMIParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#listExpression.
    def exitListExpression(self, ctx:JuanMIParser.ListExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#valueList.
    def enterValueList(self, ctx:JuanMIParser.ValueListContext):
        pass

    # Exit a parse tree produced by JuanMIParser#valueList.
    def exitValueList(self, ctx:JuanMIParser.ValueListContext):
        pass


    # Enter a parse tree produced by JuanMIParser#fullValueList.
    def enterFullValueList(self, ctx:JuanMIParser.FullValueListContext):
        pass

    # Exit a parse tree produced by JuanMIParser#fullValueList.
    def exitFullValueList(self, ctx:JuanMIParser.FullValueListContext):
        pass


    # Enter a parse tree produced by JuanMIParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:JuanMIParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:JuanMIParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#stringExpression.
    def enterStringExpression(self, ctx:JuanMIParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#stringExpression.
    def exitStringExpression(self, ctx:JuanMIParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#booleanExpression.
    def enterBooleanExpression(self, ctx:JuanMIParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#booleanExpression.
    def exitBooleanExpression(self, ctx:JuanMIParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#printExpression.
    def enterPrintExpression(self, ctx:JuanMIParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#printExpression.
    def exitPrintExpression(self, ctx:JuanMIParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#expression.
    def enterExpression(self, ctx:JuanMIParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#expression.
    def exitExpression(self, ctx:JuanMIParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#code.
    def enterCode(self, ctx:JuanMIParser.CodeContext):
        pass

    # Exit a parse tree produced by JuanMIParser#code.
    def exitCode(self, ctx:JuanMIParser.CodeContext):
        pass


    # Enter a parse tree produced by JuanMIParser#program.
    def enterProgram(self, ctx:JuanMIParser.ProgramContext):
        pass

    # Exit a parse tree produced by JuanMIParser#program.
    def exitProgram(self, ctx:JuanMIParser.ProgramContext):
        pass


    # Enter a parse tree produced by JuanMIParser#forLoopExpression.
    def enterForLoopExpression(self, ctx:JuanMIParser.ForLoopExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#forLoopExpression.
    def exitForLoopExpression(self, ctx:JuanMIParser.ForLoopExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#whileLoopExpression.
    def enterWhileLoopExpression(self, ctx:JuanMIParser.WhileLoopExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#whileLoopExpression.
    def exitWhileLoopExpression(self, ctx:JuanMIParser.WhileLoopExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#loopCode.
    def enterLoopCode(self, ctx:JuanMIParser.LoopCodeContext):
        pass

    # Exit a parse tree produced by JuanMIParser#loopCode.
    def exitLoopCode(self, ctx:JuanMIParser.LoopCodeContext):
        pass


    # Enter a parse tree produced by JuanMIParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:JuanMIParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:JuanMIParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#elifExpression.
    def enterElifExpression(self, ctx:JuanMIParser.ElifExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#elifExpression.
    def exitElifExpression(self, ctx:JuanMIParser.ElifExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#elseExpression.
    def enterElseExpression(self, ctx:JuanMIParser.ElseExpressionContext):
        pass

    # Exit a parse tree produced by JuanMIParser#elseExpression.
    def exitElseExpression(self, ctx:JuanMIParser.ElseExpressionContext):
        pass


    # Enter a parse tree produced by JuanMIParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:JuanMIParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by JuanMIParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:JuanMIParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by JuanMIParser#argList.
    def enterArgList(self, ctx:JuanMIParser.ArgListContext):
        pass

    # Exit a parse tree produced by JuanMIParser#argList.
    def exitArgList(self, ctx:JuanMIParser.ArgListContext):
        pass


    # Enter a parse tree produced by JuanMIParser#fullArgList.
    def enterFullArgList(self, ctx:JuanMIParser.FullArgListContext):
        pass

    # Exit a parse tree produced by JuanMIParser#fullArgList.
    def exitFullArgList(self, ctx:JuanMIParser.FullArgListContext):
        pass


    # Enter a parse tree produced by JuanMIParser#functionCall.
    def enterFunctionCall(self, ctx:JuanMIParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by JuanMIParser#functionCall.
    def exitFunctionCall(self, ctx:JuanMIParser.FunctionCallContext):
        pass


