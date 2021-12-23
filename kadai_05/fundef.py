# -*- coding: utf-8 -*-

class Fundef(object):
    '''
    関数定義クラス
    '''

    def __init__(self, name, type='void'):
        self.name  = name		# 関数名
        self.rettype = type		# 返り値の型名（'i32' or 'void'）
        self.codes = []			# LLVMコード列（LLVMCodeサブクラスのオブジェクトリスト）
        self.cntr  = 1			# レジスタ番号カウンタ

    def getNewRegNo(self):
        ''' レジスタ番号の取得 '''
        t = self.cntr
        self.cntr += 1
        return t

    def print(self, fp):
        ''' 関数定義の出力 '''
        print(f"define {self.rettype} @{self.name}() {{", file=fp)
        for l in self.codes:
            print(f"    {l}", file=fp)
        print("}\n", file=fp)
