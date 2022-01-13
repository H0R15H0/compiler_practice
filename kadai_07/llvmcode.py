# -*- coding: utf-8 -*-

from enum import Enum
from operand import Operand

##
## 比較演算子の種類
##
class CmpType(Enum):
    EQ  = 0    # eq  (=)
    NE  = 1    # ne  (<>)
    SGT = 2    # sgt (>， 符号付き)
    SGE = 3    # sge (>=，符号付き)
    SLT = 4    # slt (<， 符号付き)
    SLE = 5    # sle (<=，符号付き)

    @classmethod
    def getCmpType(cls, op):
        if   op == '=':		return CmpType.EQ
        elif op == '<>':	return CmpType.NE
        elif op == '>':		return CmpType.SGT
        elif op == '>=':	return CmpType.SGE
        elif op == '<':		return CmpType.SLT
        elif op == '<=':	return CmpType.SLE

    def __str__(self):
        if   self == CmpType.EQ:	return "eq"
        elif self == CmpType.NE:	return "ne"
        elif self == CmpType.SGT:	return "sgt"
        elif self == CmpType.SGE:	return "sge"
        elif self == CmpType.SLT:	return "slt"
        elif self == CmpType.SLE:	return "sle"

##
## LLVMコード
##
class LLVMCode(object):
    def __init__(self):
        pass


class LLVMCodeGlobal(LLVMCode):
    ''' global 命令
            @{name} = common global i32 0, align 4
    '''

    def __init__(self, name:str):
        super().__init__()
        self.name  = name

    def __str__(self):
        return f"@{self.name} = common global i32 0, align 4"


class LLVMCodeStore(LLVMCode):
    ''' store 命令
            store i32 {argval}, i32* {ptr}, align 4
    '''
    def __init__(self, val:Operand, ptr:Operand):
        super().__init__()
        self.argval = val
        self.ptr = ptr

    def __str__(self):
        return f"store i32 {self.argval}, i32* {self.ptr}, align 4"


class LLVMCodeLoad(LLVMCode):
    ''' load 命令
            {retval} = load i32, i32* {ptr}, align 4
    '''

    def __init__(self, retval:Operand, ptr:Operand):
        super().__init__()
        self.retval = retval
        self.ptr = ptr

    def __str__(self):
        return f"{self.retval} = load i32, i32* {self.ptr}, align 4"


class LLVMCodeAdd(LLVMCode):
    ''' add 命令
            {retval} = add nsw i32 {arg1}, {arg2}
    '''

    def __init__(self, retval:Operand, arg1:Operand, arg2:Operand):
        super().__init__()
        self.retval = retval
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f"{self.retval} = add nsw i32 {self.arg1}, {self.arg2}"


class LLVMCodeSub(LLVMCode):
    ''' sub 命令
            {retval} = sub nsw i32 {self.arg1}, {self.arg2}
    '''

    def __init__(self, retval:Operand, arg1:Operand, arg2:Operand):
        super().__init__()
        self.retval = retval
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f"{self.retval} = sub nsw i32 {self.arg1}, {self.arg2}"


class LLVMCodeMul(LLVMCode):
    ''' mul 命令
            {retval} = mul nsw i32 {arg1}, {arg2}"
    '''

    def __init__(self, retval:Operand, arg1:Operand, arg2:Operand):
        super().__init__()
        self.retval = retval
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f"{self.retval} = mul nsw i32 {self.arg1}, {self.arg2}"


class LLVMCodeDiv(LLVMCode):
    ''' sdiv 命令
            {retval} = sdiv i32 {arg1}, {arg2}
    '''

    def __init__(self, retval:Operand, arg1:Operand, arg2:Operand):
        super().__init__()
        self.retval = retval
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f"{self.retval} = sdiv i32 {self.arg1}, {self.arg2}"

class LLVMCodeCmp(LLVMCode):
    ''' cmp 命令
            {retval} = icmp {cmptype} i32 {arg1} {arg2}
    '''

    def __init__(self, retval:Operand, cmptype:CmpType, arg1:Operand, arg2:Operand):
        super().__init__()
        self.retval = retval
        self.cmptype = cmptype
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f"{self.retval} = icmp {self.cmptype} i32 {self.arg1}, {self.arg2}"

class LLVMCodeBr(LLVMCode):
    ''' br 命令
            br i1 {arg}, label {label1}, label {label2}
            br label {label1}
    '''

    def __init__(self, label1:Operand, label2:Operand=None, arg:Operand=None):
        super().__init__()
        self.arg = arg
        self.label1 = label1
        self.label2 = label2

    def __str__(self):
        if self.label2:
            return f"br i1 {self.arg}, label {self.label1}, label {self.label2}"
        else:
            return f"br label {self.label1}"

class LLVMCodeLabel(LLVMCode):
    ''' label
            {arg}:
    '''

    def __init__(self, arg:Operand):
        super().__init__()
        self.arg = arg

    def __str__(self):
        return f"{self.arg.name}:"

class LLVMCodeAlloca(LLVMCode):
    ''' alloca
            {arg} = alloca i32, align 4
    '''

    def __init__(self, arg:Operand):
        super().__init__()
        self.arg = arg

    def __str__(self):
        return f"{self.arg} = alloca i32, align 4"

class LLVMCodeRet(LLVMCode):
    ''' ret 命令
            ret void
            ret i32 {val}
    '''

    def __init__(self, type:str, val:Operand=None):
        super().__init__()
        self.type = type
        self.val = val

    def __str__(self):
        if self.type == 'i32':
            return f"ret i32 {self.val}"
        else:
            return "ret void"

class LLVMCodeCall(LLVMCode):
    ''' call命令
            call {type} {proc}
    '''
    
    def __init__(self, type:str, proc:Operand, args:list=[]):
        super().__init__()
        self.type = type
        self.proc = proc
        self.args = args

    def __str__(self):
        # print(self.args)
        if len(self.args) == 0:
            return f"call {self.type} {self.proc}()"
        else:
            return f"call {self.type} {self.proc}({', '.join([f'i32 {arg}' for arg in self.args])})"


class LLVMCodeCallPrintf(LLVMCode):
    ''' printf関数呼び出し専用の call命令
            {res} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 {arg})
    '''

    @classmethod
    def printFormat(cls, fp):
        # printf関数に与える書式文字列
        print(r'@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1', file=fp)

    @classmethod
    def printDeclare(cls, fp):
        # printf関数の宣言
        print('declare i32 @printf(i8*, ...)', file=fp)

    def __init__(self, res:Operand, arg:Operand):
        super().__init__()
        self.res = res
        self.arg = arg

    def __str__(self):
        return f"{self.res} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 {self.arg})"


class LLVMCodeCallScanf(LLVMCode):
    ''' scanf関数呼び出し専用の call命令
             {res} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* {arg})
    '''

    @classmethod
    def printFormat(cls, fp):
        # scanf関数に与える書式文字列
        print(r'@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1', file=fp)

    @classmethod
    def printDeclare(cls, fp):
        # scanf関数の宣言
        print('declare i32 @scanf(i8*, ...)', file=fp)

    def __init__(self, res:Operand, arg:Operand):
        super().__init__()
        self.res = res
        self.arg = arg

    def __str__(self):
        return f"{self.res} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* {self.arg})"

