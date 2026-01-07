import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
       return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) ==0

    def size(self):
        return len(self.buffer)

the_queue = Queue()

def place_order(orders):
    for order in orders:
        print("Order placed: ", order)
        the_queue.enqueue(order)
        time.sleep(.5)

def serve_order():
    time.sleep(1)
    while not the_queue.is_empty():
        s = the_queue.dequeue()
        print("Order served: ", s)
        time.sleep(2)



if __name__ == "__main__":
    # q = Queue()
    # q.enqueue({"company":"Walmart","timestamp":"15 apr, 11:03AM","price": 132})
    # q.enqueue({"company": "Walmart","timestamp": "15 apr, 11:02AM","price": 130})
    # q.enqueue({"company": "Walmart","timestamp": "15 apr, 11:00AM","price": 135})
    t = time.time()
    food_orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    print(food_orders)
    t1 = threading.Thread(target=place_order, args=(food_orders,))
    t2 = threading.Thread(target=serve_order)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Total time: ", time.time() - t)






