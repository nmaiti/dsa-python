import os

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.elements = 0


    def printlist(self):
        print(f'\033[92mList content \033[0m')
        cur_node = self.head
        index=0
        while cur_node != None :
            print (f'[{index}]{cur_node.data}', end=' -> ')
            cur_node = cur_node.next
            index += 1
        print (f'None')
        return

    def insert(self, data):
        print(f'\033[92mInserting [{data}]\033[0m')
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
        print(f'\033[92mInserting [{data}] at index [{index}]\033[0m')
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

    def deleteAtBegin(self):
        print(f'\033[92mDeleting at begin\033[0m')
        if self.head == None:
            print(f'List is empty')
            return
        else :
            self.head = self.head.next
            return


    def deleteAtIndex(self, index):
        print(f'\033[92mDeleting index [{index}]\033[0m')
        if index == 0 :
            self.deleteAtBegin()
            return

        else :
            position = 0
            cur_node = self.head
            while cur_node != None and  position +1 != index :
                position += 1
                cur_node = cur_node.next

        if position + 1 == index and cur_node != None and cur_node.next != None :
            cur_node.next = cur_node.next.next
        else :
            print(f'Index [{index}]_not_present')

        return

    def deleteWithData(self, data):
        print(f'\033[92mDeleting data [{data}]\033[0m')
        cur_node = self.head

        if cur_node is None:
            print('List is empty')
            return

        if cur_node.data == data:
            self.deleteAtBegin()
            return

        while cur_node.next is not None:
            if cur_node.next.data == data:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next

        print(f'Data [{data}] not found in the list')
        return

    def reverseList(self):
        print(f'\033[92mReversing the list\033[0m')
        prev_node = None
        cur_node = self.head
        next_node= None

        if cur_node is None:
            print('List is empty')
            return
        
        while cur_node is not None :
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        self.head= prev_node
        return



# def mergeList(self, llist):

    def removeDuplicates(self):
        print(f'\033[92mRemoving duplicates\033[0m')
        cur_node = self.head
        prev_node = None
        data_dict = {}

        while cur_node is not None:
            if cur_node.data in data_dict :
                  prev_node.next = cur_node.next
            else :
                data_dict[cur_node.data] = 1
                prev_node = cur_node

            cur_node = cur_node.next
        return


    def findMiddle(self):
        print(f'\033[92mFinding middle element\033[0m')
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

        print(f'Middle element is [{slow_ptr.data}]')
        return


    def findNthFromEnd(self, n):
        print(f'\033[92mFinding nth element from end\033[0m')
        slow_ptr = self.head
        fast_ptr = self.head
        
        for _ in range(n):
            if fast_ptr is None:
                print(f'List is shorter than [{n}]')
                return
            fast_ptr = fast_ptr.next
        
        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        if slow_ptr is not None:
            print(f'Nth element from end is [{slow_ptr.data}]')
        else:
            print(f'Nth element from end is not found')
        return


    def countOccurences(self, data):
        print(f'\033[92mCount Of occurences [{data}]\033[0m')
        cur_node = self.head

        count = 0

        while cur_node is not None:
            if cur_node.data == data :
                count += 1
            cur_node = cur_node.next
         
        print(f'Occurences of [{data}] is [{count}]')
        return count


# def rotateList(self, k):

    def isPalindrome(self):
        print(f'\033[92mChecking for palindrome\033[0m')
        cur_node = self.head
        data_list = []

        while cur_node is not None:
            data_list.append(cur_node.data)
            cur_node = cur_node.next

        left = 0
        right = len(data_list) - 1

        while left < right:
            if data_list[left] != data_list[right]:
                print(f'List is not palindrome')
                return
            left += 1
            right -= 1

        print(f'List is palindrome')
        return

# def isCircular(self):



def main():
    llist = LinkedList()
    llist.printlist()
    llist.insert(1)
    llist.reverseList()
    llist.printlist()
    llist.insert(5)
    llist.insert(44)
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
    print(f'remove at index 0')
    llist.deleteAtIndex(0)
    llist.printlist()
    print(f'remove at index 7')
    llist.deleteAtIndex(7)
    llist.printlist()
    llist.deleteWithData(24)
    llist.printlist()
    llist.reverseList()
    llist.printlist()
    llist.countOccurences(44)
    llist.removeDuplicates()
    llist.printlist()
    llist.findMiddle()
    llist.findNthFromEnd(2)


    return

if __name__ == '__main__':
    main()
    print(f"{os.path.basename(__file__)} is called directly")
else:
    print(f"{__file__} is being imported")



