# -------
# imports
# -------

import sys
import random

# ----
# main
# ----

if __name__ == "__main__" :
	print("start")
	sys.stdout.write("start")
	a = random.random()*1000000
	b = random.random()*1000000
	while a == 1000000:
		a = random.random()*1000000
	while b == 1000000:
		b = random.random()*1000000

	sys.stdout.write(a + " " + b + "\n")