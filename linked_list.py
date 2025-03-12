class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def printlist(self):
        cur_node = self.head
            
        while cur_node != None :
            print (f'{cur_node.data}', end=' -> ')
            cur_node = cur_node.next
        print (f'None')
        return

    def insert(self, data):
        new_node=Node(data)
        if self.head == None:
            self.head = new_node
            return
        else :
            last_node = self.head
            while last_node.next != None :
                last_node = last_node.next

            last_node.next = new_node
            return
    
    def insertAtBegin(self, data):
        new_node=Node(data)
        new_node.next = self.head
        self.head = new_node
        return


llist = LinkedList()
llist.printlist()
llist.insert(1)
llist.insert(5)
llist.insert(2)
llist.insert(4)
llist.printlist()
llist.insertAtBegin(24)
llist.printlist()


