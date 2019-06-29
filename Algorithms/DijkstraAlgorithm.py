import numpy as np

def	dijkstra(node):

	dist = np.full(vertices_num,100000000)
	parent= np.full(vertices_num,-1)
	nodes_queue= [{'src':node ,'dest':node,'weight':0}]
	
	while len(nodes_queue) != 0:
		current_node=nodes_queue[0]['src']
		prev_node=nodes_queue[0]['dest']
		cur_dist=nodes_queue[0]['weight']
		nodes_queue.pop(0)
		if dist[current_node] != 100000000:
			continue
		dist[current_node]=cur_dist
		parent[current_node]=prev_node	
		
		for i in adj_list[current_node]:
			distance=cur_dist+adj_list[current_node][i]
			temp={'src':i ,'dest':current_node,'weight':distance}
			if dist[i] !=100000000:
				continue
			nodes_queue.append(temp.copy())
			
		nodes_queue.sort(key=lambda i: i['weight'])
	
	return dist,parent
