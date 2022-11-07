# CZ3005-Artificial-Intelligence-Lab-Project
SEM2020/2021 Year 3 CZ3005 Artificial Intelligence Lab Project

# Lab 1

Lab 1 involves 3 tasks oriented around the shortest path problem: given a network of nodes, find the shortest distance between a specified start and end node.

## Task 1 - Shortest Path Problem
The shortest path problem can be solved using Uniform-Cost Search. Uniform-Cost Search uses the cost function:

g(n) = Shortest distance of node from source

g(n) is used to evaluate the best candidate node to visit in a priority queue of neighbouring nodes. 

## Task 2 - Constrained Shortest Path Problem (Uninformed Search)
Similar to Task 1, UCS can be used, but with an additional constraint, which is the energy budget; each traversal to a node costs a certain energy budget which cannot be exceeded during the path to the end node. This problem is known to be **NP-Hard [1].**

However, the issue with using UCS as-is is that the final solution may not be the path with the least distance; this happens when UCS chooses a node that has the least total distance from source at a particular instance, but the shortest path through that node may exceed the energy capacity, leading to the next best alternative within that path that does not exceed the energy budget. 

This means that UCS can miss out on paths that are not the most optimal but with low energy cost requirement, but would otherwise be the optimal path that adheres to the energy cost requirement as it visits the lowest cost nodes first.

Thus, we are required to revisit entries in the queue (even if the nodes have been visited by the current path) which may have been deemed to have a larger distance cost in the beginning, but may later lead to the optimal shortest path within the energy constraints.

## Task 3 - Constrained Shortest Path Problem (Informed Search)
A* Search algorithm uses a combination of uniform search cost and heuristics to make decisions. What kind of heuristic function is implemented is dependent on the problem context, and it is important to choose the heuristic function well. 

In this problem, we are given the x-y coordinates of the nodes; this information can be used to derive a well-known heuristic for pathfinding problems, the Euclidean distance between two nodes. 

The Euclidean distance, also known as the Pythagorean distance, refers to the length of a straight line segment between two points [2]. It is easily calculated for two points using their x-y coordinates using the following formula:

$D = \sqrt{(x_{1}^{2}-x_{2}^{2})+(y_{1}^{2}-y_{2}^{2})}$ , where (x1, y1) and (x2, y2) are coordinates of point 1 and point 2 respectively.

In the context of this problem, the euclidean distance that we are interested in is that of between any candidate nodes and the goal node; those with a shorter euclidean distance to the goal are deemed to be better choices for expansion. Thus, we can use the Euclidean distance function directly to be h(n), the heuristic cost function of the A* function.

The final A* cost function is of the form f(n) = g(n) + h(n), where g(n) is the shortest distance of the candidate node from the source, and h(n) is the euclidean distance between the candidate node and the end node.

## References
[1] Garey, Michael R., and David S. Johnson.“Computers and intractability: a guide to NP-
completeness.” (1979).  
[2] Bogomolny, A., n.d. The Distance Formula. [online] Cut-the-knot.org. Available at: <https://www.cut-the-knot.org/pythagoras/DistanceFormula.shtml> [Accessed 7 September 2022].



# Lab 2

Lab 2 involves exercises to specify each of them as a declarative knowledge base in Prolog.

## Exercise 1
The Smart Phone Rivalry

## Exercise 2
The Royal Family



