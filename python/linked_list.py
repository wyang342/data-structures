class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, data):
        # write your code to ADD an element to the Linked List
        # adding to the beginning
        current = self.head
        new_node = Node(data)
        new_node.next = current
        self.head = new_node
        self.length += 1

    def remove(self, data):
        # removes element and returns it
        if self.head == None:
            return None
        else:
            current = self.head
            if current.data == data:
                self.head = current.next
                self.length -= 1
                return current
            else:
                while current.next != None:
                    if current.next.data == data:
                        removed_node = current.next
                        current.next = current.next.next
                        self.length -= 1
                        return removed_node
                    else:
                        current = current.next

    def get(self, element_to_get):
        # write you code to GET and return an element from the Linked List
        if self.head == None:
            return None
        else:
            current = self.head
            if current.data == element_to_get:
                return current
            else:
                while current.next != None:
                    current = current.next
                    if current.data == element_to_get:
                        return current


# ----- Node ------
class Node:
    # store your DATA and NEXT values here
    def __init__(self, data):
        self.data = data
        self.next = None


linkedlist_1 = LinkList()
linkedlist_1.add(1)
linkedlist_1.add(2)
linkedlist_1.add(3)
linkedlist_1.add(4)
linkedlist_1.add(5)
print(linkedlist_1.length)

print(linkedlist_1.remove(1).data)
print(linkedlist_1.length)

print(linkedlist_1.remove(4).data)
print(linkedlist_1.length)

print(linkedlist_1.remove(5).data)
print(linkedlist_1.length)
