class Node:
    def __init__(self, state, parent=None, depth=0, cost=0):
        self.STATE = state
        self.PARENT_NODE = parent 
        self.DEPTH = depth 
        self.COST  = cost
    
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
        queue.append(i)
    return queue

def REMOVE_BEST(queue):
    removeFromQueue = REMOVE_LOCAL(queue)
    j = 0
    for i in range(len(queue)):
        if(queue[i].STATE == removeFromQueue):
            j = i
    nextState = queue[j]
    queue.pop(j)
    return nextState
    

# A* algorithm - den tjekker med den globale variabel det STATE man er i. Derefter kigger den på costen af den key man befinder sig på. 
# STATE_SPACE - alle mulige pladser. INITIAL STATE = den plads man befinder sig i
# costOfKey - den kigger på costen af en key
# cost - tjekker en heuristic cost på det indeks som man står på, starter i starten af indekset [0] -
# og tilægges så Path-costen ud fra det samme sted man står
def REMOVE_LOCAL(next):
    if(len(next)==1):
        return 0
    global INITIAL_STATE
    j = STATE_SPACE[INITIAL_STATE][0]
    costOfKey = STATE_SPACE[INITIAL_STATE]
    cost = HEURISTIC_COST[costOfKey[0]] + PATH_COST[INITIAL_STATE][costOfKey[0]]
    # variabel-costen er både heuristic cost og path cost på en specific placering
    # hvis variablens cost er mindre end den cost man står på, så lægges denne værdi til cost
    # j - her gemmer den det state_space som man står på og returner så det initial state 
    for i in range(len(costOfKey)):
        variableCost = HEURISTIC_COST[costOfKey[i]] + PATH_COST[INITIAL_STATE][costOfKey[i]]
        if variableCost < cost :
            cost = variableCost
            j =  STATE_SPACE[INITIAL_STATE][i]
            
    INITIAL_STATE = j
    return j




''''def REMOVE_FIRST(queue):
    return queue.pop(0)'''





def successor_fn(state):
    return STATE_SPACE[state]

'''
#EX1
INITIAL_STATE = 'A'
GOAL_STATE = 'J'
STATE_SPACE= {
    'A': ['B', 'C'], 
'B': ['D', 'E'], 'C': ['F','G'], 
'D': [], 'E':[], 'F':[], 'G':['H', 'I', 'J'], 
'H':[], 'I': [], 'J': [], 
}
'''

## Lav et nyt table til heuristics hvor man mapper det hele 
#EX3
INITIAL_STATE = 'A'

GOAL_STATE = ['K','L']

STATE_SPACE = {

    'A':['B','C','D'],
    'B':['F','E'], 
    'C':['E'], 
    'D':['H','I','J'],
    'E':['G','H'],
    'F':['G'],
    'G':['K'],
    'H':['K','L'],
    'I':['L'],
    'J':[],
    'K':[],
    'L':[]
}

HEURISTIC_COST = {
    'A':6,
    'B':5,
    'C':5,
    'D':2,
    'E':4,
    'F':5,
    'G':4,
    'H':1,
    'I':2,
    'J':1,
    'K':0,
    'L':0
}

GREEDY_COST = {
    ('A','B'):5,
    ('A','C'):5,
    ('A','D'):2,

    ('B','F'):5,
    ('B','E'):4,

    ('C','E'):4,

    ('D','H'):1,
    ('D','I'):2,
    ('D','J'):1,

    ('F','G'):4,

    ('E','G'):4,
    ('E','H'):1,

    ('I','L'):0,

    ('G','K'):0,
    
    ('H','K'):0,
    ('H','L'):0
}

PATH_COST = {
    
    'A': {'B':1,'C':2,'D':4},
    'B': {'F':5,'E':1},
    'C': {'E':1},
    'D': {'H':1, 'I':4, 'J':2},
    'E': {'G':2, 'H':3},
    'F': {'G':1},
    'G': {'K':6},
    'H': {'K':6,'L':5},
    'I': {'L':3},
    'J': {},
    'K': {},
    'L': {}
}

## Når vi deriver cost, lav funktion
## tage evt. en node


def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()