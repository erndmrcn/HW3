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
visited = []

def deepCopy(arr):
    result = []
    for row in arr:
        temp = []
        for column in row:
            temp.append(column)
        result.append(temp)
    return result

def terminalState(state):
    visited.append(state)

    row1 = state[:3]
    if row1[0] == row1[1] and row1[1] == row1[2]:
        # terminate
        if row1[0] == 'X':
            return 'X'
        else:
            return 'Y'

    row2 = state[3:6]
    if row2[0] == row2[1] and row2[1] == row2[2]:
        # terminate
        if row2[0] == 'X':
            return 'X'
        else:
            return 'Y'

    row3 = state[6:9]
    if row3[0] == row3[1] and row3[1] == row3[2]:
        # terminate
        if row3[0] == 'X':
            return 'X'
        else:
            return 'Y'

    diagonal1 = state[0::4]
    if diagonal1[0] == diagonal1[1] and diagonal1[1] == diagonal1[2]:
        # terminage
        if diagonal1[0] == 'X':
            return 'X'
        else:
            return 'Y'

    diagonal2 = state[2:8:2]
    if diagonal2[0] == diagonal2[1] and diagonal2[1] == diagonal2[2]:
        # terminage
        if diagonal2[0] == 'X':
            return 'X'
        else:
            return 'Y'  

    column1 = state[0::3]
    if column1[0] == column1[1] and column1[1] == column1[2]:
        # terminate
        if column1[0] == 'X':
            return 'X'
        else:
            return 'Y'

    column2 = state[1::3]
    if column2[0] == column2[1] and column2[1] == column2[2]:
        # terminate
        if column2[0] == 'X':
            return 'X'
        else:
            return 'Y'

    column3 = state[2::3]
    if column3[0] == column3[1] and column3[1] == column3[2]:
        # terminate
        if column3[0] == 'X':
            return 'X'
        else:
            return 'Y'

    if ' ' not in state:
        return 'BF'
    
    # non terminal
    return 'NT'


def expand(currentNode, depth):
    # Order -> (0, 0), (1, 0), (2, 0)
    #          (0, 1), (1, 1), (2, 1)
    #          (0, 2), (1, 2), (2, 2)
    if depth % 2 == 0:
        symbol = 'X'
    elif depth % 2 == 1:
        symbol = 'O'

    childs = []
    arr = stateToArray(currentNode.state)
    
    if arr[0][0] == ' ':
        tempArr = deepCopy(arr)
        tempArr[0][0] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (0,0), None)
        childs.append(newNode)
    if arr[0][1] == ' ':
        tempArr = deepCopy(arr)
        tempArr[0][1] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (1,0), None)
        childs.append(newNode)
    if arr[0][2] == ' ':
        tempArr = deepCopy(arr)
        tempArr[0][2] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (2,0), None)
        childs.append(newNode)


    if arr[1][0] == ' ':
        tempArr = deepCopy(arr)
        tempArr[1][0] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (0,1), None)
        childs.append(newNode)
    if arr[1][1] == ' ':
        tempArr = deepCopy(arr)
        tempArr[1][1] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (1,1), None)
        childs.append(newNode)
    if arr[1][2] == ' ':
        tempArr = deepCopy(arr)
        tempArr[1][2] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (2,1), None)
        childs.append(newNode)


    if arr[2][0] == ' ':
        tempArr = deepCopy(arr)
        tempArr[2][0] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (0,2), None)
        childs.append(newNode)
    if arr[2][1] == ' ':
        tempArr = deepCopy(arr)
        tempArr[2][1] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (1,2), None)
        childs.append(newNode)
    if arr[2][2] == ' ':
        tempArr = deepCopy(arr)
        tempArr[2][2] = symbol
        newNode = Node(currentNode, None, arrayToState(tempArr), (2,2), None)
        childs.append(newNode)

    return childs

# utilities
def arrayToState(arr):
    result = ""
    for e in arr:
        for a in e:
            result += a

    return result

def stateToArray(state):
    result = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(state[i*3 + j])
        result.append(temp)
    return result

# main function

def readFile(fileName):
    global root, stateNodes

    # read tictactoe
    if fileName[0] == 't':
        with open(fileName) as f:
            lines = f.readlines()

        lines = [ele.replace('\n', '') for ele in lines]

        result = []
        for row in lines:
            temp = []
            for column in row:
                temp.append(column)
            result.append(temp)

        state = arrayToState(result)
        root = Node(None, None, state, None, None)

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


def minimax_decision_ttt():
    global visited
    v_max = -2000000
    v = []
    depth = 0
    childs = expand(root, depth)
    for child in childs:
        root.childs.append(child)

    for child in root.childs:
        v.append(max(v_max, min_value_ttt(child, depth + 1)))

    result = max(v)
    ind = v.index(result)
    return result, root.childs[ind].action, visited
    

def max_value_ttt(currentNode, depth):
    result = terminalState(currentNode.state)
    if result == 'X':
        # X wins
        return 5 - (0.01 * (depth - 1))
    elif result == 'Y':
        # Y wins
        return -5
    elif result == 'BF':
        # board full - no winner
        return 0
    
    v = -2000000
    childs = expand(currentNode, depth)
    for child in childs:
        currentNode.childs.append(child)

    for child in currentNode.childs:
        v = max(v, min_value_ttt(child, depth+1))

    return v

def min_value_ttt(currentNode, depth):
    result = terminalState(currentNode.state)
    if result == 'X':
        # X wins
        return 5 - (0.01 * (depth - 1))
    elif result == 'Y':
        # Y wins
        return -5
    elif result == 'BF':
        # board full - no winner
        return 0
    
    v = 2000000
    childs = expand(currentNode, depth)
    for child in childs:
        currentNode.childs.append(child)

    for child in currentNode.childs:
        v = min(v, max_value_ttt(child, depth+1))

    return v

def minimax_decision(min_max):
    v_max = -2000000
    v_min = 2000000
    v = []
    if min_max == "MAX":
        for child in root.childs:
            visited.append(child.state)
            v.append(max(v_max, min_value(child)))

        result = max(v)    
        ind = v.index(result)
        return result, root.childs[ind].action, visited
    elif min_max == "MIN":
        for child in root.childs:
            visited.append(child.state)
            v.append(min(v_min, max_value(child)))
        
        result = min(v)
        ind = v.index(result)
        return result, root.childs[ind].action, visited

def max_value(currentNode):
    # leaf node
    if len(currentNode.childs) == 0:
        return currentNode.value
    
    v = -2000000

    for child in currentNode.childs:
        visited.append(child.state)
        v = max(v, min_value(child))

    return v

def min_value(currentNode):
    if len(currentNode.childs) == 0:
        return currentNode.value

    v = 2000000

    for child in currentNode.childs:
        visited.append(child.state)
        v = min(v, max_value(child))
    
    return v

def SolveGame(methodName, problemFileName, playerType):
    # methodName - Minimax or AlphaBeta
    # fileName - gametree or tictactoe
    # playerType - MAX or MIN
    readFile(problemFileName)
    # f = minimax_decision(playerType)
    return

# print(SolveGame("s", "tictactoe2.txt", "MAX"))
SolveGame('s', "gametree1.txt", 'MAX')
print(minimax_decision("MIN"))