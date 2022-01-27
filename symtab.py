# -*- coding: utf-8 -*-

from enum import Enum

class Scope(Enum):
    ''' Scopeクラス
            記号のタイプを表現
    '''
    GLOBAL_VAR = 0    # 大域変数
    LOCAL_VAR  = 1    # 局所変数
    PROC       = 2    # 手続き 及び 関数
    PARAM      = 3    # 仮引数


class Symbol(object):
    ''' Symbolクラス
            記号（変数，手続き）の情報を表現
    '''

    def __init__(self, name:str, scope:Scope, begin:int=None, end:int=None):
        self.name = name     # 名前 : str
        self.scope = scope   # スコープ : Scope
        self.begin = begin   # 配列の始まり : int
        self.end = end       # 配列の終わり : int

    def __str__(self):
        return f"({self.name},{self.scope}{','.join([str(i) for i in ['', self.begin, self.end] if i != None])})"

    def __repr__(self):
        return str(self)


class SymbolTable(object):
    ''' SymbolTableクラス
            記号表とその操作関数を定義
    '''

    def __init__(self):
        self.rows = []

    def __str__(self):
        return f"[{', '.join([str(sym) for sym in self.rows])}]"

    def insert(self, symbol:Symbol):
        ''' 記号表への変数・手続きの登録 '''
        print("-- insert --")
        self.rows.append(symbol)
        print(self.rows)


    def lookup(self, name:str) -> Symbol:
        print("-- lookup --")
        ''' 変数・手続きの検索 '''
        for symbol in self.rows[::-1]:
            if symbol.name == name:
                print(symbol)
                return symbol

    def delete(self):
        ''' 記号表から局所変数の削除 '''
        print("-- delete --")
        self.rows = [symbol for symbol in self.rows if symbol.scope != Scope.LOCAL_VAR and symbol.scope != Scope.PARAM]
        print(self.rows)


if __name__ == "__main__":
    symbol_table = SymbolTable()
    s = Scope(1)
    symbol = Symbol("hoge", s)
    symbol_table.insert(symbol)
    symbol = Symbol("hogehoge", s)
    symbol_table.insert(symbol)
    print(symbol_table.lookup("hoge"))
    print(symbol_table.lookup("hogehoge"))
    symbol_table.delete()
    print(symbol_table.lookup("hoge"))
    print(symbol_table.lookup("hogehoge"))
