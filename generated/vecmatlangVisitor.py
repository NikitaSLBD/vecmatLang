# Generated from d:/Programming/YAPIS/matveclang/vecmatLang/vecmatlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .vecmatlangParser import vecmatlangParser
else:
    from vecmatlangParser import vecmatlangParser

# This class defines a complete generic visitor for a parse tree produced by vecmatlangParser.

class vecmatlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by vecmatlangParser#program.
    def visitProgram(self, ctx:vecmatlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#functionDecl.
    def visitFunctionDecl(self, ctx:vecmatlangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#parameterList.
    def visitParameterList(self, ctx:vecmatlangParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#block.
    def visitBlock(self, ctx:vecmatlangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#classDecl.
    def visitClassDecl(self, ctx:vecmatlangParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#classBody.
    def visitClassBody(self, ctx:vecmatlangParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#methodDecl.
    def visitMethodDecl(self, ctx:vecmatlangParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#fieldAppeal.
    def visitFieldAppeal(self, ctx:vecmatlangParser.FieldAppealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#methodAppeal.
    def visitMethodAppeal(self, ctx:vecmatlangParser.MethodAppealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#statement.
    def visitStatement(self, ctx:vecmatlangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#var.
    def visitVar(self, ctx:vecmatlangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#assignment.
    def visitAssignment(self, ctx:vecmatlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#singleAssignment.
    def visitSingleAssignment(self, ctx:vecmatlangParser.SingleAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#multipleAssignment.
    def visitMultipleAssignment(self, ctx:vecmatlangParser.MultipleAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#ifStatement.
    def visitIfStatement(self, ctx:vecmatlangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#forStatement.
    def visitForStatement(self, ctx:vecmatlangParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#whileStatement.
    def visitWhileStatement(self, ctx:vecmatlangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#untilStatement.
    def visitUntilStatement(self, ctx:vecmatlangParser.UntilStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#returnStatement.
    def visitReturnStatement(self, ctx:vecmatlangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#writeStatement.
    def visitWriteStatement(self, ctx:vecmatlangParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#readStatement.
    def visitReadStatement(self, ctx:vecmatlangParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#indexExpr.
    def visitIndexExpr(self, ctx:vecmatlangParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#notExpr.
    def visitNotExpr(self, ctx:vecmatlangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#addSubExpr.
    def visitAddSubExpr(self, ctx:vecmatlangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:vecmatlangParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:vecmatlangParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:vecmatlangParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:vecmatlangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#binlogicExpr.
    def visitBinlogicExpr(self, ctx:vecmatlangParser.BinlogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#normExpr.
    def visitNormExpr(self, ctx:vecmatlangParser.NormExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#type.
    def visitType(self, ctx:vecmatlangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#idExpr.
    def visitIdExpr(self, ctx:vecmatlangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#parenExpr.
    def visitParenExpr(self, ctx:vecmatlangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:vecmatlangParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#literalExpr.
    def visitLiteralExpr(self, ctx:vecmatlangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#typeExpr.
    def visitTypeExpr(self, ctx:vecmatlangParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#lenExpr.
    def visitLenExpr(self, ctx:vecmatlangParser.LenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#readExpr.
    def visitReadExpr(self, ctx:vecmatlangParser.ReadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#argumentList.
    def visitArgumentList(self, ctx:vecmatlangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#intLiteral.
    def visitIntLiteral(self, ctx:vecmatlangParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#floatLiteral.
    def visitFloatLiteral(self, ctx:vecmatlangParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#vectorLiteral.
    def visitVectorLiteral(self, ctx:vecmatlangParser.VectorLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#matrixLiteral.
    def visitMatrixLiteral(self, ctx:vecmatlangParser.MatrixLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by vecmatlangParser#stringLiteral.
    def visitStringLiteral(self, ctx:vecmatlangParser.StringLiteralContext):
        return self.visitChildren(ctx)



del vecmatlangParser