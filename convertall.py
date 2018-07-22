import os

from src import converter

scheme_files = [f for f in os.listdir('tests') if f.endswith('.scm')]

for f in scheme_files:
    print('converting %s' % f)
    converter.convert('tests/%s' % f)
