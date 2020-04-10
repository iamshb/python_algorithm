import queue

data_queue = queue.Queue()
data_queue.put('a')
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())

print('--------------------')

lifo = queue.LifoQueue()
lifo.put('a')
lifo.put('b')
print(lifo.qsize())
print(lifo.get())
print(lifo.qsize())
print(lifo.get())
print(lifo.qsize())

print('--------------------')

pqueue = queue.PriorityQueue()
pqueue.put((10, 'sayonara'))
pqueue.put((5, 1))
pqueue.put((1, 'corona'))
for i in range(pqueue.qsize()):
    print(pqueue.get())
