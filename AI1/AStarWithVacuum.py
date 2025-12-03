class Node:
#(action der viser hvilken action der skal til for at komme til den relevante state)

    def __init__(self, state, parent=None, depth=0, cost=0, path = None): 
        self.STATE = state
        self.PARENT_NODE = parent 
        self.DEPTH = depth 
        self.COST  = cost
        self.PATH = path
        self.HEURISTIC = HEURISTIC_COST(state)
        self.ACTION = RULE_ACTION[1]
       
       
    # lav path om til en path af rigtige actions

    # the path takes the current node (self) and places it inside a list
    # we start by looking at the node placed at the bottom of the node tree and move up through the tree
    # the path we get are then appended to path-list

    def path(self):
        current_node = self 
        path = [self]
        while current_node.PARENT_NODE:
            current_node = current_node.PARENT_NODE
            path.append(current_node)
        return path
    
    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)

    # Here we compare two Nodes, if we look at a non-Node we simply return False 
    # If the object is a Node, the method returns the Nodes path-cost and heuristics and compares it with the previously known Node
    
    def __gt__(self,other):
        if type(other) == Node:
            return other.COST + other.HEURISTIC < self.COST + self.HEURISTIC
        else:
            return False

    
    def __eq__(self, other: object) -> bool:
        if type(other) == Node:
            return other.COST + other.HEURISTIC == self.COST + self.HEURISTIC
        else:
            return False


# 
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_BEST(fringe)
        
        if node.STATE == GOAL_STATE[0] or node.STATE == GOAL_STATE[1]:
            return node.path()
        
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))




def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s  = Node(node)
        s.STATE = child
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
    
        successors = INSERT(s, successors)
        
    return successors




def INSERT(node, queue):
    queue.append(node)
    return queue


def INSERT_ALL(list, queue):
    for i in list:
        queue.insert(i)
    return queue

def REMOVE_BEST(queue):
    removeFromQueue = aStarAlgorithm(queue)
    j = 0
    for i in range(len(queue)):
        if(queue[i].STATE == removeFromQueue):
            j = i
    nextState = queue[j]
    queue.pop(j)
    return nextState
    

def aStarAlgorithm(initial_state, goal_state, state_space):
    fringe = []
    initial_node = Node(initial_state)
    fringe.append(initial_node)
    while len(fringe) > 0 :
        node = fringe.pop(0)
        if node.STATE == goal_state :
            return fringe # return something else

        successor_states = successor_fn(node.STATE,state_space)

        for successor in successor_states : 
            fringe.append(Node(state=successor[1],parent=node,depth=node.DEPTH+1,cost=node.COST+1)) 

        fringe = sorted(fringe)

    '''

j = state_space[initial_state][0]

    costOfKey = state_space[initial_state]
    
    cost = HEURISTIC_COST[costOfKey[0]] + PATH_COST[initial_state][costOfKey[0]]
    # variabel-costen er både heuristic cost og path cost på en specific placering
    # hvis variablens cost er mindre end den cost man står på, så lægges denne værdi til cost
    # j - her gemmer den det state_space som man står på og returner så det initial state 

    for i in range(len(costOfKey)):
        variableCost = HEURISTIC_COST[costOfKey[i]] + PATH_COST[initial_state][costOfKey[i]]
        if variableCost < cost :
            cost = variableCost
                                            #man får tuple med state uden action
            j =  state_space[initial_state][i][1]
            
    initial_state = j



    return j

    '''
    


def successor_fn(state, state_space):

    return state_space[state]


A = 'A'
B = 'B'


RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp! '
}

 
INITIAL_STATE = (A, 'Dirty', 'Dirty')
# The first 
GOAL_STATE = (A, 'Clean', 'Clean')
#                  Current state - [(action,(location, stateA, stateB))]          
STATE_SPACE = {(A, 'Dirty', 'Dirty'): [(4,(A, 'Dirty', 'Dirty')), (1,(A, 'Clean', 'Dirty')), (2,(B, 'Dirty', 'Dirty'))],
               (B, 'Dirty', 'Dirty'): [(1,(B, 'Dirty', 'Clean')), (4,(B, 'Dirty', 'Dirty')), (3,(A, 'Dirty', 'Dirty'))],
               (A, 'Clean', 'Dirty'): [(2,(B, 'Clean', 'Dirty')), (4,(A, 'Clean', 'Dirty'))],
               (B, 'Dirty', 'Clean'): [(3,(A, 'Dirty', 'Clean')), (4,(B, 'Dirty', 'Clean'))],
               (B, 'Clean', 'Dirty'): [(1,(B, 'Clean', 'Clean')), (3,(A, 'Clean', 'Dirty')), (4,(B, 'Clean', 'Dirty'))],
               (A, 'Dirty', 'Clean'): [(1,(A, 'Clean', 'Clean')), (2,(B, 'Dirty', 'Clean')), (4,(A, 'Dirty', 'Clean'))],
               (A, 'Clean', 'Clean'): [(4,(A, 'Clean', 'Clean')), (2,(B,'Clean', 'Clean'))],
               (B, 'Clean', 'Clean'): [(4,(B, 'Clean', 'Clean')), (3,(A,'Clean', 'Clean'))],
}

PATH_COST = {

        'A' : {'B':1},
        'B' : {'A':1}
}

# This counts the amount of dirty rooms in the statespace 
# the function counts from index[1], as index[0] claims the action to do from that spot
# The heuristic cost will then be equal to the number of dirty rooms

def HEURISTIC_COST(state):
    dirty_rooms_counter: int = 0
    for room in state[1:]:
        if room == 'Dirty':
            dirty_rooms_counter+=1

    return dirty_rooms_counter
    


## Når vi deriver cost, lav funktion
## tage evt. en node

# The run method initializes the aStarAlgorithm based on the current parameters - Initial state, the goal state and the state spaces in the current version

def run():
    path = aStarAlgorithm(initial_state=INITIAL_STATE, goal_state=GOAL_STATE,state_space=STATE_SPACE)
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()

    # tage state og ignorer første (A), gør Heuristic mindre jo bedre den er
    # man kan evt. tælle hvor mange dirty der er.