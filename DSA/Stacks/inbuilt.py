# Inbuilt Stack's

# for stacks we can simply use Lists
import queue

# s = [1,2,3,4]
# s.append(45)
# s.append(54)
# s.append(69)

# s.pop()

# for Queue

# q = queue.Queue()
# q.put(55)
# q.put(84)
# q.put(64)

# print(q.get())
# # print()
q = queue.LifoQueue()
q.put(44)
q.put(55)
q.put(22)
q.put(11)

print(q.get())
