#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import ply.lex as lex
import ply.yacc as yacc

from symtab import Scope, Symbol, SymbolTable

## トークン名のリスト
tokens = (
    'BEGIN', 'DIV', 'DO', 'ELSE', 'END', 'FOR', 'FUNCTION', 'IF',
    'PROCEDURE', 'PROGRAM', 'READ', 'THEN', 'TO', 'VAR', 'WHILE', 'WRITE',
    'PLUS', 'MINUS', 'MULT', 'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE',
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON',
    'PERIOD', 'INTERVAL', 'ASSIGN',
    'IDENT', 'NUMBER'
)

## 予約語の定義
reserved = {
    'begin': 'BEGIN',
    'div': 'DIV',
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'procedure': 'PROCEDURE',
    'program': 'PROGRAM',
    'read': 'READ',
    'then': 'THEN',
    'to': 'TO',
    'var': 'VAR',
    'while': 'WHILE',
    'write': 'WRITE'
}

## 基本シンボルトークンを切り出すルール
t_PLUS  = '\+'
t_MINUS = '-'
t_MULT  = '\*'
t_EQ = '='
t_NEQ = '<>'
t_LT = '<'
t_LE = '<='
t_GT = '>'
t_GE = '>='
t_LPAREN = '\('
t_RPAREN = '\)'
t_LBRACKET = '\['
t_RBRACKET = '\]'
t_COMMA = ','
t_SEMICOLON = ';'
t_PERIOD = '\.'
t_INTERVAL = '\.\.'
t_ASSIGN = ':='

# コメントおよび空白・タブを無視するルール
t_ignore_COMMENT = '\#.*'
t_ignore = ' \t'

## アクションを伴うトークンルール
# 変数名・手続き名などの識別子を切り出すルール
def t_IDENT(t):
    '[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

# 数値を切り出すルール
def t_NUMBER(t):
    '[1-9][0-9]*|0'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Line %d: integer value %s is too large" % t.lineno, t.value)
        t.value = 0
    return t

# 改行を読んだときの処理
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# エラー処理
def t_error(t):
    print("不正な文字「", t.value[0], "」")
    t.lexer.skip(1)


#################################################################
# 解析に必要な変数を宣言しておく
#################################################################

symtable = SymbolTable()
varscope = Scope.GLOBAL_VAR

#################################################################
# ここから先に構文規則を書く
#################################################################

def p_program(p):
    '''
    program : PROGRAM IDENT SEMICOLON outblock PERIOD
    '''

def p_outblock(p):
    '''
    outblock : var_decl_part subprog_decl_part statement
    '''

def p_var_decl_part(p):
    '''
    var_decl_part : var_decl_list SEMICOLON
                  |
    '''

def p_var_decl_list(p):
    '''
    var_decl_list : var_decl_list SEMICOLON var_decl
        | var_decl
    '''

def p_var_decl(p):
    '''
    var_decl : VAR id_list
    '''

def p_subprog_decl_part(p):
    '''
    subprog_decl_part : subprog_decl_list SEMICOLON
        | 
    '''

def p_subprog_decl_list(p):
    '''
    subprog_decl_list : subprog_decl_list SEMICOLON subprog_decl
        | subprog_decl
    '''

def p_subprog_decl(p):
    '''
    subprog_decl : proc_decl
    '''

def p_proc_decl(p):
    '''
    proc_decl : PROCEDURE proc_name SEMICOLON inblock
    '''

def p_proc_name(p):
    '''
    proc_name : IDENT
    '''

def p_inblock(p):
    '''
    inblock : var_decl_part statement
    '''

def p_statement_list(p):
    '''
    statement_list : statement_list SEMICOLON statement
        | statement
    '''

def p_statement(p):
    '''
    statement : assignment_statement
        | if_statement
        | while_statement
        | for_statement
        | proc_call_statement
        | null_statement
        | block_statement
        | read_statement
        | write_statement
    '''

def p_assignment_statement(p):
    '''
    assignment_statement : IDENT ASSIGN expression
    '''

def p_if_statement(p):
    '''
    if_statement : IF condition THEN statement else_statement
    '''

def p_else_statement(p):
    '''
    else_statement : ELSE statement
        | 
    '''

def p_while_statement(p):
    '''
    while_statement : WHILE condition DO statement
    '''

def p_for_statement(p):
    '''
    for_statement : FOR IDENT ASSIGN expression TO expression DO statement
    '''

def p_proc_call_statement(p):
    '''
    proc_call_statement : proc_call_name
    '''

def p_proc_call_name(p):
    '''
    proc_call_name : IDENT
    '''

def p_block_statement(p):
    '''
    block_statement : BEGIN statement_list END
    '''

def p_read_statement(p):
    '''
    read_statement : READ LPAREN IDENT RPAREN
    '''

def p_write_statement(p):
    '''
    write_statement : WRITE LPAREN expression RPAREN
    '''

def p_null_statement(p):
    '''
    null_statement : 
    '''

def p_condition(p):
    '''
    condition : expression EQ expression
        | expression NEQ expression
        | expression LT expression
        | expression LE expression
        | expression GT expression
        | expression GE expression
    '''

def p_expression(p):
    '''
    expression : term
        | MINUS term
        | expression PLUS term
        | expression MINUS term
    '''

def p_term(p):
    '''
    term : f_actor
        | term MULT f_actor
        | term DIV f_actor
    '''

def p_f_actor(p):
    '''
    f_actor : var_name
        | number
        | LPAREN expression RPAREN
    '''

def p_var_name(p):
    '''
    var_name : IDENT
    '''

def p_number(p):
    '''
    number : NUMBER
    '''

def p_id_list(p):
    '''
    id_list : IDENT
        | id_list COMMA IDENT
    '''



#################################################################
# 構文解析エラー時の処理
#################################################################

def p_error(p):
    if p:
        # p.type, p.value, p.linenoを使ってエラーの処理を書く
        print(f"Syntax error: invalid syntax {p.value} type {p.type} at line {p.lineno}")
    else:
        print("Syntax error at EOF")

#################################################################
# メインの処理
#################################################################

if __name__ == "__main__":
    lexer = lex.lex(debug=0)  # 字句解析器
    yacc.yacc()  # 構文解析器

    # ファイルを開いて
    data = open(sys.argv[1]).read()
    # 解析を実行
    yacc.parse(data, lexer=lexer)
