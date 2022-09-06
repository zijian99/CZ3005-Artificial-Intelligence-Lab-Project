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

    #priority queue
    #[Astar Cost=f(n)=g(n)+h(n),Total distance from start to current node,Energy cost of the node,Parent node index,Current Node index]
    #g(n)=UCS cost to current node
    #h(n)=pt to pt distance from start to current node
    queue=[[0+pt_ptDist(Coord,start,start),0,0,-1,start]]
    #shortest path memory
    path=[]
    #visited node
    visited=[]
    cost_dict={start:0}
    while(len(queue)>0):
        
        queue = sorted(queue,key=lambda x:x[0])
        astar_cost,tt_dist,cost,parent_node,cur_node = queue.pop()
        #save path
        path.append([parent_node,cur_node])
        astar_cost *= -1
        
        #------------------------------------------------------------------
        if(cur_node==end):

            pathString=end

            for i in range (len(path)-1,-1,-1):
                if path[i][1] == parent_node:
                    # String format= parent node+parent node +......+end
                    pathString = parent_node+ "->" + pathString
                    parent_node=path[i][0]

            #Write answer to txt file
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
            #Dist[cur_node,next_node]
            total_distance = tt_dist + Dist["{},{}".format(int(cur_node),int(G[cur_node][i]))]
            #Cost[cur_node,next_node]
            c = cost + ECost["{},{}".format(int(cur_node),int(G[cur_node][i]))]
            astar = total_distance + pt_ptDist(Coord,end,"{}".format(G[cur_node][i]))
            if G[cur_node][i] not in visited or cost_dict[G[cur_node][i]]>c:
                
                
                

                # Astar cost(g(n)+h(n)) value is multiplied by -1 so that
                # least priority is at the top(can be deleted from the queue first)
                # IF Energy required exceeed limit we don't put into queue
                if c<MaxECost:
                    queue.append([astar*-1,total_distance,c,cur_node,G[cur_node][i]])
                    cost_dict[G[cur_node][i]] = c

            
        #-----------------------------------------------------------------------------------
