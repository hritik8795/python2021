from collections import deque
customqueue=deque(maxlen=3)
print(customqueue)
customqueue.append(1)
customqueue.append(2)
customqueue.append(3)
print(customqueue)
print(customqueue.clear())
print(customqueue)

