#Graph Constructor
def constructor (file_contents):
    vertices_num,edges_num=file_contents[0].split()
    edges_num=int(edges_num)
    vertices_num=int(vertices_num)
    adj_list = [{} for _ in range(vertices_num)]


    for i in range (0,edges_num):
        src, des, weight=file_contents[i+1].split()
        adj_list[int(src)][int(des)]=int(weight)
        adj_list[int(des)][int(src)]=int(weight)


    return adj_list,vertices_num

x=["4 5","0 2 10","1 0 1","0 3 5","3 1 1","2 3 4"]
a,b=constructor(x)
print(b)
print(a)
#Degree Centrality
def DegreeCenterality (adj_list,vertices_num):
    degree_centrality={}

    for i in range (vertices_num):
        degree_centrality[i]=len(adj_list[i])


    return degree_centrality
