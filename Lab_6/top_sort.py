'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 25, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 6 Kruskal and Topological Sort (3 0f 3)
TA: Gerardo Barraza
Purpose: To practice using graphs to implement
Kruskal's Algorithm and Topological Sort.
'''
#Imports the default dictionary from collections so that it can be used in the topological sort costructor
from collections import defaultdict
#Class to represent a graph 
class Topsort: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
 
    #Method that adds an edge to the graph to be used for topological sort. 
    def add_edge(self,u,v): 
        self.graph[u].append(v) 
  
    #Method used as a recursive function to apply the rules of the topological sorting 
    def topological_sort_utility(self,v,visited,stack): 
        # Marks the current node visited as visited. 
        visited[v] = True
        #For i in range of the graph,if the visited is false, then recall itself over again
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topological_sort_utility(i,visited,stack) 
        # Push the current vertex to the stack which will store the results 
        stack.insert(0,v) 
        
    #Method that sorts the stack to be constructed using topological sort
    def topological_sort(self): 
        #Makes a list called visited, and marks them all as false as we havent began to traverse through the methods yet
        visited = [False]*self.V 
        #Marks our stack that we will use to store our values
        stack =[] 
        #For i in range of all vertices, if the visited edge is falsem it will store that edge using the utility method
        for i in range(self.V): 
            if visited[i] == False: 
                self.topological_sort_utility(i,visited,stack) 
        #Finally, it will print out the contents of the stack to the displayed the final sort 
        print("Construction Complete!")
        print("Here are the results of the Topological Sort of the given graph: ")
        print(stack)
        print("")
        
