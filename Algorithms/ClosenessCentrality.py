closeness_centrality = {}
for i in range(vertices_num):
	distance,parent = dijkstra (i)
	distance_sum = sum(distance)
	closeness_centrality[i]=(vertices_num-1)/distance_sum
	print('%0.12f' % closeness_centrality[i])
	
