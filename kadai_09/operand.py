# -*- coding: utf-8 -*-

from enum import Enum

class OType(Enum):
    GLOBAL_VAR   = 0    # 大域変数（@x, @y など）
    NAMED_REG    = 1    # 名前付きレジスタ（%m, %n など）
    NUMBERED_REG = 2    # 番号付きレジスタ（%1, %2 など）
    CONSTANT     = 3    # 定数
    LABEL        = 4    # ラベル

class Operand(object):
    '''
    Operandクラス
        大域変数，レジスタ，定数を表現
    '''

    def __init__(self, type:OType, name:str=None, val:int=None):
        self.type = type    # タイプ: OType
        self.name = name    # 名前: str
        self.val = val      # 番号/値: int
        if self.val and self.type == OType.LABEL:
            self.name = f'L{val}'

    def __str__(self):
        if self.type == OType.GLOBAL_VAR:
            return f"@{self.name}"
        elif self.type == OType.NAMED_REG:
            return f"%{self.name}"
        elif self.type == OType.NUMBERED_REG:
            return f"%{self.val}"
        elif self.type == OType.CONSTANT:
            return str(self.val)
        elif self.type == OType.LABEL:
            return f"%L{self.val}"
