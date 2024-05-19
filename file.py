import sys

from sayings import hello
from sayings import goodbye

if len(sys.argv)>2:
    goodbye(sys.argv[1])
if len(sys.argv)>2:
    hello(sys.argv[1])

for arg in sys.argv[1:]:
    goodbye(arg)
for arg in sys.argv[1:]:
    hello(arg)
