import re
import argparse

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("word", help="The word that you're searching for in the file.")	
	parser.add_argument("fname", help="The file that you're searching..")

	args = parser.parse_args()

	searchFile = open(args.fname)
	lineNum = 0

	for line in searchFile.readlines():
		line = line.strip('\n\r')
		lineNum += 1

		searchResult = re.search(args.word, line, re.M|re.I)
		if searchResult:
			print(str(lineNum) + ": \t" + line)

if __name__ == '__main__':
	Main()	
