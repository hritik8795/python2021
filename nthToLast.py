#yahn par hum last se nth term ko find out karenge
from LinkedList import LinkedList
def nthtoLast(ll,n):
    pointer1 =ll.head
    pointer2 =ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 =pointer2.next
    while pointer2:
        pointer1 =pointer1.next
        pointer2 =pointer2.next
    return pointer1
customLL= LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(nthtoLast(customLL,3))