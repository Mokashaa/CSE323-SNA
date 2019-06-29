#Graph Constructor
def	dijkstra(node,vertices_num,adj_list):

	dist = [100000000 for i in range(vertices_num)]
	parent = [-1 for i in range(vertices_num)]
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


def ClosenessCentrality (vertices_num,adj_list):
    closeness_centrality = {}
    for i in range(vertices_num):
        distance,parent = dijkstra (i,vertices_num,adj_list)
        distance_sum = sum(distance)
        closeness_centrality[i]=(vertices_num-1)/distance_sum
        
    return closeness_centrality
	
