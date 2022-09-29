import json
import task1
import task2
import task3
import timeit


graph = open(".\G.json")
cost = open(".\Cost.json")
coord = open(".\Coord.json")
dist = open(".\Dist.json")
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
print("----------------------------")
print("Running task 1, please wait.")
task1_time = timeit.timeit("task1.UCSTask1(\"1\",\"50\",G,Dist,Cost)", number=1, globals=locals())
print("----------------------------")
print("Running task 2, please wait. (This may take a while)")
task2_time = timeit.timeit("task2.UCS_EConstraint(\"1\",\"50\",G,Dist,Cost,287932)", number=1, globals=locals())
print("----------------------------")
print("Running task 3, please wait.")
task3_time = timeit.timeit("task3.Astar_EConstraint(\"1\",\"50\",G,Dist,Cost,287932,Coord)", number=1, globals=locals())

data1 = data2 = data3 =""
with open('.\Task1_Output.txt') as fp:
    data1 = fp.read()
with open('.\Task2_Output.txt') as fp:
    data2 = fp.read()
with open('.\Task3_Output.txt') as fp:
    data3 = fp.read()
data  = data1 + data2 + data3
with open ('.\Lab1_Output.txt', 'w') as fp:
    fp.write(data)

print("----------------------------")
print("Execution Time Summary:\n")
print("Task 1: "+str(task1_time)+" seconds\n")
print("Task 2: "+str(task2_time)+" seconds\n")
print("Task 3: "+str(task3_time)+" seconds\n")
