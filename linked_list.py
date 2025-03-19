import os 

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

    def insertAtIndex(self, data, index):
        if index == 0 :
            self.insertAtBegin(data)
            return
     
        cur_node = self.head
        position = 0 # index

        while cur_node != None and position+1 != index:
            position += 1
            cur_node = cur_node.next
            
        if cur_node != None :
            new_node=Node(data)
            new_node.next=cur_node.next
            cur_node.next=new_node
        else :
            print(f'Index_not_present')
            return

#    def deleteAtBegin(self):


#     def deleteAtIndex(self, index):

#     def deleteWithData(self, data):

# def reverseList(self):

# def mergeList(self, llist):

# def removeDuplicates(self):

# def findMiddle(self):

# def findNthFromEnd(self, n):

# def countOccurences(self, data):

# def rotateList(self, k):

# def isPalindrome(self):

# def isCircular(self):



def main():
    llist = LinkedList()
    llist.printlist()
    llist.insert(1)
    llist.insert(5)
    llist.insert(2)
    llist.insert(4)
    llist.printlist()
    llist.insertAtBegin(24)
    llist.printlist()
    llist.insertAtIndex(55,0)
    llist.printlist()
    llist.insertAtIndex(44,2)
    llist.printlist()
    llist.insertAtIndex(33,6)
    llist.printlist()
    return

if __name__ == '__main__':
    main()
    print(f"{os.path.basename(__file__)} is called directly")
else: 
    print(f"{__file__} is being imported")



