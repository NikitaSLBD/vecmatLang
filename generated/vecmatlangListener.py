# Generated from d:/Programming/YAPIS/matveclang/vecmatLang/vecmatlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .vecmatlangParser import vecmatlangParser
else:
    from vecmatlangParser import vecmatlangParser

# This class defines a complete listener for a parse tree produced by vecmatlangParser.
class vecmatlangListener(ParseTreeListener):

    # Enter a parse tree produced by vecmatlangParser#program.
    def enterProgram(self, ctx:vecmatlangParser.ProgramContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#program.
    def exitProgram(self, ctx:vecmatlangParser.ProgramContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#functionDecl.
    def enterFunctionDecl(self, ctx:vecmatlangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#functionDecl.
    def exitFunctionDecl(self, ctx:vecmatlangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#parameterList.
    def enterParameterList(self, ctx:vecmatlangParser.ParameterListContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#parameterList.
    def exitParameterList(self, ctx:vecmatlangParser.ParameterListContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#block.
    def enterBlock(self, ctx:vecmatlangParser.BlockContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#block.
    def exitBlock(self, ctx:vecmatlangParser.BlockContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#classDecl.
    def enterClassDecl(self, ctx:vecmatlangParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#classDecl.
    def exitClassDecl(self, ctx:vecmatlangParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#classBody.
    def enterClassBody(self, ctx:vecmatlangParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#classBody.
    def exitClassBody(self, ctx:vecmatlangParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#methodDecl.
    def enterMethodDecl(self, ctx:vecmatlangParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#methodDecl.
    def exitMethodDecl(self, ctx:vecmatlangParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#fieldAppeal.
    def enterFieldAppeal(self, ctx:vecmatlangParser.FieldAppealContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#fieldAppeal.
    def exitFieldAppeal(self, ctx:vecmatlangParser.FieldAppealContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#methodAppeal.
    def enterMethodAppeal(self, ctx:vecmatlangParser.MethodAppealContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#methodAppeal.
    def exitMethodAppeal(self, ctx:vecmatlangParser.MethodAppealContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#statement.
    def enterStatement(self, ctx:vecmatlangParser.StatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#statement.
    def exitStatement(self, ctx:vecmatlangParser.StatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#var.
    def enterVar(self, ctx:vecmatlangParser.VarContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#var.
    def exitVar(self, ctx:vecmatlangParser.VarContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#assignment.
    def enterAssignment(self, ctx:vecmatlangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#assignment.
    def exitAssignment(self, ctx:vecmatlangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#singleAssignment.
    def enterSingleAssignment(self, ctx:vecmatlangParser.SingleAssignmentContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#singleAssignment.
    def exitSingleAssignment(self, ctx:vecmatlangParser.SingleAssignmentContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#multipleAssignment.
    def enterMultipleAssignment(self, ctx:vecmatlangParser.MultipleAssignmentContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#multipleAssignment.
    def exitMultipleAssignment(self, ctx:vecmatlangParser.MultipleAssignmentContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#ifStatement.
    def enterIfStatement(self, ctx:vecmatlangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#ifStatement.
    def exitIfStatement(self, ctx:vecmatlangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#forStatement.
    def enterForStatement(self, ctx:vecmatlangParser.ForStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#forStatement.
    def exitForStatement(self, ctx:vecmatlangParser.ForStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#whileStatement.
    def enterWhileStatement(self, ctx:vecmatlangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#whileStatement.
    def exitWhileStatement(self, ctx:vecmatlangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#untilStatement.
    def enterUntilStatement(self, ctx:vecmatlangParser.UntilStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#untilStatement.
    def exitUntilStatement(self, ctx:vecmatlangParser.UntilStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#returnStatement.
    def enterReturnStatement(self, ctx:vecmatlangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#returnStatement.
    def exitReturnStatement(self, ctx:vecmatlangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#writeStatement.
    def enterWriteStatement(self, ctx:vecmatlangParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#writeStatement.
    def exitWriteStatement(self, ctx:vecmatlangParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#readStatement.
    def enterReadStatement(self, ctx:vecmatlangParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#readStatement.
    def exitReadStatement(self, ctx:vecmatlangParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#indexExpr.
    def enterIndexExpr(self, ctx:vecmatlangParser.IndexExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#indexExpr.
    def exitIndexExpr(self, ctx:vecmatlangParser.IndexExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#notExpr.
    def enterNotExpr(self, ctx:vecmatlangParser.NotExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#notExpr.
    def exitNotExpr(self, ctx:vecmatlangParser.NotExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#addSubExpr.
    def enterAddSubExpr(self, ctx:vecmatlangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#addSubExpr.
    def exitAddSubExpr(self, ctx:vecmatlangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:vecmatlangParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:vecmatlangParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:vecmatlangParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:vecmatlangParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:vecmatlangParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:vecmatlangParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:vecmatlangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:vecmatlangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#binlogicExpr.
    def enterBinlogicExpr(self, ctx:vecmatlangParser.BinlogicExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#binlogicExpr.
    def exitBinlogicExpr(self, ctx:vecmatlangParser.BinlogicExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#normExpr.
    def enterNormExpr(self, ctx:vecmatlangParser.NormExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#normExpr.
    def exitNormExpr(self, ctx:vecmatlangParser.NormExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#type.
    def enterType(self, ctx:vecmatlangParser.TypeContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#type.
    def exitType(self, ctx:vecmatlangParser.TypeContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#idExpr.
    def enterIdExpr(self, ctx:vecmatlangParser.IdExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#idExpr.
    def exitIdExpr(self, ctx:vecmatlangParser.IdExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#parenExpr.
    def enterParenExpr(self, ctx:vecmatlangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#parenExpr.
    def exitParenExpr(self, ctx:vecmatlangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:vecmatlangParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:vecmatlangParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#literalExpr.
    def enterLiteralExpr(self, ctx:vecmatlangParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#literalExpr.
    def exitLiteralExpr(self, ctx:vecmatlangParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#typeExpr.
    def enterTypeExpr(self, ctx:vecmatlangParser.TypeExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#typeExpr.
    def exitTypeExpr(self, ctx:vecmatlangParser.TypeExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#lenExpr.
    def enterLenExpr(self, ctx:vecmatlangParser.LenExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#lenExpr.
    def exitLenExpr(self, ctx:vecmatlangParser.LenExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#readExpr.
    def enterReadExpr(self, ctx:vecmatlangParser.ReadExprContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#readExpr.
    def exitReadExpr(self, ctx:vecmatlangParser.ReadExprContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#argumentList.
    def enterArgumentList(self, ctx:vecmatlangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#argumentList.
    def exitArgumentList(self, ctx:vecmatlangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#intLiteral.
    def enterIntLiteral(self, ctx:vecmatlangParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#intLiteral.
    def exitIntLiteral(self, ctx:vecmatlangParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#floatLiteral.
    def enterFloatLiteral(self, ctx:vecmatlangParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#floatLiteral.
    def exitFloatLiteral(self, ctx:vecmatlangParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#vectorLiteral.
    def enterVectorLiteral(self, ctx:vecmatlangParser.VectorLiteralContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#vectorLiteral.
    def exitVectorLiteral(self, ctx:vecmatlangParser.VectorLiteralContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#matrixLiteral.
    def enterMatrixLiteral(self, ctx:vecmatlangParser.MatrixLiteralContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#matrixLiteral.
    def exitMatrixLiteral(self, ctx:vecmatlangParser.MatrixLiteralContext):
        pass


    # Enter a parse tree produced by vecmatlangParser#stringLiteral.
    def enterStringLiteral(self, ctx:vecmatlangParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by vecmatlangParser#stringLiteral.
    def exitStringLiteral(self, ctx:vecmatlangParser.StringLiteralContext):
        pass



del vecmatlangParser