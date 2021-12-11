# Eren Demircan - 2237246
# CEng462 - HW3
# Game playing with minimax&alpha-beta algorithms

# global variables and structures
class Node:
    def __init__(self, parent, min_max, state, action, value):
        self.parent = parent
        self.min_max = min_max
        self.state = state
        self.action = action
        self.value = value
        self.childs = []
        return

stateNodes = []
visited = []

# utility functions
# deep copy for child expansion
def deepCopy(arr):
    result = []
    for row in arr:
        temp = []
        for column in row:
            temp.append(column)
        result.append(temp)
    return result

# changes state array to state string
def arrayToState(arr):
    result = ""
    for e in arr:
        for a in e:
            result += a

    return result

# changes state string to state array
def stateToArray(state):
    result = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(state[i*3 + j])
        result.append(temp)
    return result

# checks if a state is end state or not
def terminalState(state):
    visited.append(state)

    row1 = state[:3]
    # three 'X' or 'O' in row1
    if row1[0] == row1[1] and row1[1] == row1[2]:
        if row1[0] == 'X':
            return 'X'
        elif row1[0] == 'O':
            return 'Y'

    row2 = state[3:6]
    # three 'X' or 'O' in row2
    if row2[0] == row2[1] and row2[1] == row2[2]:
        if row2[0] == 'X':
            return 'X'
        elif row2[0] == 'O':
            return 'Y'

    row3 = state[6:9]
    # three 'X' or 'O' in row2
    if row3[0] == row3[1] and row3[1] == row3[2]:
        if row3[0] == 'X':
            return 'X'
        elif row3[0] == 'O':
            return 'Y'

    diagonal1 = state[0::4]
    # three 'X' or 'O' in diagonal1
    if diagonal1[0] == diagonal1[1] and diagonal1[1] == diagonal1[2]:
        if diagonal1[0] == 'X':
            return 'X'
        elif diagonal1[0] == 'O':
            return 'Y'

    diagonal2 = state[2:8:2]
    # three 'X' or 'O' in diagonal2
    if diagonal2[0] == diagonal2[1] and diagonal2[1] == diagonal2[2]:
        # terminage
        if diagonal2[0] == 'X':
            return 'X'
        elif diagonal2[0] == 'O':
            return 'Y'  

    column1 = state[0::3]
    # three 'X' or 'O' in column1
    if column1[0] == column1[1] and column1[1] == column1[2]:
        if column1[0] == 'X':
            return 'X'
        elif column1[0] == 'O':
            return 'Y'

    column2 = state[1::3]
    # three 'X' or 'O' in column2
    if column2[0] == column2[1] and column2[1] == column2[2]:
        if column2[0] == 'X':
            return 'X'
        elif column2[0] == 'O':
            return 'Y'

    column3 = state[2::3]
    # three 'X' or 'O' in column3
    if column3[0] == column3[1] and column3[1] == column3[2]:
        if column3[0] == 'X':
            return 'X'
        elif column3[0] == 'O':
            return 'Y'

    # there is no winner
    # board is full
    if ' ' not in state:
        return 'BF'
    
    # non terminal
    return 'NT'

# expand a tictactoe node
def expand(currentNode, depth):
    # determine whose turn it is
    if depth % 2 == 0:
        symbol = 'X'
    elif depth % 2 == 1:
        symbol = 'O'

    childs = []
    arr = stateToArray(currentNode.state)
    
    # first row
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

    # second row
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

    # third row
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

# read files into the global structures
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

# minimax for tictactoe
def minimax_decision_ttt(alpha_beta):
    v_max = -2000000
    v_min = 2000000
    v = []
    
    depth = 0

    childs = expand(root, depth)
    for child in childs:
        root.childs.append(child)

    for child in root.childs:
        # apply alphabeta pruning
        if alpha_beta == True:
            temp = max(v_max, min_value_ttt(child, depth+1, alpha_beta, v_max, v_min))
            if temp > v_max:
                v_max = temp
            if v_min <= v_max:
                break
            v.append(v_max)
        else:
            v.append(max(v_max, min_value_ttt(child, depth + 1, alpha_beta, v_max, v_min)))

    result = max(v)
    # find the action taken for optimal solution
    ind = v.index(result)
    return result, root.childs[ind].action, visited

# max value for tictactoe
def max_value_ttt(currentNode, depth, alpha_beta, alpha, beta):
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
        # apply alphabeta pruning
        if alpha_beta == True:
            v = max(v, min_value_ttt(child, depth+1, alpha_beta, alpha, beta))
            if v > alpha:
                alpha = v
            if beta <= alpha:
                break
        else:
            v = max(v, min_value_ttt(child, depth+1, alpha_beta, alpha, beta))
            alpha = v

    return alpha

# min value for tictactoe
def min_value_ttt(currentNode, depth, alpha_beta, alpha, beta):
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
        # apply alphabeta pruning
        if alpha_beta == True:
            v = min(v, max_value_ttt(child, depth+1, alpha_beta, alpha, beta))
            if v < beta:
                beta = v
            if beta <= alpha:
                break
        else:
            v = min(v, max_value_ttt(child, depth+1, alpha_beta, alpha, beta))
            beta = v
    return beta


# minimax for gametree
def minimax_decision(min_max, alpha_beta):
    v_max = 999999
    v_min = -999999
    v = []
    v_max = -2000000
    v_min = 2000000
    v = []
    depth = 0


    if min_max == "MAX":
        for child in root.childs:
            visited.append(child.state)
            # apply alphabeta pruning
            if alpha_beta == True:
                temp = max(v_max, min_value(child, alpha_beta, v_max, v_min))
                if temp > v_max:
                    v_max = temp
                if v_min <= v_max:
                    break
                v.append(v_max)
            else:
                v.append(max(v_max, min_value(child, alpha_beta, v_max, v_min)))

        result = max(v)
        # find the action taken for optimal solution
        ind = v.index(result)
        return result, root.childs[ind].action, visited

    elif min_max == "MIN":
        for child in root.childs:
            visited.append(child.state)
            # apply alphabeta pruning
            if alpha_beta == True:
                temp = min(v_min, max_value(child, alpha_beta, v_max, v_min))
                if temp < v_min:
                    v_min = temp
                if v_min <= v_max:
                    break
                v.append(v_min)
            else:
                v.append(min(v_min, max_value(child, alpha_beta, v_max, v_min)))

        result = min(v)
        # find the action taken for optimal solution
        ind = v.index(result)
        return result, root.childs[ind].action, visited


# max value for gametree
def max_value(currentNode, alpha_beta, alpha, beta):
    # leaf node
    if len(currentNode.childs) == 0:
        return currentNode.value
    
    v = -2000000

    for child in currentNode.childs:
        visited.append(child.state)
        v = max(v, min_value(child, alpha_beta, alpha, beta))
        # apply alphabeta pruning
        if alpha_beta == True:
            if v > alpha:
                alpha = v
            if beta <= alpha:
                break
        else:
            alpha = v
    return alpha

# min value for gametree
def min_value(currentNode, alpha_beta, alpha, beta):

    if len(currentNode.childs) == 0:
        return currentNode.value

    v = 2000000

    for child in currentNode.childs:
        visited.append(child.state)
        v = min(v, max_value(child, alpha_beta, alpha, beta))
        # apply alphabeta pruning
        if alpha_beta == True:
            if v < beta:
                beta = v
            if beta <= alpha:
                break
        else:
            beta = v
    return beta

# main function to be calles
def SolveGame(methodName, problemFileName, playerType):
    global visited, stateNodes 

    visited = []
    stateNodes = []

    readFile(problemFileName)

    # check if alphabeta pruning will be applied
    if methodName == "Minimax":
        ab = False
    elif methodName == "AlphaBeta":
        ab = True

    # call problem specifi functions according to fileName
    if problemFileName[0] == 'g':
        result = minimax_decision(playerType, ab)
    elif problemFileName[0] == 't':
        result = minimax_decision_ttt(ab)
    else:
        exit("Wrong file name format")

    return result