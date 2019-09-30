import math
import random
class node:
    def __init__(self, id, x, y, conns):
        self.id = id
        self.x = x
        self.y = y
        self.conns = conns
class map:
    def __init__(self, nodes):
        self.nodes = nodes

    def findNode(self, id):
        for node in self.nodes:
            if node.id == id:
                return node

def getDist(node1, node2):
    dist = math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)
    return dist

class tspHillClimbing:
    def __init__(self, map):
        self.map = map
        self.solution = []
        self.startNode = "-999"
        self.goalTestRequests = 0
        self.goalTestsExceeded = False

    def randomStartNode(self):
        i = random.randint(0,len(self.map.nodes) - 1)
        self.startNode = self.map.nodes[i].id

    def getUphillNode(self, node):
        neighbors = []
        neighborsObjective =[]
        neighborsDist = []
        ineighbors = []
        ineighborsObjective = []
        ineighborsDist = []
        for id in node.conns:
            #print(id)
            neighborNode = self.map.findNode(id)
            neighbors.append(neighborNode)
            neighborsObjective.append(1 - self.solution.count(id))
            neighborsDist.append(getDist(node, neighborNode))

        indexes = [i for i, j in enumerate(neighborsObjective) if j == max(neighborsObjective)]

        for i in range(0,len(indexes)):
            ineighbors.append(neighbors[indexes[i]])
            ineighborsObjective.append(neighborsObjective[indexes[i]])
            ineighborsDist.append(neighborsDist[indexes[i]])
        index = ineighborsDist.index(min(ineighborsDist))
        return ineighbors[index]

    def goalTest(self):
        self.goalTestRequests = self.goalTestRequests + 1
        if self.goalTestRequests >= 100:
            self.goalTestsExceeded = True
        for node in self.map.nodes:
            if not node.id in self.solution:
                return False
        return True

    def solve(self):
        path = []
        goalTest = False
        node = self.map.findNode(self.startNode)
        self.solution.append(node.id)
        goalTest = self.goalTest()


        while not goalTest and not self.goalTestsExceeded:
            node = self.getUphillNode(node)
            self.solution.append(node.id)
            goalTest = self.goalTest()
            print(self.solution)
        #self.solution.append(self.solution[0])
        return not self.goalTestsExceeded

    def totalDist(self):
        totDist = 0
        for i in range(0,len(self.solution)-1):
            node1 = self.map.findNode(self.solution[i])
            node2 = self.map.findNode(self.solution[i+1])
            totDist += getDist(node1,node2)

        return totDist

A = node("A", 0, 0, ["D", "B", "C"])
B = node("B", 5, 0, ["A", "D", "C"])
C = node("C", 2, 5, ["A", "B", "D"])
D = node("D", 3, 2, ["A", "B", "C"])

theMap = map([A,B,C,D])
#print(theMap.findNode("D"))
hillClimbing = tspHillClimbing(theMap)
hillClimbing.randomStartNode()
print(hillClimbing.solve())
print("Total Distance: " + str(hillClimbing.totalDist()))
