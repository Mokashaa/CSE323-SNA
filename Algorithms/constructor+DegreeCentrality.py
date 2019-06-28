#Graph Constructor
vertices_num,edges_num=input().split()
edges_num=int(edges_num)
vertices_num=int(vertices_num)
adj_list = [{} for _ in range(vertices_num)]


for i in range (edges_num):
    src, des, weight=input().split()
    adj_list[int(src)][int(des)]=int(weight)
    adj_list[int(des)][int(src)]=int(weight)



#Degree Centrality
degree_centrality={}

for i in range (edges_num):
    degree_centrality[i]=len(adj_list[i])


for i in range (edges_num):
    print(degree_centrality[i])
