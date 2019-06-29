#Closeness Centrality
closeness_centrality = {}
for i in range(vertices_num):
	distance_sum = 0
	distance,parent = dijkstra (i)
	for x in range(vertices_num):
		distance_sum += int(distance[x])
	closeness_centrality[i] = (vertices_num-1)/distance_sum

for i in range(vertices_num):
	print(closeness_centrality[i])
