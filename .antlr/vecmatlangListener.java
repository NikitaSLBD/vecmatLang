// Generated from d:/Programming/YAPIS/matveclang/vecmatLang/vecmatlang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link vecmatlangParser}.
 */
public interface vecmatlangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(vecmatlangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(vecmatlangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(vecmatlangParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(vecmatlangParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(vecmatlangParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(vecmatlangParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(vecmatlangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(vecmatlangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(vecmatlangParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(vecmatlangParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#classBody}.
	 * @param ctx the parse tree
	 */
	void enterClassBody(vecmatlangParser.ClassBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#classBody}.
	 * @param ctx the parse tree
	 */
	void exitClassBody(vecmatlangParser.ClassBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void enterMethodDecl(vecmatlangParser.MethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void exitMethodDecl(vecmatlangParser.MethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#fieldAppeal}.
	 * @param ctx the parse tree
	 */
	void enterFieldAppeal(vecmatlangParser.FieldAppealContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#fieldAppeal}.
	 * @param ctx the parse tree
	 */
	void exitFieldAppeal(vecmatlangParser.FieldAppealContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#methodAppeal}.
	 * @param ctx the parse tree
	 */
	void enterMethodAppeal(vecmatlangParser.MethodAppealContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#methodAppeal}.
	 * @param ctx the parse tree
	 */
	void exitMethodAppeal(vecmatlangParser.MethodAppealContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(vecmatlangParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(vecmatlangParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(vecmatlangParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(vecmatlangParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(vecmatlangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(vecmatlangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#singleAssignment}.
	 * @param ctx the parse tree
	 */
	void enterSingleAssignment(vecmatlangParser.SingleAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#singleAssignment}.
	 * @param ctx the parse tree
	 */
	void exitSingleAssignment(vecmatlangParser.SingleAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#multipleAssignment}.
	 * @param ctx the parse tree
	 */
	void enterMultipleAssignment(vecmatlangParser.MultipleAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#multipleAssignment}.
	 * @param ctx the parse tree
	 */
	void exitMultipleAssignment(vecmatlangParser.MultipleAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(vecmatlangParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(vecmatlangParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(vecmatlangParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(vecmatlangParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(vecmatlangParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(vecmatlangParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#untilStatement}.
	 * @param ctx the parse tree
	 */
	void enterUntilStatement(vecmatlangParser.UntilStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#untilStatement}.
	 * @param ctx the parse tree
	 */
	void exitUntilStatement(vecmatlangParser.UntilStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(vecmatlangParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(vecmatlangParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteStatement(vecmatlangParser.WriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteStatement(vecmatlangParser.WriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(vecmatlangParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(vecmatlangParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code indexExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIndexExpr(vecmatlangParser.IndexExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code indexExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIndexExpr(vecmatlangParser.IndexExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNotExpr(vecmatlangParser.NotExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNotExpr(vecmatlangParser.NotExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addSubExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAddSubExpr(vecmatlangParser.AddSubExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addSubExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAddSubExpr(vecmatlangParser.AddSubExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpr(vecmatlangParser.PrimaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpr(vecmatlangParser.PrimaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unaryMinusExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinusExpr(vecmatlangParser.UnaryMinusExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unaryMinusExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinusExpr(vecmatlangParser.UnaryMinusExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comparisonExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterComparisonExpr(vecmatlangParser.ComparisonExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparisonExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitComparisonExpr(vecmatlangParser.ComparisonExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulDivExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMulDivExpr(vecmatlangParser.MulDivExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulDivExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMulDivExpr(vecmatlangParser.MulDivExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code binlogicExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBinlogicExpr(vecmatlangParser.BinlogicExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code binlogicExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBinlogicExpr(vecmatlangParser.BinlogicExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code normExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNormExpr(vecmatlangParser.NormExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code normExpr}
	 * labeled alternative in {@link vecmatlangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNormExpr(vecmatlangParser.NormExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(vecmatlangParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(vecmatlangParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code idExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterIdExpr(vecmatlangParser.IdExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code idExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitIdExpr(vecmatlangParser.IdExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(vecmatlangParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(vecmatlangParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code funcCallExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterFuncCallExpr(vecmatlangParser.FuncCallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funcCallExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitFuncCallExpr(vecmatlangParser.FuncCallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code literalExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterLiteralExpr(vecmatlangParser.LiteralExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code literalExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitLiteralExpr(vecmatlangParser.LiteralExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code typeExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterTypeExpr(vecmatlangParser.TypeExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code typeExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitTypeExpr(vecmatlangParser.TypeExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lenExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterLenExpr(vecmatlangParser.LenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lenExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitLenExpr(vecmatlangParser.LenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code readExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterReadExpr(vecmatlangParser.ReadExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code readExpr}
	 * labeled alternative in {@link vecmatlangParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitReadExpr(vecmatlangParser.ReadExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link vecmatlangParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(vecmatlangParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link vecmatlangParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(vecmatlangParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterIntLiteral(vecmatlangParser.IntLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitIntLiteral(vecmatlangParser.IntLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code floatLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterFloatLiteral(vecmatlangParser.FloatLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code floatLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitFloatLiteral(vecmatlangParser.FloatLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code vectorLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterVectorLiteral(vecmatlangParser.VectorLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code vectorLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitVectorLiteral(vecmatlangParser.VectorLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code matrixLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterMatrixLiteral(vecmatlangParser.MatrixLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code matrixLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitMatrixLiteral(vecmatlangParser.MatrixLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code stringLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteral(vecmatlangParser.StringLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code stringLiteral}
	 * labeled alternative in {@link vecmatlangParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteral(vecmatlangParser.StringLiteralContext ctx);
}