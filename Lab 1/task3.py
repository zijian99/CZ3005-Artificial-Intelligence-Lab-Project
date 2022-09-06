#Task 3: You will need to develop an A* search algorithm to solve the NYC instance. The key is to
#develop a suitable heuristic function for the A* search algorithm in this setting. The solution quality of
#your algorithm will affect the grade. 
#
#
#A* search

from math import sqrt

# Heuristic Function h(n)
def pt_ptDist(Coord,x,y):
    #x-->pt1
    #y-->pt2
    x1 = Coord[x][0]
    y1 = Coord[x][1]
    x2 = Coord[y][0]
    y2 = Coord[y][1]
    return sqrt( pow(y2-y1,2) + pow(x2-x1,2))
    

    
def Astar_EConstraint(start,end,G,Dist,ECost,MaxECost,Coord):

    # Priority queue
    # The priority queue contains arrays that store information regarding a node:
    # - A* Cost=f(n)=g(n)+h(n)
    # - Total distance from start to current node
    # - Energy cost of the node
    # - Parent node index
    # - Current node index
    # g(n)= UCS cost to current node
    # h(n)= pt to pt distance from start to current node
    queue=[[0+pt_ptDist(Coord,start,start),0,0,-1,start]]

    # Shortest path memory: Stores the shortest path
    path=[]

    # Visited nodes: Stores the index of the visited nodes
    visited=[]

    # Cost dictionary: Stores the least cost known to reach a visited node
    cost_dict={start:0}

    while(len(queue)>0):
        
	# Sort based on the queue total distance (index 0) and pop the first node with highest priority (Shortest distance from source):  
        queue = sorted(queue,key=lambda x:x[0])
        astar_cost,tt_dist,cost,parent_node,cur_node = queue.pop(0) # Obtain info about the popped node
	
	# Add node to path memory:
        path.append([parent_node,cur_node])
        
        #------------------------------------------------------------------
	# Goal Reached:
        if(cur_node==end):

            pathString=end
		
	    # Start back tracking steps from end node and build the path string: 
            for i in range (len(path)-1,-1,-1):
                if path[i][1] == parent_node:
                    # String format= parent node+parent node +......+end
                    pathString = parent_node+ "->" + pathString
                    parent_node=path[i][0]

            # Write answer to txt file f:
            with open('.\Task3_Output.txt', 'w') as f:
                print('[ Task 3 ] A* Search with Energy Constraint Answer:\n')
                print("Shortest path: " +pathString +"\n")
                print("Shortest distance: {}".format(tt_dist) +"\n")
                print("Total energy cost: {}".format(cost) +"\n\n")
                f.write('[ Task 3 ] A* Search with Energy Constraint Answer:\n')
                f.write("Shortest path: " +pathString +"\n")
                f.write("Shortest distance: {}".format(tt_dist) +"\n")
                f.write("Total energy cost: {}".format(cost) +"\n\n")
            
            return
        #-----------------------------------------------------------------
        

        visited.append(cur_node)
        
        for i in range (len(G[cur_node])):
            # Calculate distance from source to neighbour: 
            total_distance = tt_dist + Dist["{},{}".format(int(cur_node),int(G[cur_node][i]))]
           
	    # Calculate energy cost from source to neighbour: 
            c = cost + ECost["{},{}".format(int(cur_node),int(G[cur_node][i]))]

	    # Calculate A* Cost:	    
            astar = total_distance + pt_ptDist(Coord,end,"{}".format(G[cur_node][i]))
            if G[cur_node][i] not in visited or cost_dict[G[cur_node][i]]>c:
              
                # If Energy required exceeed the limit, we do not put into queue
                if c<MaxECost:
                    queue.append([astar,total_distance,c,cur_node,G[cur_node][i]])
                    cost_dict[G[cur_node][i]] = c

            
        #-----------------------------------------------------------------------------------
