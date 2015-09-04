**Assignemnt 1

#Assignment1 by Patrick Andresen paan2097

class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		if self.items == []:
			return True
		else:
			return False
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def printQueue(self):
		print(self.items[len(self.items)-1])
		
q=Queue()
x=[1,2,3,4,5,6,7,8,9,10]
for x in x:
	q.enqueue(x)
while q.isEmpty() == False:
	q.printQueue() #prints values in the order they are dequeued
	q.dequeue()

class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		if self.items == []:
			return True
		else: 
			return False
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def checkSize(self):
		return len(self.items)
	def printStack(self):
		print(self.items[len(self.items)-1])
        
s = Stack()
y = [11,12,13,14,15,16,17,18,19,20]
for y in y:
	s.push(y)
	s.checkSize()
while s.isEmpty() == False:
	s.printStack() #prints values in the order they are popped
	s.pop()
	
class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


	def add(self,value):
			parentValue = None
			if value < self.value:
				if self.right is None:
					self.right = Node(value)
				else:
					self.right.add(value)
				
			elif value > self.value:
				if self.left is None:
					self.left = Node(value)
				else:
					self.left.add(value)
			elif self.left & self.right != None:
				print("Parent has two children, node not added")
			else:
				self.value = value
	
	def delete(self, value):
		self.value = None			
			
	def printTree(self):
		print self.value
		if self.left:
			self.left.printTree()
		if self.right:
			self.right.printTree()
			
n = Node(0)
n.add(1)
n.add(2)
n.add(3)
n.add(4)
n.add(5)
n.add(6)
n.add(7)
n.add(8)
n.add(9)
n.add(10)
n.printTree()
n.delete(2)
n.delete(0)
n.printTree()
				

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def addVertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = node
        self.vert_dict[node] = new_vertex
        return new_vertex
		

    def findVertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def addEdge(self, value1, value2):
        if value1 not in self.vert_dict:
            self.addVertex(value1)
        if value2 not in self.vert_dict:
            self.addVertex(value2)

g = Graph()

g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)

g.addEdge(1,2)  
g.addEdge(1,3)  
g.addEdge(4,2)  
g.addEdge(5,2)  
g.addEdge(6,3)  
g.addEdge(5,3)  
g.addEdge(7,2)  
g.addEdge(8,2)  
g.addEdge(9,4)  
g.addEdge(8,4)  
g.addEdge(1,5)  
g.addEdge(1,6)  
g.addEdge(5,8)  
g.addEdge(6,8)  
g.addEdge(6,9)  
g.addEdge(7,8)  
g.addEdge(7,9)  
g.addEdge(10,5)  
g.addEdge(10,6)  
g.addEdge(10,3)  

g.findVertex(2)
g.findVertex(4)
g.findVertex(6)
g.findVertex(8)
g.findVertex(10)

