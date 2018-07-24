import argparse
import os
import sys
from functools import partial

from .mapping import *
from .prettify_scope import prettify_scope

def convert(filename):

    to_schemoji = filename.endswith('.scm')

    # conversion map
    cm = []
    key_name = 'n' if to_schemoji else 'm'
    val_name = 'm' if to_schemoji else 'n'
    for token in master_token_set:
        cm.append( (getattr(token, key_name), getattr(token, val_name)) )

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
        for item in cm:
            k,v = item
            line = line.replace(k, v)
        to_write.append(line)

    with open(outfilename, 'w') as outfile:
        outfile.write('\n'.join(to_write))
    print('done! written to %s' % outfilename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--prettify', action='store_true', default=False)
    args = parser.parse_args()

    convert(args.filename)
    if args.prettify:
        to_schemoji = args.filename.endswith('.scm')
        ext = '.smoji' if to_schemoji else '.scm'
        outfilename = os.path.splitext(args.filename)[0] + ext
        prettify_scope(outfilename)