#Task 1: You will need to solve a relaxed version of the NYC instance where we do not have the energy
#constraint. You can use any algorithm we discussed in the lectures. Note that this is equivalent to
#solving the shortest path problem. The solution quality of your algorithm will affect the grade.
#
#
#Uniform Cost Search without energy constraint


def UCSTask1(start,end,G,Dist,ECost):

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
        #save path
        path.append([tt_dist,cost,parent_node,cur_node])
        tt_dist *= -1
        
        if cur_node in visited:
            continue
        #------------------------------------------------------------------
        if(cur_node==end):

            pathString=end

            for i in range (len(path)-1,-1,-1):
                if path[i][3] == parent_node:
                    # String format= parent node+parent node +......+end
                    pathString = parent_node+ "->" + pathString
                    parent_node=path[i][2]

            #Write answer to txt file
            with open('Lab 1\Task1_Output.txt', 'w') as f:
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
        

        visited.append(cur_node)
        
        for i in range (len(G[cur_node])):
            if G[cur_node][i] not in visited:
                #Dist[cur_node,next_node]
                total_distance = tt_dist + Dist["{},{}".format(int(cur_node),int(G[cur_node][i]))]
                #Cost[cur_node,next_node]
                c = cost + ECost["{},{}".format(int(cur_node),int(G[cur_node][i]))]

                # value is multiplied by -1 so that
                # least priority is at the top(can be deleted from the queue first)
                queue.append([total_distance*-1,c,cur_node,G[cur_node][i]])

    
        #-----------------------------------------------------------------------------------