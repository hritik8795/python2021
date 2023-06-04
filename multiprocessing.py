from multiprocessing import queue
customQueue=Queue(maxsize=3)
customQueue.put(1)
print(customQueue.get())