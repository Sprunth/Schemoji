# The idea is that we can read the program in order
# keeping track of open/close parentheses and replace them with
# The emoji equivelent 0-9

import sys

from .mapping import *

def prettify_scope(filename):
    
    lines = [line.rstrip('\n') for line in open(filename)]
    open(filename, 'w').close()  # clear file
    
    to_write = []
    
    scope_depth = 0
    for line in lines:
        l = []  # to reconstruct the line
        for c in line:
            if c == EXP_OPEN.m:
                ch = EXP_OPENCLOSE_ALT[min(scope_depth, 10)]
                l.append(ch)
                scope_depth += 1
            elif c == EXP_CLOSE.m:
                scope_depth -= 1
                ch = EXP_OPENCLOSE_ALT[min(scope_depth, 10)]
                l.append(ch)                
            else:
                l.append(c)
        to_write.append(''.join(l))
    
    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(to_write))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('need one arg: filename')
        sys.exit(1)
    
    filename = sys.argv[1]

    prettify_scope(filename)