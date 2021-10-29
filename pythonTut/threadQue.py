# QUeues
from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

first = q.get()
sec = q.get()
sec = q.get()
print(first)
print(sec)
q.task_done()
# q.join()
