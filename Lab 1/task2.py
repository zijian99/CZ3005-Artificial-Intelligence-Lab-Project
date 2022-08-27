#Task 2: You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve
#the NYC instance.
#
#Uniform Cost Search

def UCS_EConstraint(start,end,G,Dist,ECost,MaxECost):
    
    #priority queue
    #[Total distance from start to current node,Energy cost of the node,Parent node index,Current Node index]
    queue=[[0,0,-1,start]]
    #shortest path memory
    path=[]
    #visited node
    visited=[]
    
    while(len(queue)>0):
        
        queue = sorted(queue)
        tt_dist,cost,parent_node,cur_node = queue.pop()
        #print("node"+cur_node)
        #save path
        #print("len queue"+str(len(queue)))
        path.append([tt_dist,cost,parent_node,cur_node])

        tt_dist *= -1
        

        #------------------------------------------------------------------
        #print(cur_node==end)
        if(cur_node==end):
            
            pathString=end

            for i in range (len(path)-1,-1,-1):
                if path[i][3] == parent_node:
                    # String format= parent node+parent node +......+end
                    pathString = parent_node+ "->" + pathString
                    parent_node=path[i][2]

            #Write answer to txt file
            with open('Task2_Output.txt', 'w') as f:
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
        if cur_node in visited:
            continue

        
        
        for i in range(len(G[cur_node])):
            if G[cur_node][i] not in visited:
                
                #Dist[cur_node,next_node]
                total_distance = tt_dist + Dist["{},{}".format(int(cur_node),int(G[cur_node][i]))]
                #Cost[cur_node,next_node]
                c = cost + ECost["{},{}".format(int(cur_node),int(G[cur_node][i]))]

                # value is multiplied by -1 so that
                # least priority is at the top(can be deleted from the queue first)
                # IF Energy required exceeed limit we don't put into queue
                if c<MaxECost:
                    queue.append([total_distance*-1,c,cur_node,G[cur_node][i]])
        visited.append(cur_node)
        
        #-----------------------------------------------------------------------------------

