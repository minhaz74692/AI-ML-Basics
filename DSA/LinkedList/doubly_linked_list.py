class Node:
    def __init__(self, data = None, next = None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        new_node = Node(data)
        new_node.next = temp
        temp.prev= new_node
        self.head = new_node

        #     Or more simple and optimized way
        # node = Node(data, self.head)
        # self.head = node







    def printLL(self):
        if self.head is None:
            print("Empty Linked List")
            return

        s = ""
        itr = self.head
        while itr:
            s += str(itr.data) + "-->"
            itr = itr.next

        print("Forward: " +s)

    def backward_print(self):
        if self.head is None:
            print("Empty doubly linked list")
            return


        itr = self.head
        itr2=None
        while itr:
            # print(itr.data, "----")
            itr2=itr
            itr = itr.next

        # print(itr.data)

        s = ""
        while itr2:
            # print(itr2.data)
            s += str(itr2.data) + "-->"
            itr2 = itr2.prev

        print("Backward: " + s)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(40)
    ll.printLL()
    ll.backward_print()