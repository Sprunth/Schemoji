import sys

from .schemoji import parse

def run(filename):

    with open(filename) as f:
        program = f.read()
    print ('read in')
    print(program.replace('\n', ''))
    
    print(parse(program))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('need one arg: filename')
        sys.exit(1)
    filename = sys.argv[1]
    run(filename)