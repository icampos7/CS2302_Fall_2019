'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 25, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 6 Kruskal and Topological Sort (2 0f 3)
TA: Gerardo Barraza
Purpose: To practice using graphs to implement
Kruskal's Algorithm and Topological Sort.
'''
#Creates the node values necessary to use kruskal's algorithm
class kruskal: 
    def __init__(self,vertices): 
        self.V= vertices  
        self.graph = []
   
    #Method that sorts the graph to be constructed using kruskal's algorithm
    def Kruskal_al(self): 
        #This will store the resultant edges into a list to be used later
        list = [] 
        #Indexes used for keeping track of the sorted edges and for the list[]
        i_edge = 0 
        i_list = 0 
        #Will sort all the edges in an non-decreasing order of their respective weight.
        self.graph =  sorted(self.graph,key=lambda item: item[2])       
        #Creates two new sets called parent and ranked that keep the values of their respective variables 
        parent = [] 
        ranked = [] 
        # Create a set of subsets of rank of the maximum vertices V with single elements as placebos
        for i in range(self.V): 
            parent.append(i) 
            ranked.append(0)     
        # While the number of edges to be taken is equal to V-1, it will select the smallest edge and increase its index 
        while i_list < self.V -1 : 
            From,To,weight =  self.graph[i_edge] 
            i_edge = i_edge + 1
            x = self.find(parent, From) 
            y = self.find(parent ,To) 
            # If including this particular edge doesn't cause a cycle, it will include it in the result and increment its index for the result of the next edge, otherwise it will discard it
            if x != y: 
                i_list = i_list + 1     
                list.append([From,To,weight]) 
                self.union(parent, ranked, x, y)                   
        #Will print the results gathered form the class, including the edges and their respected weights 
        print("Construction Complete!")
        print("Here are the resulting edges:")
        print("")
        for From,To,weight in list:  
            print("Edge: ", From, "---", To, "Weight: ", weight)
        print("")

    # Method that serves as a function of uniting two sets x and y to form a singular set
    def union(self, parent, ranked, x, y):
        #Creates two roots from their respective sets to traverse 
        x_root = self.find(parent, x) 
        y_root = self.find(parent, y) 
        #Replace an object in order of ascending depending of the root of each set; if they are the same rank, then make them one as a root and increment its rank by a value one 
        if ranked[x_root] < ranked[y_root]: 
            parent[x_root] = y_root
        elif ranked[x_root] > ranked[y_root]: 
            parent[y_root] = x_root 
        else : 
            parent[y_root] = x_root
            ranked[x_root] += 1
            
    #Method that adds an edge to the graph to be used for kruskals algorithm. 
    def addEdge(self,u,v,w):
        #Prints out the current edge being added to the graph
        print("Adding an edge from",u,"to",v,",with a weight of",w)
        self.graph.append([u,v,w])
        
    #Metod that uses a utility function to find set of an element i using a parent as its index  
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i])   