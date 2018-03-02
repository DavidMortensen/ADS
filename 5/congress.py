from algs4.stdlib import stdio
from priority_queue import PriorityQueue, Node

pQueue = PriorityQueue()

states = stdio.readInt()
seats = stdio.readInt() - states

print(states, seats)
while not stdio.isEmpty():
    state = stdio.readString()
    population = stdio.readInt()
    #indsæt udregning

    assigned_seats = 1 +
    current_node = Node(state, population)
    pQueue.insert(current_node)

pQueue.show()

print()
pQueue.show()

