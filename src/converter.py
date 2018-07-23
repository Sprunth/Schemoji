import os
import sys
from functools import partial

from .mapping import *

def convert(filename):

    to_schemoji = filename.endswith('.scm')

    # conversion map
    cm = {}
    key_name = 'n' if to_schemoji else 'm'
    val_name = 'm' if to_schemoji else 'n'
    for token in master_token_set:
        cm[getattr(token, key_name)] = getattr(token, val_name)

    ext = '.smoji' if to_schemoji else '.scm'
    outfilename = os.path.splitext(filename)[0] + ext

    # read file
    lines = [line.rstrip('\n') for line in open(filename)]

    to_write = []
    for line in lines:
        # do the replacement
        # for schemoji -> Scheme, we need to support the dialer tones too
        if not to_schemoji:
            # first replace the EXP_CLOSE, since we need to check for the ALT dual-char
            for c in EXP_OPENCLOSE_ALT.values():
                line = line.replace('%s%s' % (EXP_CLOSE_ALT_IDENTIFIER, c), EXP_CLOSE.n)
            # then the EXP_OPEN
            for c in EXP_OPENCLOSE_ALT.values():
                line = line.replace(c, EXP_OPEN.n)
        # note, need to do multi-character replacements before single ones
        # e.g. do '>=' first, then '='
        for k,v in cm.items():
            line = line.replace(k, v)        
        to_write.append(line)

    with open(outfilename, 'w') as outfile:
        outfile.write('\n'.join(to_write))
    print('done! written to %s' % outfilename)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('need one arg: filename')
        sys.exit(1)

    filename = sys.argv[1]

    convert(filename)