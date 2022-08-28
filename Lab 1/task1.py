#Task 1: You will need to solve a relaxed version of the NYC instance where we do not have the energy
#constraint. You can use any algorithm we discussed in the lectures. Note that this is equivalent to
#solving the shortest path problem. The solution quality of your algorithm will affect the grade.
#
#
#Uniform Cost Search without energy constraint


def UCSTask1(start,end,G,Dist,ECost):

    # Priority queue
    # The priority queue contains arrays that store information regarding a node:
    # - Total distance from start to the node
    # - Energy cost of the node (Always 0 for Task 1)
    # - Parent node index
    # - Current node index
    queue=[[0,0,-1,start]]
    
    # Shortest path memory: Stores the shortest path
    path=[]
   
    # Visited nodes: Stores the index of the visited nodes
    visited=[]

    while(len(queue)>0):

        # Sort based on the queue total distance (index 0) and pop the first node with highest priority (Shortest distance from source): 
        queue = sorted(queue, key=lambda x: x[0])
        tt_dist,cost,parent_node,cur_node = queue.pop(0) # Obtain info about the popped node

        # Add node to path memory:
        path.append([tt_dist,cost,parent_node,cur_node])
        
        if cur_node in visited:
            continue
        #------------------------------------------------------------------
        # Goal reached:
        if(cur_node==end): 
            pathString=end # String to store the path

            # Start back tracking steps from end node and build the path string:
            for i in range (len(path)-1,-1,-1):
                if path[i][3] == parent_node:
                    # String format= parent node+parent node +......+end
                    pathString = parent_node+ "->" + pathString
                    parent_node=path[i][2]

            #Write answer to txt file f:
            with open('Task1_Output.txt', 'w') as f:
                print('[ Task 1 ] Uniform Cost Search without Energy Constraint Answer:\n')
                print("Shortest path: " +pathString +"\n")
                print("Shortest distance: {}".format(tt_dist) +"\n")
                print("Total energy cost: {}".format(cost) +"\n\n")
                f.write('[ Task 1 ] Uniform Cost Search without Energy Constraint Answer:\n')
                f.write("Shortest path: " +pathString +"\n")
                f.write("Shortest distance: {}".format(tt_dist) +"\n")
                f.write("Total energy cost: {}".format(cost) +"\n\n")
            
            return
        #-----------------------------------------------------------------
        #Goal not yet reached:
        visited.append(cur_node)

        # Check all neighours of cur_node: 
        for i in range (len(G[cur_node])):
            if G[cur_node][i] not in visited:
                # Calculate distance from source to neighbour:
                total_distance = tt_dist + Dist["{},{}".format(int(cur_node),int(G[cur_node][i]))]

                # Calculate energy cost from source to neighbour:
                # Note that this cost is not used in this task, as there is no energy constraint.
                c = cost + ECost["{},{}".format(int(cur_node),int(G[cur_node][i]))]

                queue.append([total_distance,c,cur_node,G[cur_node][i]])

    
        #-----------------------------------------------------------------------------------