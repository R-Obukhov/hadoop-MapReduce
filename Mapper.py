import sys
import string

for line in sys.stdin:
	line = line.strip()
	#delete punctuations
	line = line.translate(None, string.punctuation)
	words = line.split()
	
	for word in words:
		if word in words:
			print '%s\t%s' % (word.lower(), 1) 
			#word.lower() is lowercase string correction