performanceMeasure = [0,0,0,0,0,0,0,0]
expectedPerformance = -999

#first array is location, clean/dirty for sqaure A and second array is square B
percept = ["null", "null"]
environmentState = ["null", "null"]
def resetAgent():

    expectedPerformance = -999
    environmentState = ["null", "null"]
def initialPercept(envState, location):
    status = "null"
    if location == "B":
        status = envState[1]
    else:
        status = envState[0]
    percept = [location,status]
    return percept


def agentFunction(percept):
    action = "null"
    if percept[1] == "Dirty": # Suck if Dirty
        action = "Suck"
    else: # else move
        if percept[0] == "A":
            action = "Right"
        else:
            action = "Left"
    return action

# adds 1 to performance for every clean tile
def updatePerformanceMeasure(envState, performanceMeasure):
    if envState[0] == "Clean":
        performanceMeasure += 1
    if envState[1] == "Clean":
        performanceMeasure += 1
    return performanceMeasure

def updateEnvironment(envState, percept, action, performanceMeasure):
    AorB = -99
    if percept[0] == "A":
        AorB = 0
    else:
        AorB = 1
    squareState = envState[AorB]

    if action == "Suck":
        squareState = "Clean"
        percept[1] = squareState
    if action == "Right":
        percept[0] = "B" # update next perception if moving
        percept[1] = envState[1]  # update next perception of clean/dirty
    if action == "Left":
        percept[0] = "A"
        percept[1] = envState[0]  # update next perception of clean/dirty

    envState[AorB] = squareState


    performanceMeasure = updatePerformanceMeasure(envState,performanceMeasure)
    return [envState, percept, performanceMeasure]
num = 0

print("Testing agent for 5 steps with envState (clean clean) and robot in A")
resetAgent()
environmentState = ["Clean", "Clean"]
percept = initialPercept(environmentState, "A")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (clean Dirty) and robot in A")
resetAgent()
environmentState = ["Clean", "Dirty"]
percept = initialPercept(environmentState, "A")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (Dirty Clean) and robot in A")
resetAgent()
environmentState = ["Dirty", "Clean"]
percept = initialPercept(environmentState, "A")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (Dirty Dirty) and robot in A")
resetAgent()
environmentState = ["Dirty", "Dirty"]
percept = initialPercept(environmentState, "A")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (clean clean) and robot in B")
resetAgent()
environmentState = ["Clean", "Clean"]
percept = initialPercept(environmentState, "B")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (clean Dirty) and robot in B")
resetAgent()
environmentState = ["Clean", "Dirty"]
percept = initialPercept(environmentState, "B")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (Dirty Clean) and robot in B")
resetAgent()
environmentState = ["Dirty", "Clean"]
percept = initialPercept(environmentState, "B")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

print("Testing agent for 5 steps with envState (Dirty Dirty) and robot in B")
resetAgent()
environmentState = ["Dirty", "Dirty"]
percept = initialPercept(environmentState, "B")
print("initial perception: " + str(percept))

for x in range(0,5):
    action = agentFunction(percept)
    print("Action: " + str(action))
    [envState, percept, performanceMeasure[num]] = updateEnvironment(environmentState,percept,action,performanceMeasure[num])
print("Final Performance Measure: " + str(performanceMeasure[num]) + "\n" )
num += 1

averagePerformanceMeasure = 0
for x in range(0, len(performanceMeasure)):
    averagePerformanceMeasure += performanceMeasure[x]

averagePerformanceMeasure = averagePerformanceMeasure / len(performanceMeasure)
print("Average Performance Measure: " + str(averagePerformanceMeasure))





