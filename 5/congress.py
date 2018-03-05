from algs4.stdlib import stdio
from priority_queue import PriorityQueue, Node
import math
import sys

pq = PriorityQueue()

states = stdio.readInt()
total_seats = stdio.readInt() 
allocated_seats = states
#print('States: ', states, '   Remaining seats:',seats, '   Allocated seats so far:', allocated_seats, '\n')


# make sure our file still has values 
while not stdio.isEmpty():
    # assign statename and population count 
    state = str(stdio.readLine()).strip('\n')
    population = stdio.readInt()
    # initialize 1 seat per state
    initial_seat = 1
    current_node = Node(state, population, initial_seat)
    pq.insert(current_node)

# run untill we have no more seats
while allocated_seats < total_seats:
    (max_priority, max_state) = (0, '')
    current_index = 0
    for item in pq.queue:
        n = item.seats
        A = item.priority / math.sqrt(n*(n+1))
        if (A > max_priority):
            (max_priority) = (A)
            max_index = current_index
        current_index += 1
        
    allocated_seats += 1
    pq.queue[max_index].seats += 1
    

pq.show()





