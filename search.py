# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
def directions(dir):
    from game import Directions as d
    if dir == "South":
        return d.SOUTH
    elif dir == "North":
        return d.NORTH
    elif dir == "West":
        return d.WEST
    elif dir == "East":
        return d.EAST
    else:
        return None
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #function graph-search(problem,fringe) return solution
    #a search node must contain not only a 
    # state but also the information necessary 
    # to reconstruct the path (plan) which gets 
    # to that state.
    from game import Directions as d
    close = []
    #close list of state closed
    fringe = util.Stack()
    fringe.push((problem.getStartState(),[]))
    _fringe = []
    # _fringe.insert(0,(problem.getStartState(),[]))
    _fringe.append((problem.getStartState(),[]))
    p_action =[]

    while not fringe.isEmpty():
        
        node=fringe.pop()
        _fringe.pop()  
        p_action = node[1]
        #node start state, path
        # ((5,4),[s,w,e,n])       
        if problem.isGoalState(node[0]):
            return node[1]                  
        if node[0] not in close:
            close.append(node[0])
            for x in problem.getSuccessors(node[0]):
                path = []
                path.extend(p_action)
                path.append(x[1])
                fringe.push((x[0],path))
                _fringe.append((x[0],path))
                # _fringe.insert(0,(x[0],path))                
    else:
        return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    close = []
    #close list of state closed
    fringe = util.Queue()
    fringe.push((problem.getStartState(),[]))
    _fringe = []
    _fringe.insert(0,(problem.getStartState(),[]))
    # _fringe.append((problem.getStartState(),[]))
    p_action =[]

    while not fringe.isEmpty():
        
        node=fringe.pop()
        _fringe.pop()  
        p_action = node[1]
        #node start state, path
        # ((5,4),[s,w,e,n])       
        if problem.isGoalState(node[0]):
            return node[1]                  
        if node[0] not in close:
            close.append(node[0])
            for x in problem.getSuccessors(node[0]):
                path = []
                path.extend(p_action)
                path.append(x[1])
                fringe.push((x[0],path))
                # _fringe.append((x[0],path))
                _fringe.insert(0,(x[0],path))                
    else:
        return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions as d
    close = []
    #close list of state closed
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    # _fringe.insert(0,(problem.getStartState(),[]))
    # _fringe.append((problem.getStartState(),[]))
    p_action =[]
    p_cost=0
    while not fringe.isEmpty():        
        node=fringe.pop()
        # _fringe.pop()  
        p_action = node[1]  
        p_cost = problem.getCostOfActions(node[1])   
        #node start state, path
        # ((5,4),[s,w,e,n])       
        if problem.isGoalState(node[0]):
            return node[1]                  
        if node[0] not in close:
            close.append(node[0])
            for x in problem.getSuccessors(node[0]):
                path = []
                path.extend(p_action)
                path.append(x[1])
                fringe.push((x[0],path),x[2]+p_cost)
                # _fringe.append((x[0],path))
                # _fringe.insert(0,(x[0],path))
         
    else:
        return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    from game import Directions as d
    close = []
    #close list of state closed
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0)
    # _fringe.insert(0,(problem.getStartState(),[]))
    # _fringe.append((problem.getStartState(),[]))
    p_action =[]
    p_cost=0
    p_heuristic=0
    while not fringe.isEmpty():        
        node=fringe.pop()
        # _fringe.pop()  
        p_action = node[1]  
        # p_heuristic = heuristic(node[0],problem)
        p_cost = problem.getCostOfActions(node[1])
        #node start state, path
        # ((5,4),[s,w,e,n])       
        if problem.isGoalState(node[0]):
            return node[1]                  
        if node[0] not in close:
            close.append(node[0])
            for x in problem.getSuccessors(node[0]):
                path = []
                path.extend(p_action)
                path.append(x[1])
                p_heuristic = heuristic(x[0],problem)
                fringe.push((x[0],path),x[2]+p_cost+p_heuristic)
                # _fringe.append((x[0],path))
                # _fringe.insert(0,(x[0],path))
         
    else:
        return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
