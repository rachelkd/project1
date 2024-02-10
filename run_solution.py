import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < gameplay4.txt".format(sys.executable))
print(p)
