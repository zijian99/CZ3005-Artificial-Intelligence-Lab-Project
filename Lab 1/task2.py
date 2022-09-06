#Task 2: You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve
#the NYC instance.
#
#Uniform Cost Search

def UCS_EConstraint(start,end,G,Dist,ECost,MaxECost):
    
    # Priority queue
    # The priority queue contains arrays that store information regarding a node:
    # - Total distance from start to the node
    # - Energy cost of the node
    # - Parent node index
    # - Current node index    
    queue=[[0,0,-1,start]]

    # Shortest path memory: Stores the shortest path
    path=[]

    # Visited nodes: Stores the index of the visited nodes
    visited=[]

    # Cost dictionary: Stores the least cost known to reach a visited node
    cost_dict={start:0}

    while(len(queue)>0):
        
        # Sort based on the queue total distance (index 0) and pop the first node with highest priority (Shortest distance from source):  
        queue = sorted(queue,key=lambda x:x[0])
        tt_dist,cost,parent_node,cur_node = queue.pop(0) # Obtain info about the popped node

        # Add node to path memory:
        path.append([tt_dist,cost,parent_node,cur_node])

        #------------------------------------------------------------------

        # Goal Reached:
        if(cur_node==end):
            
            pathString=end
            
            # Start back tracking steps from end node and build the path string: 
            for i in range (len(path)-1,-1,-1):
                if path[i][3] == parent_node:
                    # String format= parent node+parent node +......+end
                    pathString = parent_node+ "->" + pathString
                    parent_node=path[i][2]

            #Write answer to txt file f:
            with open('.\Task2_Output.txt', 'w') as f:
                f.write('[ Task 2 ] Uniform Cost Search with Energy Constraint Answer:\n')
                print('[ Task 2 ] Uniform Cost Search with Energy Constraint Answer:\n')
                print("Shortest path: " +pathString +"\n")
                print("Shortest distance: {}".format(tt_dist) +"\n")
                print("Total energy cost: {}".format(cost) +"\n\n")
                f.write("Shortest path: " +pathString +"\n")
                f.write("Shortest distance: {}".format(tt_dist) +"\n")
                f.write("Total energy cost: {}".format(cost) +"\n\n")
            
            return
        #-----------------------------------------------------------------
        # if cur_node in visited:
        #     continue

        
        
        for i in range(len(G[cur_node])):
            # Calculate distance from source to neighbour: 
            total_distance = tt_dist + Dist["{},{}".format(int(cur_node),int(G[cur_node][i]))]

            # Calculate energy cost from source to neighbour: 
            c = cost + ECost["{},{}".format(int(cur_node),int(G[cur_node][i]))]
            if G[cur_node][i] not in visited or cost_dict[G[cur_node][i]]>c:
                # If Energy required exceeed the limit, we do not put into queue
                if c<MaxECost:
                    queue.append([total_distance,c,cur_node,G[cur_node][i]])
                    cost_dict[G[cur_node][i]] = c
        visited.append(cur_node)
        
        #-----------------------------------------------------------------------------------

