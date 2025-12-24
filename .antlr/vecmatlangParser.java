// Generated from d:/Programming/YAPIS/matveclang/vecmatLang/vecmatlang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class vecmatlangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, WS=20, NEWLINE=21, TAB=22, INDENT=23, DEDENT=24, IF=25, 
		THEN=26, ELSE=27, FOR=28, IN=29, WHILE=30, UNTIL=31, FUNC=32, RETURN=33, 
		WRITE=34, READ=35, RANGE=36, CLASS=37, METHOD=38, CONTINUE=39, BREAK=40, 
		LEN=41, AND=42, OR=43, NOT=44, INT_TYPE=45, FLOAT_TYPE=46, VECTOR=47, 
		MATRIX=48, ID=49, INT=50, FLOAT=51, STRING=52, COMMENT=53;
	public static final int
		RULE_program = 0, RULE_functionDecl = 1, RULE_parameterList = 2, RULE_block = 3, 
		RULE_classDecl = 4, RULE_classBody = 5, RULE_methodDecl = 6, RULE_fieldAppeal = 7, 
		RULE_methodAppeal = 8, RULE_statement = 9, RULE_var = 10, RULE_assignment = 11, 
		RULE_singleAssignment = 12, RULE_multipleAssignment = 13, RULE_ifStatement = 14, 
		RULE_forStatement = 15, RULE_whileStatement = 16, RULE_untilStatement = 17, 
		RULE_returnStatement = 18, RULE_writeStatement = 19, RULE_readStatement = 20, 
		RULE_expression = 21, RULE_type = 22, RULE_primaryExpression = 23, RULE_argumentList = 24, 
		RULE_literal = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "functionDecl", "parameterList", "block", "classDecl", "classBody", 
			"methodDecl", "fieldAppeal", "methodAppeal", "statement", "var", "assignment", 
			"singleAssignment", "multipleAssignment", "ifStatement", "forStatement", 
			"whileStatement", "untilStatement", "returnStatement", "writeStatement", 
			"readStatement", "expression", "type", "primaryExpression", "argumentList", 
			"literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "':'", "','", "'.'", "'['", "']'", "'='", "'|'", 
			"'-'", "'*'", "'/'", "'+'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
			null, null, "'\\t'", "'<<INDENT>>'", "'<<DEDENT>>'", "'if'", "'then'", 
			"'else'", "'for'", "'in'", "'while'", "'until'", "'func'", "'return'", 
			"'write'", "'read'", "'range'", "'class'", "'method'", "'continue'", 
			"'exit'", "'len'", "'&&'", "'||'", "'!'", "'int'", "'float'", "'vector'", 
			"'matrix'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "WS", "NEWLINE", "TAB", 
			"INDENT", "DEDENT", "IF", "THEN", "ELSE", "FOR", "IN", "WHILE", "UNTIL", 
			"FUNC", "RETURN", "WRITE", "READ", "RANGE", "CLASS", "METHOD", "CONTINUE", 
			"BREAK", "LEN", "AND", "OR", "NOT", "INT_TYPE", "FLOAT_TYPE", "VECTOR", 
			"MATRIX", "ID", "INT", "FLOAT", "STRING", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "vecmatlang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public vecmatlangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(vecmatlangParser.EOF, 0); }
		public List<FunctionDeclContext> functionDecl() {
			return getRuleContexts(FunctionDeclContext.class);
		}
		public FunctionDeclContext functionDecl(int i) {
			return getRuleContext(FunctionDeclContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNC) {
				{
				{
				setState(52);
				functionDecl();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8993656453203522L) != 0)) {
				{
				{
				setState(58);
				statement();
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(vecmatlangParser.FUNC, 0); }
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterFunctionDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitFunctionDecl(this);
		}
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(FUNC);
			setState(67);
			match(ID);
			setState(68);
			match(T__0);
			setState(70);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(69);
				parameterList();
				}
			}

			setState(72);
			match(T__1);
			setState(73);
			match(T__2);
			setState(74);
			match(NEWLINE);
			setState(75);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterListContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(vecmatlangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(vecmatlangParser.ID, i);
		}
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterParameterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitParameterList(this);
		}
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(ID);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(78);
				match(T__3);
				setState(79);
				match(ID);
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode INDENT() { return getToken(vecmatlangParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(vecmatlangParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(INDENT);
			setState(87); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(86);
				statement();
				}
				}
				setState(89); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 8993656453203522L) != 0) );
			setState(91);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassDeclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(vecmatlangParser.CLASS, 0); }
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public ClassBodyContext classBody() {
			return getRuleContext(ClassBodyContext.class,0);
		}
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public ClassDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterClassDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitClassDecl(this);
		}
	}

	public final ClassDeclContext classDecl() throws RecognitionException {
		ClassDeclContext _localctx = new ClassDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_classDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(CLASS);
			setState(94);
			match(ID);
			setState(95);
			match(T__0);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(96);
				parameterList();
				}
			}

			setState(99);
			match(T__1);
			setState(100);
			match(T__2);
			setState(101);
			match(NEWLINE);
			setState(102);
			classBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassBodyContext extends ParserRuleContext {
		public TerminalNode INDENT() { return getToken(vecmatlangParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(vecmatlangParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<MethodDeclContext> methodDecl() {
			return getRuleContexts(MethodDeclContext.class);
		}
		public MethodDeclContext methodDecl(int i) {
			return getRuleContext(MethodDeclContext.class,i);
		}
		public ClassBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterClassBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitClassBody(this);
		}
	}

	public final ClassBodyContext classBody() throws RecognitionException {
		ClassBodyContext _localctx = new ClassBodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_classBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(INDENT);
			setState(107); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(107);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
				case T__5:
				case T__8:
				case T__9:
				case NEWLINE:
				case IF:
				case FOR:
				case WHILE:
				case UNTIL:
				case RETURN:
				case WRITE:
				case READ:
				case CLASS:
				case CONTINUE:
				case BREAK:
				case LEN:
				case NOT:
				case INT_TYPE:
				case FLOAT_TYPE:
				case VECTOR:
				case MATRIX:
				case ID:
				case INT:
				case FLOAT:
				case STRING:
					{
					setState(105);
					statement();
					}
					break;
				case METHOD:
					{
					setState(106);
					methodDecl();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(109); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 8993931331110466L) != 0) );
			setState(111);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodDeclContext extends ParserRuleContext {
		public TerminalNode METHOD() { return getToken(vecmatlangParser.METHOD, 0); }
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public MethodDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterMethodDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitMethodDecl(this);
		}
	}

	public final MethodDeclContext methodDecl() throws RecognitionException {
		MethodDeclContext _localctx = new MethodDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_methodDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(METHOD);
			setState(114);
			match(ID);
			setState(115);
			match(T__0);
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(116);
				parameterList();
				}
			}

			setState(119);
			match(T__1);
			setState(120);
			match(T__2);
			setState(121);
			match(NEWLINE);
			setState(122);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FieldAppealContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(vecmatlangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(vecmatlangParser.ID, i);
		}
		public FieldAppealContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fieldAppeal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterFieldAppeal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitFieldAppeal(this);
		}
	}

	public final FieldAppealContext fieldAppeal() throws RecognitionException {
		FieldAppealContext _localctx = new FieldAppealContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_fieldAppeal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(ID);
			setState(125);
			match(T__4);
			setState(126);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodAppealContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(vecmatlangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(vecmatlangParser.ID, i);
		}
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public MethodAppealContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodAppeal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterMethodAppeal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitMethodAppeal(this);
		}
	}

	public final MethodAppealContext methodAppeal() throws RecognitionException {
		MethodAppealContext _localctx = new MethodAppealContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_methodAppeal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(ID);
			setState(129);
			match(T__4);
			setState(130);
			match(ID);
			setState(131);
			match(T__0);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8991840451692098L) != 0)) {
				{
				setState(132);
				argumentList();
				}
			}

			setState(135);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public ClassDeclContext classDecl() {
			return getRuleContext(ClassDeclContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public UntilStatementContext untilStatement() {
			return getRuleContext(UntilStatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public WriteStatementContext writeStatement() {
			return getRuleContext(WriteStatementContext.class,0);
		}
		public ReadStatementContext readStatement() {
			return getRuleContext(ReadStatementContext.class,0);
		}
		public TerminalNode CONTINUE() { return getToken(vecmatlangParser.CONTINUE, 0); }
		public TerminalNode BREAK() { return getToken(vecmatlangParser.BREAK, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(171);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				assignment();
				setState(139);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(138);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				classDecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(142);
				ifStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(143);
				forStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(144);
				whileStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(145);
				untilStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(146);
				expression(0);
				setState(148);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
				case 1:
					{
					setState(147);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(150);
				returnStatement();
				setState(152);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
				case 1:
					{
					setState(151);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(154);
				writeStatement();
				setState(156);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
				case 1:
					{
					setState(155);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(158);
				readStatement();
				setState(160);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
				case 1:
					{
					setState(159);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(162);
				match(CONTINUE);
				setState(164);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
				case 1:
					{
					setState(163);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(166);
				match(BREAK);
				setState(168);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
				case 1:
					{
					setState(167);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(170);
				match(NEWLINE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public FieldAppealContext fieldAppeal() {
			return getRuleContext(FieldAppealContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitVar(this);
		}
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_var);
		try {
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(173);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(174);
				fieldAppeal();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(175);
				match(ID);
				setState(176);
				match(T__5);
				setState(177);
				expression(0);
				setState(178);
				match(T__6);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public SingleAssignmentContext singleAssignment() {
			return getRuleContext(SingleAssignmentContext.class,0);
		}
		public MultipleAssignmentContext multipleAssignment() {
			return getRuleContext(MultipleAssignmentContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assignment);
		try {
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(182);
				singleAssignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				multipleAssignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SingleAssignmentContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public SingleAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleAssignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterSingleAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitSingleAssignment(this);
		}
	}

	public final SingleAssignmentContext singleAssignment() throws RecognitionException {
		SingleAssignmentContext _localctx = new SingleAssignmentContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_singleAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			var();
			setState(187);
			match(T__7);
			setState(188);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultipleAssignmentContext extends ParserRuleContext {
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MultipleAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multipleAssignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterMultipleAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitMultipleAssignment(this);
		}
	}

	public final MultipleAssignmentContext multipleAssignment() throws RecognitionException {
		MultipleAssignmentContext _localctx = new MultipleAssignmentContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_multipleAssignment);
		int _la;
		try {
			setState(207);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				var();
				setState(193); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(191);
					match(T__3);
					setState(192);
					var();
					}
					}
					setState(195); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__3 );
				setState(197);
				match(T__7);
				setState(198);
				primaryExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(200);
				expression(0);
				setState(203); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(201);
					match(T__3);
					setState(202);
					expression(0);
					}
					}
					setState(205); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__3 );
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(vecmatlangParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode THEN() { return getToken(vecmatlangParser.THEN, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(vecmatlangParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(vecmatlangParser.NEWLINE, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(vecmatlangParser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterIfStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitIfStatement(this);
		}
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(IF);
			setState(210);
			expression(0);
			setState(211);
			match(THEN);
			setState(212);
			match(NEWLINE);
			setState(213);
			block();
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(214);
				match(ELSE);
				setState(215);
				match(NEWLINE);
				setState(216);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(vecmatlangParser.FOR, 0); }
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public TerminalNode IN() { return getToken(vecmatlangParser.IN, 0); }
		public TerminalNode RANGE() { return getToken(vecmatlangParser.RANGE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterForStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitForStatement(this);
		}
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(FOR);
			setState(220);
			match(ID);
			setState(221);
			match(IN);
			setState(222);
			match(RANGE);
			setState(223);
			match(T__0);
			setState(224);
			expression(0);
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(225);
				match(T__3);
				setState(226);
				expression(0);
				}
				break;
			}
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(229);
				match(T__3);
				setState(230);
				expression(0);
				}
			}

			setState(233);
			match(T__1);
			setState(234);
			match(NEWLINE);
			setState(235);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(vecmatlangParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterWhileStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitWhileStatement(this);
		}
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(WHILE);
			setState(238);
			expression(0);
			setState(239);
			match(NEWLINE);
			setState(240);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UntilStatementContext extends ParserRuleContext {
		public TerminalNode UNTIL() { return getToken(vecmatlangParser.UNTIL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(vecmatlangParser.NEWLINE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public UntilStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_untilStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterUntilStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitUntilStatement(this);
		}
	}

	public final UntilStatementContext untilStatement() throws RecognitionException {
		UntilStatementContext _localctx = new UntilStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_untilStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(UNTIL);
			setState(243);
			expression(0);
			setState(244);
			match(NEWLINE);
			setState(245);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(vecmatlangParser.RETURN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterReturnStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitReturnStatement(this);
		}
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_returnStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(RETURN);
			setState(248);
			argumentList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteStatementContext extends ParserRuleContext {
		public TerminalNode WRITE() { return getToken(vecmatlangParser.WRITE, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public WriteStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_writeStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterWriteStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitWriteStatement(this);
		}
	}

	public final WriteStatementContext writeStatement() throws RecognitionException {
		WriteStatementContext _localctx = new WriteStatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_writeStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(WRITE);
			setState(251);
			match(T__0);
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8991840451692098L) != 0)) {
				{
				setState(252);
				argumentList();
				}
			}

			setState(255);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadStatementContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(vecmatlangParser.READ, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public ReadStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_readStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterReadStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitReadStatement(this);
		}
	}

	public final ReadStatementContext readStatement() throws RecognitionException {
		ReadStatementContext _localctx = new ReadStatementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_readStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(READ);
			setState(258);
			match(T__0);
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8991840451692098L) != 0)) {
				{
				setState(259);
				argumentList();
				}
			}

			setState(262);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IndexExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public IndexExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterIndexExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitIndexExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotExprContext extends ExpressionContext {
		public TerminalNode NOT() { return getToken(vecmatlangParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NotExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterNotExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitNotExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AddSubExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterAddSubExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitAddSubExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExprContext extends ExpressionContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public PrimaryExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterPrimaryExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitPrimaryExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryMinusExprContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public UnaryMinusExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterUnaryMinusExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitUnaryMinusExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ComparisonExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterComparisonExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitComparisonExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MulDivExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterMulDivExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitMulDivExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BinlogicExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(vecmatlangParser.AND, 0); }
		public TerminalNode OR() { return getToken(vecmatlangParser.OR, 0); }
		public BinlogicExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterBinlogicExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitBinlogicExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NormExprContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NormExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterNormExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitNormExpr(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__5:
			case READ:
			case LEN:
			case INT_TYPE:
			case FLOAT_TYPE:
			case VECTOR:
			case MATRIX:
			case ID:
			case INT:
			case FLOAT:
			case STRING:
				{
				_localctx = new PrimaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(265);
				primaryExpression();
				}
				break;
			case T__8:
				{
				_localctx = new NormExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(266);
				match(T__8);
				setState(267);
				expression(0);
				setState(268);
				match(T__8);
				}
				break;
			case T__9:
				{
				_localctx = new UnaryMinusExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(270);
				match(T__9);
				setState(271);
				expression(7);
				}
				break;
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(272);
				match(NOT);
				setState(273);
				expression(2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(295);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(293);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(276);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(277);
						_la = _input.LA(1);
						if ( !(_la==T__10 || _la==T__11) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(278);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new AddSubExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(279);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(280);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__12) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(281);
						expression(5);
						}
						break;
					case 3:
						{
						_localctx = new ComparisonExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(282);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(283);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1032192L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(284);
						expression(4);
						}
						break;
					case 4:
						{
						_localctx = new BinlogicExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(285);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(286);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(287);
						expression(2);
						}
						break;
					case 5:
						{
						_localctx = new IndexExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(288);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(289);
						match(T__5);
						setState(290);
						expression(0);
						setState(291);
						match(T__6);
						}
						break;
					}
					} 
				}
				setState(297);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(vecmatlangParser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(vecmatlangParser.FLOAT_TYPE, 0); }
		public TerminalNode VECTOR() { return getToken(vecmatlangParser.VECTOR, 0); }
		public TerminalNode MATRIX() { return getToken(vecmatlangParser.MATRIX, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitType(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 527765581332480L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	 
		public PrimaryExpressionContext() { }
		public void copyFrom(PrimaryExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LenExprContext extends PrimaryExpressionContext {
		public TerminalNode LEN() { return getToken(vecmatlangParser.LEN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public LenExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterLenExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitLenExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TypeExprContext extends PrimaryExpressionContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public TypeExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterTypeExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitTypeExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LiteralExprContext extends PrimaryExpressionContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public LiteralExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterLiteralExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitLiteralExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReadExprContext extends PrimaryExpressionContext {
		public ReadStatementContext readStatement() {
			return getRuleContext(ReadStatementContext.class,0);
		}
		public ReadExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterReadExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitReadExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncCallExprContext extends PrimaryExpressionContext {
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FuncCallExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterFuncCallExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitFuncCallExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenExprContext extends PrimaryExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParenExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterParenExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitParenExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdExprContext extends PrimaryExpressionContext {
		public TerminalNode ID() { return getToken(vecmatlangParser.ID, 0); }
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public IdExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterIdExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitIdExpr(this);
		}
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_primaryExpression);
		int _la;
		try {
			setState(327);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				_localctx = new IdExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				match(ID);
				}
				break;
			case 2:
				_localctx = new ParenExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(301);
				match(T__0);
				setState(302);
				expression(0);
				setState(303);
				match(T__1);
				}
				break;
			case 3:
				_localctx = new FuncCallExprContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(305);
				match(ID);
				setState(306);
				match(T__0);
				setState(308);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8991840451692098L) != 0)) {
					{
					setState(307);
					argumentList();
					}
				}

				setState(310);
				match(T__1);
				}
				break;
			case 4:
				_localctx = new LiteralExprContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(311);
				literal();
				}
				break;
			case 5:
				_localctx = new IdExprContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(312);
				var();
				}
				break;
			case 6:
				_localctx = new TypeExprContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(313);
				type();
				setState(314);
				match(T__0);
				setState(316);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8991840451692098L) != 0)) {
					{
					setState(315);
					argumentList();
					}
				}

				setState(318);
				match(T__1);
				}
				break;
			case 7:
				_localctx = new LenExprContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(320);
				match(LEN);
				setState(321);
				match(T__0);
				setState(323);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8991840451692098L) != 0)) {
					{
					setState(322);
					argumentList();
					}
				}

				setState(325);
				match(T__1);
				}
				break;
			case 8:
				_localctx = new ReadExprContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(326);
				readStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterArgumentList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitArgumentList(this);
		}
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			expression(0);
			setState(334);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(330);
				match(T__3);
				setState(331);
				expression(0);
				}
				}
				setState(336);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	 
		public LiteralContext() { }
		public void copyFrom(LiteralContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VectorLiteralContext extends LiteralContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public VectorLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterVectorLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitVectorLiteral(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringLiteralContext extends LiteralContext {
		public TerminalNode STRING() { return getToken(vecmatlangParser.STRING, 0); }
		public StringLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterStringLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitStringLiteral(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntLiteralContext extends LiteralContext {
		public TerminalNode INT() { return getToken(vecmatlangParser.INT, 0); }
		public IntLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterIntLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitIntLiteral(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MatrixLiteralContext extends LiteralContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MatrixLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterMatrixLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitMatrixLiteral(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FloatLiteralContext extends LiteralContext {
		public TerminalNode FLOAT() { return getToken(vecmatlangParser.FLOAT, 0); }
		public FloatLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).enterFloatLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof vecmatlangListener ) ((vecmatlangListener)listener).exitFloatLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_literal);
		int _la;
		try {
			setState(381);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				_localctx = new IntLiteralContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(337);
				match(INT);
				}
				break;
			case 2:
				_localctx = new FloatLiteralContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(338);
				match(FLOAT);
				}
				break;
			case 3:
				_localctx = new VectorLiteralContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(339);
				match(T__5);
				setState(340);
				expression(0);
				setState(345);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(341);
					match(T__3);
					setState(342);
					expression(0);
					}
					}
					setState(347);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(348);
				match(T__6);
				}
				break;
			case 4:
				_localctx = new MatrixLiteralContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(350);
				match(T__5);
				setState(351);
				match(T__5);
				setState(352);
				expression(0);
				setState(357);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(353);
					match(T__3);
					setState(354);
					expression(0);
					}
					}
					setState(359);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(360);
				match(T__6);
				setState(375);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(361);
					match(T__3);
					setState(362);
					match(T__5);
					setState(363);
					expression(0);
					setState(368);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__3) {
						{
						{
						setState(364);
						match(T__3);
						setState(365);
						expression(0);
						}
						}
						setState(370);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(371);
					match(T__6);
					}
					}
					setState(377);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(378);
				match(T__6);
				}
				break;
			case 5:
				_localctx = new StringLiteralContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(380);
				match(STRING);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 21:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 1);
		case 4:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00015\u0180\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0001\u0000\u0005\u00006\b\u0000\n\u0000\f\u0000"+
		"9\t\u0000\u0001\u0000\u0005\u0000<\b\u0000\n\u0000\f\u0000?\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001G\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002Q\b\u0002\n\u0002"+
		"\f\u0002T\t\u0002\u0001\u0003\u0001\u0003\u0004\u0003X\b\u0003\u000b\u0003"+
		"\f\u0003Y\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004b\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0004\u0005"+
		"l\b\u0005\u000b\u0005\f\u0005m\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0003\u0006v\b\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0086"+
		"\b\b\u0001\b\u0001\b\u0001\t\u0001\t\u0003\t\u008c\b\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u0095\b\t\u0001\t\u0001"+
		"\t\u0003\t\u0099\b\t\u0001\t\u0001\t\u0003\t\u009d\b\t\u0001\t\u0001\t"+
		"\u0003\t\u00a1\b\t\u0001\t\u0001\t\u0003\t\u00a5\b\t\u0001\t\u0001\t\u0003"+
		"\t\u00a9\b\t\u0001\t\u0003\t\u00ac\b\t\u0001\n\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0003\n\u00b5\b\n\u0001\u000b\u0001\u000b\u0003"+
		"\u000b\u00b9\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0004\r\u00c2\b\r\u000b\r\f\r\u00c3\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0004\r\u00cc\b\r\u000b\r\f\r\u00cd\u0003\r\u00d0\b\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u00da\b\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0003\u000f\u00e4\b\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00e8\b"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00fe\b\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u0105\b\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003"+
		"\u0015\u0113\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0005\u0015\u0126\b\u0015\n\u0015\f\u0015\u0129\t\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0135\b\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017"+
		"\u013d\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0003\u0017\u0144\b\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0148\b"+
		"\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u014d\b\u0018\n"+
		"\u0018\f\u0018\u0150\t\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u0158\b\u0019\n\u0019\f\u0019"+
		"\u015b\t\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0005\u0019\u0164\b\u0019\n\u0019\f\u0019\u0167"+
		"\t\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0005\u0019\u016f\b\u0019\n\u0019\f\u0019\u0172\t\u0019\u0001\u0019"+
		"\u0001\u0019\u0005\u0019\u0176\b\u0019\n\u0019\f\u0019\u0179\t\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u017e\b\u0019\u0001\u0019\u0000"+
		"\u0001*\u001a\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02\u0000\u0005\u0001\u0000\u000b\f\u0002"+
		"\u0000\n\n\r\r\u0001\u0000\u000e\u0013\u0001\u0000*+\u0001\u0000-0\u01a8"+
		"\u00007\u0001\u0000\u0000\u0000\u0002B\u0001\u0000\u0000\u0000\u0004M"+
		"\u0001\u0000\u0000\u0000\u0006U\u0001\u0000\u0000\u0000\b]\u0001\u0000"+
		"\u0000\u0000\nh\u0001\u0000\u0000\u0000\fq\u0001\u0000\u0000\u0000\u000e"+
		"|\u0001\u0000\u0000\u0000\u0010\u0080\u0001\u0000\u0000\u0000\u0012\u00ab"+
		"\u0001\u0000\u0000\u0000\u0014\u00b4\u0001\u0000\u0000\u0000\u0016\u00b8"+
		"\u0001\u0000\u0000\u0000\u0018\u00ba\u0001\u0000\u0000\u0000\u001a\u00cf"+
		"\u0001\u0000\u0000\u0000\u001c\u00d1\u0001\u0000\u0000\u0000\u001e\u00db"+
		"\u0001\u0000\u0000\u0000 \u00ed\u0001\u0000\u0000\u0000\"\u00f2\u0001"+
		"\u0000\u0000\u0000$\u00f7\u0001\u0000\u0000\u0000&\u00fa\u0001\u0000\u0000"+
		"\u0000(\u0101\u0001\u0000\u0000\u0000*\u0112\u0001\u0000\u0000\u0000,"+
		"\u012a\u0001\u0000\u0000\u0000.\u0147\u0001\u0000\u0000\u00000\u0149\u0001"+
		"\u0000\u0000\u00002\u017d\u0001\u0000\u0000\u000046\u0003\u0002\u0001"+
		"\u000054\u0001\u0000\u0000\u000069\u0001\u0000\u0000\u000075\u0001\u0000"+
		"\u0000\u000078\u0001\u0000\u0000\u00008=\u0001\u0000\u0000\u000097\u0001"+
		"\u0000\u0000\u0000:<\u0003\u0012\t\u0000;:\u0001\u0000\u0000\u0000<?\u0001"+
		"\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000"+
		">@\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000@A\u0005\u0000\u0000"+
		"\u0001A\u0001\u0001\u0000\u0000\u0000BC\u0005 \u0000\u0000CD\u00051\u0000"+
		"\u0000DF\u0005\u0001\u0000\u0000EG\u0003\u0004\u0002\u0000FE\u0001\u0000"+
		"\u0000\u0000FG\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0005"+
		"\u0002\u0000\u0000IJ\u0005\u0003\u0000\u0000JK\u0005\u0015\u0000\u0000"+
		"KL\u0003\u0006\u0003\u0000L\u0003\u0001\u0000\u0000\u0000MR\u00051\u0000"+
		"\u0000NO\u0005\u0004\u0000\u0000OQ\u00051\u0000\u0000PN\u0001\u0000\u0000"+
		"\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000"+
		"\u0000\u0000S\u0005\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000"+
		"UW\u0005\u0017\u0000\u0000VX\u0003\u0012\t\u0000WV\u0001\u0000\u0000\u0000"+
		"XY\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000Z[\u0001\u0000\u0000\u0000[\\\u0005\u0018\u0000\u0000\\\u0007\u0001"+
		"\u0000\u0000\u0000]^\u0005%\u0000\u0000^_\u00051\u0000\u0000_a\u0005\u0001"+
		"\u0000\u0000`b\u0003\u0004\u0002\u0000a`\u0001\u0000\u0000\u0000ab\u0001"+
		"\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000cd\u0005\u0002\u0000\u0000"+
		"de\u0005\u0003\u0000\u0000ef\u0005\u0015\u0000\u0000fg\u0003\n\u0005\u0000"+
		"g\t\u0001\u0000\u0000\u0000hk\u0005\u0017\u0000\u0000il\u0003\u0012\t"+
		"\u0000jl\u0003\f\u0006\u0000ki\u0001\u0000\u0000\u0000kj\u0001\u0000\u0000"+
		"\u0000lm\u0001\u0000\u0000\u0000mk\u0001\u0000\u0000\u0000mn\u0001\u0000"+
		"\u0000\u0000no\u0001\u0000\u0000\u0000op\u0005\u0018\u0000\u0000p\u000b"+
		"\u0001\u0000\u0000\u0000qr\u0005&\u0000\u0000rs\u00051\u0000\u0000su\u0005"+
		"\u0001\u0000\u0000tv\u0003\u0004\u0002\u0000ut\u0001\u0000\u0000\u0000"+
		"uv\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wx\u0005\u0002\u0000"+
		"\u0000xy\u0005\u0003\u0000\u0000yz\u0005\u0015\u0000\u0000z{\u0003\u0006"+
		"\u0003\u0000{\r\u0001\u0000\u0000\u0000|}\u00051\u0000\u0000}~\u0005\u0005"+
		"\u0000\u0000~\u007f\u00051\u0000\u0000\u007f\u000f\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u00051\u0000\u0000\u0081\u0082\u0005\u0005\u0000\u0000\u0082"+
		"\u0083\u00051\u0000\u0000\u0083\u0085\u0005\u0001\u0000\u0000\u0084\u0086"+
		"\u00030\u0018\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0085\u0086\u0001"+
		"\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000\u0087\u0088\u0005"+
		"\u0002\u0000\u0000\u0088\u0011\u0001\u0000\u0000\u0000\u0089\u008b\u0003"+
		"\u0016\u000b\u0000\u008a\u008c\u0005\u0015\u0000\u0000\u008b\u008a\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u00ac\u0001"+
		"\u0000\u0000\u0000\u008d\u00ac\u0003\b\u0004\u0000\u008e\u00ac\u0003\u001c"+
		"\u000e\u0000\u008f\u00ac\u0003\u001e\u000f\u0000\u0090\u00ac\u0003 \u0010"+
		"\u0000\u0091\u00ac\u0003\"\u0011\u0000\u0092\u0094\u0003*\u0015\u0000"+
		"\u0093\u0095\u0005\u0015\u0000\u0000\u0094\u0093\u0001\u0000\u0000\u0000"+
		"\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u00ac\u0001\u0000\u0000\u0000"+
		"\u0096\u0098\u0003$\u0012\u0000\u0097\u0099\u0005\u0015\u0000\u0000\u0098"+
		"\u0097\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099"+
		"\u00ac\u0001\u0000\u0000\u0000\u009a\u009c\u0003&\u0013\u0000\u009b\u009d"+
		"\u0005\u0015\u0000\u0000\u009c\u009b\u0001\u0000\u0000\u0000\u009c\u009d"+
		"\u0001\u0000\u0000\u0000\u009d\u00ac\u0001\u0000\u0000\u0000\u009e\u00a0"+
		"\u0003(\u0014\u0000\u009f\u00a1\u0005\u0015\u0000\u0000\u00a0\u009f\u0001"+
		"\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1\u00ac\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a4\u0005\'\u0000\u0000\u00a3\u00a5\u0005\u0015"+
		"\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000"+
		"\u0000\u0000\u00a5\u00ac\u0001\u0000\u0000\u0000\u00a6\u00a8\u0005(\u0000"+
		"\u0000\u00a7\u00a9\u0005\u0015\u0000\u0000\u00a8\u00a7\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00ac\u0001\u0000\u0000"+
		"\u0000\u00aa\u00ac\u0005\u0015\u0000\u0000\u00ab\u0089\u0001\u0000\u0000"+
		"\u0000\u00ab\u008d\u0001\u0000\u0000\u0000\u00ab\u008e\u0001\u0000\u0000"+
		"\u0000\u00ab\u008f\u0001\u0000\u0000\u0000\u00ab\u0090\u0001\u0000\u0000"+
		"\u0000\u00ab\u0091\u0001\u0000\u0000\u0000\u00ab\u0092\u0001\u0000\u0000"+
		"\u0000\u00ab\u0096\u0001\u0000\u0000\u0000\u00ab\u009a\u0001\u0000\u0000"+
		"\u0000\u00ab\u009e\u0001\u0000\u0000\u0000\u00ab\u00a2\u0001\u0000\u0000"+
		"\u0000\u00ab\u00a6\u0001\u0000\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000"+
		"\u0000\u00ac\u0013\u0001\u0000\u0000\u0000\u00ad\u00b5\u00051\u0000\u0000"+
		"\u00ae\u00b5\u0003\u000e\u0007\u0000\u00af\u00b0\u00051\u0000\u0000\u00b0"+
		"\u00b1\u0005\u0006\u0000\u0000\u00b1\u00b2\u0003*\u0015\u0000\u00b2\u00b3"+
		"\u0005\u0007\u0000\u0000\u00b3\u00b5\u0001\u0000\u0000\u0000\u00b4\u00ad"+
		"\u0001\u0000\u0000\u0000\u00b4\u00ae\u0001\u0000\u0000\u0000\u00b4\u00af"+
		"\u0001\u0000\u0000\u0000\u00b5\u0015\u0001\u0000\u0000\u0000\u00b6\u00b9"+
		"\u0003\u0018\f\u0000\u00b7\u00b9\u0003\u001a\r\u0000\u00b8\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b8\u00b7\u0001\u0000\u0000\u0000\u00b9\u0017\u0001"+
		"\u0000\u0000\u0000\u00ba\u00bb\u0003\u0014\n\u0000\u00bb\u00bc\u0005\b"+
		"\u0000\u0000\u00bc\u00bd\u0003*\u0015\u0000\u00bd\u0019\u0001\u0000\u0000"+
		"\u0000\u00be\u00c1\u0003\u0014\n\u0000\u00bf\u00c0\u0005\u0004\u0000\u0000"+
		"\u00c0\u00c2\u0003\u0014\n\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2"+
		"\u00c3\u0001\u0000\u0000\u0000\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5"+
		"\u00c6\u0005\b\u0000\u0000\u00c6\u00c7\u0003.\u0017\u0000\u00c7\u00d0"+
		"\u0001\u0000\u0000\u0000\u00c8\u00cb\u0003*\u0015\u0000\u00c9\u00ca\u0005"+
		"\u0004\u0000\u0000\u00ca\u00cc\u0003*\u0015\u0000\u00cb\u00c9\u0001\u0000"+
		"\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000"+
		"\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce\u00d0\u0001\u0000"+
		"\u0000\u0000\u00cf\u00be\u0001\u0000\u0000\u0000\u00cf\u00c8\u0001\u0000"+
		"\u0000\u0000\u00d0\u001b\u0001\u0000\u0000\u0000\u00d1\u00d2\u0005\u0019"+
		"\u0000\u0000\u00d2\u00d3\u0003*\u0015\u0000\u00d3\u00d4\u0005\u001a\u0000"+
		"\u0000\u00d4\u00d5\u0005\u0015\u0000\u0000\u00d5\u00d9\u0003\u0006\u0003"+
		"\u0000\u00d6\u00d7\u0005\u001b\u0000\u0000\u00d7\u00d8\u0005\u0015\u0000"+
		"\u0000\u00d8\u00da\u0003\u0006\u0003\u0000\u00d9\u00d6\u0001\u0000\u0000"+
		"\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u001d\u0001\u0000\u0000"+
		"\u0000\u00db\u00dc\u0005\u001c\u0000\u0000\u00dc\u00dd\u00051\u0000\u0000"+
		"\u00dd\u00de\u0005\u001d\u0000\u0000\u00de\u00df\u0005$\u0000\u0000\u00df"+
		"\u00e0\u0005\u0001\u0000\u0000\u00e0\u00e3\u0003*\u0015\u0000\u00e1\u00e2"+
		"\u0005\u0004\u0000\u0000\u00e2\u00e4\u0003*\u0015\u0000\u00e3\u00e1\u0001"+
		"\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000\u0000\u00e4\u00e7\u0001"+
		"\u0000\u0000\u0000\u00e5\u00e6\u0005\u0004\u0000\u0000\u00e6\u00e8\u0003"+
		"*\u0015\u0000\u00e7\u00e5\u0001\u0000\u0000\u0000\u00e7\u00e8\u0001\u0000"+
		"\u0000\u0000\u00e8\u00e9\u0001\u0000\u0000\u0000\u00e9\u00ea\u0005\u0002"+
		"\u0000\u0000\u00ea\u00eb\u0005\u0015\u0000\u0000\u00eb\u00ec\u0003\u0006"+
		"\u0003\u0000\u00ec\u001f\u0001\u0000\u0000\u0000\u00ed\u00ee\u0005\u001e"+
		"\u0000\u0000\u00ee\u00ef\u0003*\u0015\u0000\u00ef\u00f0\u0005\u0015\u0000"+
		"\u0000\u00f0\u00f1\u0003\u0006\u0003\u0000\u00f1!\u0001\u0000\u0000\u0000"+
		"\u00f2\u00f3\u0005\u001f\u0000\u0000\u00f3\u00f4\u0003*\u0015\u0000\u00f4"+
		"\u00f5\u0005\u0015\u0000\u0000\u00f5\u00f6\u0003\u0006\u0003\u0000\u00f6"+
		"#\u0001\u0000\u0000\u0000\u00f7\u00f8\u0005!\u0000\u0000\u00f8\u00f9\u0003"+
		"0\u0018\u0000\u00f9%\u0001\u0000\u0000\u0000\u00fa\u00fb\u0005\"\u0000"+
		"\u0000\u00fb\u00fd\u0005\u0001\u0000\u0000\u00fc\u00fe\u00030\u0018\u0000"+
		"\u00fd\u00fc\u0001\u0000\u0000\u0000\u00fd\u00fe\u0001\u0000\u0000\u0000"+
		"\u00fe\u00ff\u0001\u0000\u0000\u0000\u00ff\u0100\u0005\u0002\u0000\u0000"+
		"\u0100\'\u0001\u0000\u0000\u0000\u0101\u0102\u0005#\u0000\u0000\u0102"+
		"\u0104\u0005\u0001\u0000\u0000\u0103\u0105\u00030\u0018\u0000\u0104\u0103"+
		"\u0001\u0000\u0000\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105\u0106"+
		"\u0001\u0000\u0000\u0000\u0106\u0107\u0005\u0002\u0000\u0000\u0107)\u0001"+
		"\u0000\u0000\u0000\u0108\u0109\u0006\u0015\uffff\uffff\u0000\u0109\u0113"+
		"\u0003.\u0017\u0000\u010a\u010b\u0005\t\u0000\u0000\u010b\u010c\u0003"+
		"*\u0015\u0000\u010c\u010d\u0005\t\u0000\u0000\u010d\u0113\u0001\u0000"+
		"\u0000\u0000\u010e\u010f\u0005\n\u0000\u0000\u010f\u0113\u0003*\u0015"+
		"\u0007\u0110\u0111\u0005,\u0000\u0000\u0111\u0113\u0003*\u0015\u0002\u0112"+
		"\u0108\u0001\u0000\u0000\u0000\u0112\u010a\u0001\u0000\u0000\u0000\u0112"+
		"\u010e\u0001\u0000\u0000\u0000\u0112\u0110\u0001\u0000\u0000\u0000\u0113"+
		"\u0127\u0001\u0000\u0000\u0000\u0114\u0115\n\u0005\u0000\u0000\u0115\u0116"+
		"\u0007\u0000\u0000\u0000\u0116\u0126\u0003*\u0015\u0006\u0117\u0118\n"+
		"\u0004\u0000\u0000\u0118\u0119\u0007\u0001\u0000\u0000\u0119\u0126\u0003"+
		"*\u0015\u0005\u011a\u011b\n\u0003\u0000\u0000\u011b\u011c\u0007\u0002"+
		"\u0000\u0000\u011c\u0126\u0003*\u0015\u0004\u011d\u011e\n\u0001\u0000"+
		"\u0000\u011e\u011f\u0007\u0003\u0000\u0000\u011f\u0126\u0003*\u0015\u0002"+
		"\u0120\u0121\n\u0006\u0000\u0000\u0121\u0122\u0005\u0006\u0000\u0000\u0122"+
		"\u0123\u0003*\u0015\u0000\u0123\u0124\u0005\u0007\u0000\u0000\u0124\u0126"+
		"\u0001\u0000\u0000\u0000\u0125\u0114\u0001\u0000\u0000\u0000\u0125\u0117"+
		"\u0001\u0000\u0000\u0000\u0125\u011a\u0001\u0000\u0000\u0000\u0125\u011d"+
		"\u0001\u0000\u0000\u0000\u0125\u0120\u0001\u0000\u0000\u0000\u0126\u0129"+
		"\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000\u0000\u0127\u0128"+
		"\u0001\u0000\u0000\u0000\u0128+\u0001\u0000\u0000\u0000\u0129\u0127\u0001"+
		"\u0000\u0000\u0000\u012a\u012b\u0007\u0004\u0000\u0000\u012b-\u0001\u0000"+
		"\u0000\u0000\u012c\u0148\u00051\u0000\u0000\u012d\u012e\u0005\u0001\u0000"+
		"\u0000\u012e\u012f\u0003*\u0015\u0000\u012f\u0130\u0005\u0002\u0000\u0000"+
		"\u0130\u0148\u0001\u0000\u0000\u0000\u0131\u0132\u00051\u0000\u0000\u0132"+
		"\u0134\u0005\u0001\u0000\u0000\u0133\u0135\u00030\u0018\u0000\u0134\u0133"+
		"\u0001\u0000\u0000\u0000\u0134\u0135\u0001\u0000\u0000\u0000\u0135\u0136"+
		"\u0001\u0000\u0000\u0000\u0136\u0148\u0005\u0002\u0000\u0000\u0137\u0148"+
		"\u00032\u0019\u0000\u0138\u0148\u0003\u0014\n\u0000\u0139\u013a\u0003"+
		",\u0016\u0000\u013a\u013c\u0005\u0001\u0000\u0000\u013b\u013d\u00030\u0018"+
		"\u0000\u013c\u013b\u0001\u0000\u0000\u0000\u013c\u013d\u0001\u0000\u0000"+
		"\u0000\u013d\u013e\u0001\u0000\u0000\u0000\u013e\u013f\u0005\u0002\u0000"+
		"\u0000\u013f\u0148\u0001\u0000\u0000\u0000\u0140\u0141\u0005)\u0000\u0000"+
		"\u0141\u0143\u0005\u0001\u0000\u0000\u0142\u0144\u00030\u0018\u0000\u0143"+
		"\u0142\u0001\u0000\u0000\u0000\u0143\u0144\u0001\u0000\u0000\u0000\u0144"+
		"\u0145\u0001\u0000\u0000\u0000\u0145\u0148\u0005\u0002\u0000\u0000\u0146"+
		"\u0148\u0003(\u0014\u0000\u0147\u012c\u0001\u0000\u0000\u0000\u0147\u012d"+
		"\u0001\u0000\u0000\u0000\u0147\u0131\u0001\u0000\u0000\u0000\u0147\u0137"+
		"\u0001\u0000\u0000\u0000\u0147\u0138\u0001\u0000\u0000\u0000\u0147\u0139"+
		"\u0001\u0000\u0000\u0000\u0147\u0140\u0001\u0000\u0000\u0000\u0147\u0146"+
		"\u0001\u0000\u0000\u0000\u0148/\u0001\u0000\u0000\u0000\u0149\u014e\u0003"+
		"*\u0015\u0000\u014a\u014b\u0005\u0004\u0000\u0000\u014b\u014d\u0003*\u0015"+
		"\u0000\u014c\u014a\u0001\u0000\u0000\u0000\u014d\u0150\u0001\u0000\u0000"+
		"\u0000\u014e\u014c\u0001\u0000\u0000\u0000\u014e\u014f\u0001\u0000\u0000"+
		"\u0000\u014f1\u0001\u0000\u0000\u0000\u0150\u014e\u0001\u0000\u0000\u0000"+
		"\u0151\u017e\u00052\u0000\u0000\u0152\u017e\u00053\u0000\u0000\u0153\u0154"+
		"\u0005\u0006\u0000\u0000\u0154\u0159\u0003*\u0015\u0000\u0155\u0156\u0005"+
		"\u0004\u0000\u0000\u0156\u0158\u0003*\u0015\u0000\u0157\u0155\u0001\u0000"+
		"\u0000\u0000\u0158\u015b\u0001\u0000\u0000\u0000\u0159\u0157\u0001\u0000"+
		"\u0000\u0000\u0159\u015a\u0001\u0000\u0000\u0000\u015a\u015c\u0001\u0000"+
		"\u0000\u0000\u015b\u0159\u0001\u0000\u0000\u0000\u015c\u015d\u0005\u0007"+
		"\u0000\u0000\u015d\u017e\u0001\u0000\u0000\u0000\u015e\u015f\u0005\u0006"+
		"\u0000\u0000\u015f\u0160\u0005\u0006\u0000\u0000\u0160\u0165\u0003*\u0015"+
		"\u0000\u0161\u0162\u0005\u0004\u0000\u0000\u0162\u0164\u0003*\u0015\u0000"+
		"\u0163\u0161\u0001\u0000\u0000\u0000\u0164\u0167\u0001\u0000\u0000\u0000"+
		"\u0165\u0163\u0001\u0000\u0000\u0000\u0165\u0166\u0001\u0000\u0000\u0000"+
		"\u0166\u0168\u0001\u0000\u0000\u0000\u0167\u0165\u0001\u0000\u0000\u0000"+
		"\u0168\u0177\u0005\u0007\u0000\u0000\u0169\u016a\u0005\u0004\u0000\u0000"+
		"\u016a\u016b\u0005\u0006\u0000\u0000\u016b\u0170\u0003*\u0015\u0000\u016c"+
		"\u016d\u0005\u0004\u0000\u0000\u016d\u016f\u0003*\u0015\u0000\u016e\u016c"+
		"\u0001\u0000\u0000\u0000\u016f\u0172\u0001\u0000\u0000\u0000\u0170\u016e"+
		"\u0001\u0000\u0000\u0000\u0170\u0171\u0001\u0000\u0000\u0000\u0171\u0173"+
		"\u0001\u0000\u0000\u0000\u0172\u0170\u0001\u0000\u0000\u0000\u0173\u0174"+
		"\u0005\u0007\u0000\u0000\u0174\u0176\u0001\u0000\u0000\u0000\u0175\u0169"+
		"\u0001\u0000\u0000\u0000\u0176\u0179\u0001\u0000\u0000\u0000\u0177\u0175"+
		"\u0001\u0000\u0000\u0000\u0177\u0178\u0001\u0000\u0000\u0000\u0178\u017a"+
		"\u0001\u0000\u0000\u0000\u0179\u0177\u0001\u0000\u0000\u0000\u017a\u017b"+
		"\u0005\u0007\u0000\u0000\u017b\u017e\u0001\u0000\u0000\u0000\u017c\u017e"+
		"\u00054\u0000\u0000\u017d\u0151\u0001\u0000\u0000\u0000\u017d\u0152\u0001"+
		"\u0000\u0000\u0000\u017d\u0153\u0001\u0000\u0000\u0000\u017d\u015e\u0001"+
		"\u0000\u0000\u0000\u017d\u017c\u0001\u0000\u0000\u0000\u017e3\u0001\u0000"+
		"\u0000\u0000)7=FRYakmu\u0085\u008b\u0094\u0098\u009c\u00a0\u00a4\u00a8"+
		"\u00ab\u00b4\u00b8\u00c3\u00cd\u00cf\u00d9\u00e3\u00e7\u00fd\u0104\u0112"+
		"\u0125\u0127\u0134\u013c\u0143\u0147\u014e\u0159\u0165\u0170\u0177\u017d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}