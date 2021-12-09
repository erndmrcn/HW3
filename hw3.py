# Eren Demircan - 2237246
# CEng462 - HW3
# Game playing with minimax&alpha-beta algorithms

# imports

# global variables and structures

# utilities

# main function

def readFile(fileName):
    # read tictactoe
    if fileName[0] == 't':
        pass
    # read gametree
    elif fileName[0] == 'g':
        pass
    else:
        print('Wrong file name: File name should start with \'t\' or \'g\'.')
        exit('Program exited with code -1')
    
    with open(fileName) as f:
        lines = f.readlines()
        
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')

    return lines

def SolveGame(methodName, problemFileName, playerType):
    # methodName - Minimax or AlphaBeta
    # fileName - gametree or tictactoe
    # playerType - MAX or MIN

    return

fileName = "tictactoe1.txt"
print(readFile('b'))