import community
import networkx as nx
import matplotlib.pyplot as plt
import sys
import pickle

edge_list = []
node_list = []
with open(sys.argv[1],"rb") as f:
	for line in f.readlines():
		f1,f2,val = line.split()
		#f1 = int(f1.split('/')[-1].split('.')[0][1:])
		#f2 = int(f2.split('/')[-1].split('.')[0][1:])
		edge_list.append((f1,f2,float(val)))
		node_list.append(f1)
		node_list.append(f2)
node_list = list(set(node_list))
G = nx.Graph()
# print nodes
G.add_nodes_from(node_list)
# G.add_edges_from(array)
G.add_weighted_edges_from(edge_list)


#first compute the best partition
partition= community.best_partition(G)
#print partition

dendo = community.generate_dendrogram(G,None,'weight',1.,False)
# print dendo
testing= community.partition_at_level(dendo, len(dendo) - 1)
#print testing

res = community.modularity(partition,G,'weight');
#print res

list1 = [partition]
cluster_set = set(val for dic in list1 for val in dic.values())
print cluster_set

cluster_set_elements = []
for cluster_id in cluster_set:
	temp_elements = []
	for node,cluster in partition.iteritems():
		if(cluster==cluster_id):
			temp_elements.append(node)
	cluster_set_elements.append(temp_elements)
for cluster_id in xrange(len(cluster_set_elements)):
	print "Cluster:",cluster_id,"\n", cluster_set_elements[cluster_id], "\n"

with open("/home/perseus/Sem-9/Thesis/Code/cluster.pickle","wb") as fin:
	pickle.dump(cluster_set_elements,fin)
#drawing
'''
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
'''
