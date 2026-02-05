class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_values(self, data_list):
        if data_list is None or len(data_list) == 0:
            print("Data list is empty")
            return

        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        itr = self.head
        while itr.next.next:
            itr = itr.next

        itr.next= None

    def length(self):
        if self.head is None:
            return 0

        count =0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count

    def insert_at_index(self, index,data):
        if index < 0 or index > self.length():
            print("Invalid Index")
            return

        if index ==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        prev = self.head
        while count != index:
            count += 1
            prev = itr
            itr = itr.next

        new_data = Node(data)
        prev.next = new_data
        new_data.next = itr

    def remove_at_index(self, index):
        if self.head is None:
            print("Empty linked list")
            return
        if index<0 or index >= self.length():
            # raise Exception("Invalid Index")
            print("Invalid Index")
            return

        if index == 0:
            self.delete_at_beginning()
            return

        count = 0
        itr = self.head
        prev = self.head
        while count != index:
            count += 1
            prev = itr
            itr = itr.next

        prev.next = itr.next


    def insert_after_value(self, value, data):
        if self.head is None:
            print("Empty Linked List with Invalid value")
            return

        new_node = Node(data)
        itr = self.head
        while itr:
            if itr.data == value:
                temp_node = itr.next
                itr.next = new_node
                new_node.next = temp_node
                break
            itr = itr.next

    def remove_by_value(self, value):
        if self.head is None:
            print("Empty Linked List with invalid value to remove")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = None
        itr = self.head
        while itr:
            if itr.data == value:
                prev.next = itr.next
                break
            prev = itr
            itr = itr.next


    def printll(self):
        if self.head is None:
            print("Linked List is empty from print")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next

        print(llstr)



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_end(40)

    ll.insert_at_index(3, 100)
    ll.printll()
    ll.remove_at_index(5)
    ll.printll()

    # print("lenght of the list: "  , ll.length()  )# Output: 2
    ll2 = LinkedList()
    ll2.insert_values(["apple", "banana", "cherry"])
    ll2.printll()  # Output: apple -> banana -> cherry -> None
    ll2.insert_after_value("cherry", "watermelon")
    ll2.printll()
    ll2.remove_by_value("banana")
    ll2.printll()


