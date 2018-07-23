import sys

from . import schemoji

def run(filename):

    with open(filename) as f:
        program = f.read()
    
    parsed = schemoji.parse(program)
    schemoji.eval(parsed)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('need one arg: filename')
        sys.exit(1)
    filename = sys.argv[1]
    run(filename)