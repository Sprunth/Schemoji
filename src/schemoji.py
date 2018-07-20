
import math
import operator as op

from mapping import *

Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List
Env    = dict             # A Scheme environment (defined below) is a mapping of {variable: value}

def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens"
    return chars.replace(EXP_OPEN, ' %s ' % EXP_OPEN).replace(EXP_CLOSE, ' %s ' % EXP_CLOSE).split()

def parse(program: str) -> Exp:
    "Read a Schemoji expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == EXP_OPEN:
        L = []
        while tokens[0] != EXP_CLOSE:
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off EXP_CLOSE
        return L
    elif token == EXP_CLOSE:
        raise SyntaxError('unexpected %s' % EXP_CLOSE)
    else:
        return atom(token)

def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)



def standard_env() -> Env:
    "An environment with some Scheme standard procedures."
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        OP_ADD:op.add, OP_SUB:op.sub, OP_MUL:op.mul, OP_DIV:op.truediv, 
        OP_GT:op.gt, OP_LT:op.lt, OP_GE:op.ge, OP_LE:op.le, OP_EQ:op.eq, 
        SC_ABS:     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        SC_BEGIN:   lambda *x: x[-1],
        SC_CAR:     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: List(x), 
        'list?':   lambda x: isinstance(x, List), 
        SC_MAP:     map,
        'max':     max,
        'min':     min,
        SC_NOT:     op.not_,
        SC_NULLQ:   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),  
		SC_PRINT:   print,
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env

global_env = standard_env()
