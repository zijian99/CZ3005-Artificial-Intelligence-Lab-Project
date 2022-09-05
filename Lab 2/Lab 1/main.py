import json
import task1
import task2
import task3



graph = open("Lab 1\G.json")
cost = open("Lab 1\Cost.json")
coord = open("Lab 1\Coord.json")
dist = open("Lab 1\Dist.json")
G = json.load(graph)
Cost = json.load(cost)
Coord = json.load(coord)
Dist = json.load(dist)


#queue=[[0,0,-1,1],[-1,0,0,0],[-2,0,0,0]]
# queue =[[["1"],0,0,-1,"1"]]
# print(sorted(queue))
# queue = sorted(queue)
# dist,cost,parent ,node = queue.pop()
# print(dist)
#print(1==1)
task1.UCSTask1("1","50",G,Dist,Cost)
task2.UCS_EConstraint("1","50",G,Dist,Cost,287932)
task3.Astar_EConstraint("1","50",G,Dist,Cost,287932,Coord)

data1 = data2 = data3 =""
with open('Lab 1\Task1_Output.txt') as fp:
    data1 = fp.read()
with open('Lab 1\Task2_Output.txt') as fp:
    data2 = fp.read()
with open('Lab 1\Task3_Output.txt') as fp:
    data3 = fp.read()
data  = data1 + data2 + data3
with open ('Lab 1\Lab1_Output.txt', 'w') as fp:
    fp.write(data)