Schemoji

An emoji-based language structured on Scheme's syntax.

# examples
Check out the tests folder for Scheme (.scm) and Schemoji (.smoji) equivelent files.

# conversion
run convertall.py or src/converter.py to convert between Scheme and Schemoji

# to run
e.x. python -m src.run tests/circle_area.smoji

For Scheme, these files are tested against [Chicken Scheme](https://www.call-cc.org/).

# language rules
The rules are defined in src/mapping.py

# python env
using conda: `conda create --name schemoji --file env.txt`

# thanks
Peter Norvig and his wonderful walkthroughs of writing [lispy.py](http://norvig.com/lispy.html). This project uses a lot of code from lispy.py
