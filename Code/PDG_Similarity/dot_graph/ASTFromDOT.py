from dot_tools import parse
from dot_tools.dot_graph import SimpleGraph
import pickle
import sys
import warnings
warnings.filterwarnings("ignore")

filename = sys.argv[1]

with open(filename,"r") as fin:
	dotStr = fin.read()
	tree = parse(dotStr)
	g = SimpleGraph.build(tree.kid('Graph'))
	#print g.nodes.keys()
	#print g.edges
	
	try:
		name = filename.split('/')[-1].split('.')[0]
	except:
		name = "pickle_file"
	with open(name+".pickle","wb") as fin:
		pickle.dump(g.nodes.keys(),fin)
		pickle.dump(g.edges,fin)
	
	
