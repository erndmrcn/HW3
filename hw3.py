# Eren Demircan - 2237246
# CEng462 - HW3
# Game playing with minimax&alpha-beta algorithms

# global variables and structures
class Node:
    def __init__(self, parent, min_max, state, action, value):
        # parent -> parent of the node
        # min_max -> if the node is min or max 
        self.parent = parent
        self.min_max = min_max
        self.state = state
        self.action = action
        self.value = value
        self.childs = []
        return

global stateNodes
# holds (state, Node)
stateNodes = []

# utilities
# main function

def readFile(fileName):
    global root, stateNodes

    # read tictactoe
    if fileName[0] == 't':
        pass
    # read gametree
    elif fileName[0] == 'g':
        with open(fileName) as f:
            lines = f.readlines()
        
        lines = [ele.replace('\n', '') for ele in lines]

        rootState = lines[0]
        root = Node(None, "MAX", rootState, None, None)

        stateNodes.append((rootState, root))
        lines.pop(0)
        for ele in lines:

            temp = ele.split(' ')
            # means parent child action
            if len(temp) > 1:
                newNode = Node(None, None, None, None, None)
                for node in stateNodes:
                    if node[0] == temp[0]:
                        newNode.parent = node[1]
                        newNode.state = temp[1]
                        newNode.action = temp[2]
                        stateNodes.append((temp[1], newNode))
                        node[1].childs.append(newNode)
                
            # means the value of leaf nodes given
            elif len(temp) == 1:
                temp2 = ele.split(':')
                for node in stateNodes:
                    if node[0] == temp2[0]:
                        node[1].value = int(temp2[1])
    else:
        print('Wrong file name: File name should start with \'t\' or \'g\'.')
        exit('Program exited with code -1')
    return

def findNode(state):
    global root

    return

def minimax_decision(min_max):
    v_max = -2000000
    v_min = 2000000
    v = []
    if min_max == "MAX":
        for child in root.childs:
            print(child.state)
            v.append(max(v_max, min_value(child)))

        result = max(v)    
        print("main: max_value " + str(v) + " is selected")

        return result
    elif min_max == "MIN":
        for child in root.childs:
            v.append(min(v_min, max_value(child)))
        
        result = min(v)
        print("main: min_value " + str(v) + " is selected")

        return result

def max_value(currentNode):
    # leaf node
    if len(currentNode.childs) == 0:
        print("max_value")
        print(currentNode.state, currentNode.value)
        return currentNode.value
    
    v = -2000000

    for child in currentNode.childs:
        v = max(v, min_value(child))
        print("max_value " + str(v) + " is selected")

    return v

def min_value(currentNode):
    if len(currentNode.childs) == 0:
        print("min_value")
        print(currentNode.state, currentNode.value)
        return currentNode.value

    v = 2000000

    for child in currentNode.childs:
        v = min(v, max_value(child))
        print("min_value " + str(v) + " is selected")
    
    return v

def SolveGame(methodName, problemFileName, playerType):
    # methodName - Minimax or AlphaBeta
    # fileName - gametree or tictactoe
    # playerType - MAX or MIN
    readFile(problemFileName)
    f = minimax_decision(playerType)
    return f

print(SolveGame("s", "gametree1.txt", "MIN"))