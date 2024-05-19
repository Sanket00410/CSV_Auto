import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello," + sys.argv[1])

for arg in sys.argv[1:]:
    cowsay.cow("hello," + arg)