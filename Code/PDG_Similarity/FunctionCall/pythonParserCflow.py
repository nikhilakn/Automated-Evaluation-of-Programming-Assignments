import sys

funListWithLevel = []
with open(sys.argv[1],"r") as fin:
	for line in fin:
		countWhiteSpace = len(line) - len(line.lstrip(' '))
		level = countWhiteSpace/4
		funName = ""
		for char in line.lstrip(' '):
			if(char=="("):
				break
			funName += char
		funListWithLevel.append((funName,level))

	for (fun,level) in funListWithLevel:
		print fun,level		
