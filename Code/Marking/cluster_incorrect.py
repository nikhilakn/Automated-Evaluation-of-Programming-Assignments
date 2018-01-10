import sys
import pickle

cluster_set_elements = []
similarity_measure = []

dict_incorr_val = {}
dict_incorr_val_list = {}
with open(sys.argv[1],"rb") as fin:
	for line in fin.readlines():
		line = line [:-1]
		incorr_name,corr_name,val = line.split()
		try:
			if(dict_incorr_val[incorr_name][1] < float(val)):
				dict_incorr_val[incorr_name][0] = corr_name
				dict_incorr_val[incorr_name][1] = float(val)
		except:
			dict_incorr_val[incorr_name] = [corr_name,float(val)]	

with open(sys.argv[1],"rb") as fin:
	for line in fin.readlines():
		line = line [:-1]
		incorr_name,corr_name,val = line.split()
		if(dict_incorr_val[incorr_name][1] == float(val)):
			try:
				dict_incorr_val_list[incorr_name].append(corr_name)
			except:
				dict_incorr_val_list[incorr_name] = [corr_name]
				dict_incorr_val_list[incorr_name].append(dict_incorr_val[incorr_name][0])
	
with open("/home/perseus/Sem-9/Thesis/Code/cluster.pickle","rb") as fin:
	cluster_set_elements = pickle.load(fin)

for incorr_files in dict_incorr_val_list.keys():
	cluster_id_count_list = [0]*len(cluster_set_elements)
	for cluster_id in xrange(len(cluster_set_elements)):
		#print cluster_id, dict_incorr_val[incorr_files]
		for files in dict_incorr_val_list[incorr_files]: 
			if(files in cluster_set_elements[cluster_id]):
				cluster_id_count_list[cluster_id]+=1
	ans_id = -1	
	max_val_cluster = max(cluster_id_count_list)
	for id1 in xrange(len(cluster_id_count_list)): 
		if(cluster_id_count_list[id1]==max_val_cluster):
			ans_id = id1				
			break
	cluster_set_elements[ans_id].append(incorr_files)
	print ans_id, incorr_files
with open("/home/perseus/Sem-9/Thesis/Code/cluster_w_incorrect.pickle","wb") as fin:
	pickle.dump(cluster_set_elements,fin)		
