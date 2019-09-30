import math
import random
class node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return self.id

    def __repr__(self):
        return str(self)

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

def getTotDist(route):
    totDist = 0
    for i in range(0, len(route) - 1):
        totDist += getDist(route[i], route[i + 1])
    return totDist

def getFitness(route):
    totDist = getTotDist(route)
    fitness = 1/float(totDist)
    return fitness
def randomRoute(map):
    route = random.sample(map.nodes,len(map.nodes))
    return route

class population:
    def __init__(self,map, generationSize, mutationRate):
        self.map = map
        self.generationSize = generationSize
        self.mutationRate = mutationRate
        self.population = []
        self.fitness = []
        self.initializeRoutes()
        self.evaluateFitnesses()

    def initializeRoutes(self):
        self.population = []
        for i in range(0,self.generationSize):
            self.population.append(randomRoute(self.map))

    def evaluateFitnesses(self):
        #aPopulation is any list of route
        # route is a list of node
        self.fitness = []
        for route in self.population:
            self.fitness.append(getFitness(route))

    def evaluateFitnessOfList(self,list):
        #aPopulation is any list of route
        # route is a list of node
        fitnesses = []
        for route in list:
            fitnesses.append(getFitness(route))
        return fitnesses

    def getBestRoute(self):
        i = self.fitness.index(self.getFitnessOfBestRoute())
        return self.population[i]
    def getFitnessOfBestRoute(self):
        return (max(self.fitness))

    def getDistOfBestRoute(self):
        return (1/(max(self.fitness)))

    def chooseMates(self):
        #Tournament style selection method
        tournamentSize = int(len(self.population) / 20)
        mateList1 = random.sample(self.population,tournamentSize)
        remainingPopulation = []
        for route in self.population:
            if not route in mateList1:
                remainingPopulation.append(route)
        mateList2 = random.sample(remainingPopulation,tournamentSize)
        fitness1 = self.evaluateFitnessOfList(mateList1)
        fitness2 = self.evaluateFitnessOfList(mateList2)
        i1 = fitness1.index(max(fitness1))
        i2 = fitness2.index(max(fitness2))
        mate1 = mateList1[i1]
        mate2 = mateList2[i2]
        mates = [mate1, mate2]
        return mates

    def breedMates(self, mates):
        mate1 = mates[0]
        mate2 = mates[1]
        gene1 = random.randint(0,len(mate1) - 1)
        gene2 = random.randint(0,len(mate1) - 1)

        startGene = min(gene1,gene2)
        endGene = max(gene1, gene2)

        childG1 = []
        child = []

        for i in range(startGene,endGene):
            childG1.append(mate1[i])
        adder = 0
        for i in range(0,len(mate2)):
            if mate2[i] in childG1:
                child.append(childG1[adder])
                adder += 1
            else:
                child.append(mate2[i])
        return child

    def mutateGeneration(self,generation):
        for route in generation:
            if random.random() <= self.mutationRate:
                i1 = random.randint(0,len(route)-1)
                i2 = random.randint(0, len(route) - 1)
                gene1 = route[i1]
                gene2 = route[i2]
                route[i1] = gene2
                route[i2] = gene1
        return generation


    def breedPopulation(self):
        newGeneration = []
        listOfMates = []
        for x in range(0,self.generationSize):
            listOfMates.append(self.chooseMates())

        for mates in listOfMates:
            newGeneration.append(self.breedMates(mates))

        newGeneration = self.mutateGeneration(newGeneration)

        self.population = newGeneration
        self.evaluateFitnesses()


A = node("A",0,0)
B = node("B",10,5)
C = node("C",2,3)
D = node("D",3,2)
E = node("E",6,4)
F = node("F",7,6)
G = node("G",10,0)
H = node("H",2,1)
I = node("I",5,5)
J = node("J",7,8)

theMap = map([A,B,C,D,E,F,G,H,I,J])
thePopulation = population(theMap,60,0.2)



for x in range(0,50):
    print("The best route of generation " + str(x) + " is " + str(thePopulation.getBestRoute()) + " with a distance of " + str(thePopulation.getDistOfBestRoute()))
    #print(thePopulation.population)
    thePopulation.breedPopulation()












