import time
import sys
import copy

def swap(a,b):
  return (b,a)

def iszero(currState):
    for i in range(0,3):
        for j in range(0,3):
            if currState[i][j]== 0:
                return(i,j)

def moveUp(currState):
    newState = copy.deepcopy(currState)
    i, j = iszero(currState)
    if i != 0:
        newState[i][j], newState[i-1][j] = swap(newState[i][j], newState[i-1][j])
    return newState 

def moveDown(currState):
    newState = copy.deepcopy(currState)
    i, j = iszero(currState)
    if i != 2:
        newState[i][j], newState[i+1][j] = swap(newState[i][j], newState[i+1][j])
    return newState

def moveLeft(currState):
    newState = copy.deepcopy(currState)
    i, j = iszero(currState)
    if j != 0:
        newState[i][j], newState[i][j-1] = swap(newState[i][j], newState[i][j-1])
    return newState

def moveRight(currState):
    newState = copy.deepcopy(currState)
    i, j = iszero(currState)
    if j != 2:
        newState[i][j], newState[i][j+1] = swap(newState[i][j], newState[i][j+1])     
    return newState


def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst

    
def statesearch(unexplored, goal, path):
    if unexplored == []:
        return []
    if len(path) > 30:
        return []
    elif (head(unexplored) == goal):
        return cons(goal,path)
    else:
        visitedStates = []
        if(moveUp(head(unexplored)) not in cons(head(unexplored),path)):
            visitedStates.append(moveUp(head(unexplored)))
        if(moveDown(head(unexplored)) not in cons(head(unexplored),path)):
            visitedStates.append(moveDown(head(unexplored)))
        if(moveLeft(head(unexplored)) not in cons(head(unexplored),path)):
            visitedStates.append(moveLeft(head(unexplored)))
        if(moveRight(head(unexplored)) not in cons(head(unexplored),path)):
            visitedStates.append(moveRight(head(unexplored)))

        result = statesearch(visitedStates, goal, cons(head(unexplored),path))
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored), goal, path)
    return


def tilepuzzle(start, goal):
    return reverse(statesearch([start],goal,[]))
