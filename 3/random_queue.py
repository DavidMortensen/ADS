from algs4.stdlib.stdrandom import uniform,shuffle
from algs4.stdlib.stdstats import mean,stddev
from random import randint
import random
#from algs4.stdlib.stdio import eprint
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class RandomQueue:
# the code replaces the following Nones;
    def __init__(self):
        self._size = 0
        self._start_size = 1
        self._queue = [None] * self._start_size

    def size(self):
        return self._size
    
    # check if our queue is empty or not
    def isEmpty(self):
        return True if self._size == 0 else False

    def enqueue(self, data):
        # if the amount of items in queue is larger or equal to the size of the queue
        # we double the size of the queue
        if self._size >= len(self._queue):
            self._queue = self._queue + [None]*len(self._queue)

        # input data at the first empty index which will always be equal to 
        # the amount of items in queue (because of zero indexing)
        self._queue[self._size] = data

        self._size += 1


    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError ('Queue is empty!')

        # generate random index
        random_index = randint(0, self._size-1)
        popped = self._queue[random_index]

        # if size is equal to one, there's only 1 item left, and we can safely set that
        # value to 0, since it's already been stored.
        if self._size == 1:
            self._queue[random_index] = None

        # if size is greater than 1, we swap the index of the random index with the last
        # item in the list.
        else:
            self._queue[random_index] = self._queue[self._size-1]
            self._queue[self._size-1] = None
        

        self._size -= 1

        # if the size is 75% of the length of the list, slice from 0 to 75% of the length.
        if self._size <= round(len(self._queue)*.5):
            self._queue = self._queue[:round(len(self._queue)*.75)]

        return popped

    def sample(self):
        #return a random item from our queue.
        random_index = randint(0, self._size-1)
        return self._queue[random_index]

    def __iter__(self):
        # for at gøre TA glad, har vi benyttet din metode :) :) :) :) 
        # Til Andreas, se link: https://giphy.com/gifs/whoa-hd-tim-and-eric-xT0xeJpnrWC4XWblEk
        mine = [i for i in range(self._size)]
        shuffle(mine)

        for idx in mine:
            yield self._queue[idx]


        

    # This "main method" tests your implementation. Do not change it.
if __name__ == "__main__":
    Q = RandomQueue()
    # build a randomQueue with 1,2,..,6
    for i in range(1,7):
        Q.enqueue(i)

    # print 30 die rolls
    eprint( ' '.join([str(Q.sample()) for i in range(30) ] ) )

    # Let’s be more serious: do they really behave like die rolls?
    rolls = [ Q.sample() for i in range(1000) ]
    eprint("Mean (should be around 3.5): {:5.4f}".format(mean(rolls)))
    eprint("Standard deviation (should be around 1.7): {:5.4f}".format(stddev(rolls)))   # removing 3 random values
    eprint( "Removing {}".format(' '.join( [str(Q.dequeue()) for i in range(3) ] ) ) )
    # Add 7,8,9
    for i in range(7,10):
        Q.enqueue(i)

    # Empty the queue in random order
    while not Q.isEmpty():
        eprint(Q.dequeue(),end=' ')       
    eprint()

    # Let s look at the iterator. First, we make a queue of colours:
    C = RandomQueue()
    C.enqueue("red"); C.enqueue("blue"); C.enqueue("green"); C.enqueue("yellow")
    I = iter(C)
    J = iter(C)
    eprint("Two colours from first shuffle: {} {}".format(next(I),next(I)))
    
    eprint("Entire second shuffle: {}".format(' '.join([i for i in J])))
    eprint("Remaining two colours from first shuffle: {} {}".format(next(I),next(I)))
    

    