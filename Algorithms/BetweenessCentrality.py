
def lastelement(element):
	return element[-1]

def AllSimplePaths(originNode,targetNode,adj_list):
	currentPath = [originNode]
	usedNodes=[originNode]
	answerPaths=[]
	return getAllSimplePaths(targetNode,currentPath,usedNodes,adj_list,answerPaths)	
 
def getAllSimplePaths(targetNode,currentPath,usedNodes,adj_list,answerPaths):
	weight=0
	lastNode = currentPath[-1]
	if lastNode == targetNode:
		for i in range(len(currentPath)):
			if currentPath[i] != currentPath[-1] :
				weight+=adj_list[currentPath[i]][currentPath[i+1]]
    	
		currentPath.append(weight)
		answerPaths.append(list(currentPath))
		currentPath.pop()
		 	
	else:
		for neighbor in adj_list[lastNode]:
			if neighbor not in usedNodes:
				currentPath.append(neighbor)
				usedNodes.append(neighbor)
				getAllSimplePaths(targetNode,currentPath,usedNodes,adj_list,answerPaths)
				usedNodes.remove(neighbor)
				currentPath.pop()
	return answerPaths
   
def numShortestPaths (answerPaths):		
	numberpaths=0
	answerPaths.sort(key=lastelement)
	weight=answerPaths[0][-1]
	for i in answerPaths:
		if i[-1]==weight :
			numberpaths+=1

	return numberpaths
	
def numShortestPathsWithNode(Paths,Node,numpaths):
	numpathsWnode = 0
	for i in range(numpaths):
		temp=Paths[i][-1]
		Paths[i].pop()
		if Node in Paths[i] and Node != Paths[i][0] and Node != Paths[i][-1] :
			numpathsWnode+=1
		Paths[i].append(temp)
	return numpathsWnode

def BetweenessCentralityInternal(Node,adj_list):
	g=0
	for i in range(len(adj_list)-1):
		for j in range(i+1,len(adj_list)):
			Paths=AllSimplePaths(i,j,adj_list)
			numpaths = numShortestPaths(Paths)
			numWithNode = numShortestPathsWithNode(Paths,Node,numpaths)
			g+= (1.000000000000*numWithNode)/numpaths	

	return g



#Printing betweeness centrality
#creating list for the result
def BetweenessCentrality(adj_list):
	betweeness_centrality=[]
	for i in range(vertices_num):
		g=BetweenessCentralityInternal(i,adj_list)
		betweeness_centrality.append('%.12f' % g)
		print('%.12f' % g)
	return betweeness_centrality
