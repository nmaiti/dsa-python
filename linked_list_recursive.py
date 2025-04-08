import os


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.elements = 0

    def printlist(self, head):
        if not hasattr(self, 'call_count'):
            self.call_count = -1
        self.call_count += 1
        print(f'[{self.call_count}]', end=' ')
        if head is None:
            print(f'None')
            self.call_count = -1
            return
        else :
            print(f'{head.data}', end=' -> ')
            self.printlist(head.next)

        return
    
    def clear(self, head):
        if head is None:
            return
        self.clear(head.next)
        head.next = None
        if head == self.head:
            self.head = None
        return

    def insert(self, head, data):

        if head is None:
            self.head = Node(data)
            return
        elif head.next is None:
            head.next = Node(data)
            return
        else:
            self.insert(head.next, data)
            return
                
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def insertAtIndex(self, head, data, index):
        if not hasattr(self, 'test_index'):
            self.test_index = index
   
        if index < 0:
            print(f'Index [{index}] is invalid')
            return head

        if index == 0:
            print(f'\033[92mInserting [{data}] at index [{index}]\033[0m')
            new_node = Node(data)
            new_node.next = head
            if head == self.head:  # Update the head of the list if it's the first element
                self.head = new_node
            return new_node

        if head is None:
        #    print(f'Index [{index}] is out of bounds. Requested index: [{index}]')
            print(f'Index [{index}] is out of bounds. Requested index: [{self.test_index}]')
            return head

        head.next = self.insertAtIndex(head.next, data, index - 1)
        return head

    def deleteAtBegin(self):
        print(f'\033[92mDeleting at begin\033[0m')
        if self.head == None:
            print(f'List is empty')
            return
        else:
            self.head = self.head.next
            return

    def deleteAtIndex(self, head, index):
        if head is None:
            print(f'Index [{index}]_not_present')
            return head

        if index == 0:
            print(f'\033[92mDeleting index [{index}]\033[0m')
            if head == self.head:  # Update the head of the list if it's the first element
                self.head = head.next
            return head.next

        head.next = self.deleteAtIndex(head.next, index - 1)
        return head

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

    def reverseList(self, head):
        if head is None or head.next is None:
            self.head = head
        else :
            self.reverseList(head.next)
            head.next.next=head
            head.next=None
        return


# def mergeList(self, llist):


    def removeDuplicates(self):
        print(f'\033[92mRemoving duplicates\033[0m')
        cur_node = self.head
        prev_node = None
        data_dict = {}

        while cur_node is not None:
            if cur_node.data in data_dict:
                prev_node.next = cur_node.next
            else:
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

    def countNccurences(self, head, data):
       
        if head is None:
            return 0  # Base case: If the list is empty, return 0

        # Check if the current node's data matches the target data
        count = 1 if head.data == data else 0

        # Add the count from the rest of the list
        return count + self.countNccurences(head.next, data)


# def rotateList(self, k):


    def isPalindromeOn(self):
        """
        Checks if the linked list is a palindrome using recursion.
        """
        # Initialize the left pointer to the head of the list
    #    self.left = self.head
        self.rleft = self.head
        def _isPalindromeHelper(right):
            """
            Recursive helper function to check for palindrome.
            Traverses to the end of the list and compares nodes during the unwinding phase.
            """
            # Base case: If the right pointer reaches the end, return True
            if right is None:
                return True

            # Recursive call to move the right pointer to the end
            is_palindrome = _isPalindromeHelper(right.next)

            # If any previous comparison failed, return False
            if not is_palindrome:
                return False

            # Compare the left and right pointers
            is_palindrome = (self.rleft.data == right.data)

            # Move the left pointer one step forward
            self.rleft = self.rleft.next

            return is_palindrome

        # Call the nested helper function
        if (_isPalindromeHelper(self.rleft)) :
            print(f'The linked list is a palindrome')
        else:
            print(f'The linked list is not a palindrome')


# def isCircular(self):


def main():
    llist = LinkedList()
    llist.printlist(llist.head)
    llist.insert(llist.head, 1)
#    llist.reverseList()
#    llist.printlist(llist.head)
    llist.insert(llist.head, 5)
    llist.insert(llist.head, 44)
    llist.insert(llist.head, 2)
    llist.insert(llist.head, 4)
    llist.printlist(llist.head)

    print(f'\033[92mInserting at index [1]\033[0m')
    llist.insertAtIndex(llist.head, 99, 12)
    llist.printlist(llist.head)
    print(f'\033[92m---------------[2]\033[0m')

#    llist.clear(llist.head)
#    llist.printlist(llist.head)
    llist.reverseList(llist.head)
    llist.printlist(llist.head)
    

    llist.deleteAtIndex(llist.head, 2)
    llist.printlist(llist.head)    

    print(f'\033[92mDeleting at begin\033[0m')
    llist.clear(llist.head)
    llist.printlist(llist.head)    


    llist.insertAtIndex(llist.head, 97, 0)
    llist.printlist(llist.head)

    llist.clear(llist.head)
###    llist.insertAtBegin(24)
###    llist.printlist()
###    llist.insertAtIndex(55, 0)
###    llist.printlist()
###    llist.insertAtIndex(44, 2)
###    llist.printlist()
###    llist.insertAtIndex(33, 6)
###    llist.printlist()
###    print(f'remove at index 0')
###    llist.deleteAtIndex(0)
###    llist.printlist()
###    print(f'remove at index 7')
###    llist.deleteAtIndex(7)
###    llist.printlist()
###    llist.deleteWithData(24)
###    llist.printlist()
###    llist.reverseList()
###    llist.printlist()
#    print(f'\033[92mCount Of occurences [{data}]\033[0m')

###    llist.removeDuplicates()
###    llist.printlist()
###    llist.findMiddle()
###    llist.findNthFromEnd(2)
###
###    llist.clear()
###    llist.printlist()
###
###
###
###    llist.insert(1)
###    llist.insert(44)
####    llist.insert(23)
###    llist.insert(44)
###    llist.insert(2)
       
    llist.insert(llist.head, 1)
    llist.insert(llist.head, 66)
    llist.insert(llist.head, 2)
    llist.insert(llist.head, 66)
    llist.insert(llist.head, 1)
    llist.printlist(llist.head)
    llist.isPalindromeOn()
    cc=llist.countNccurences(llist.head, 66)
    print(f'Count of [66] is [{cc}]')



if __name__ == '__main__':
    main()
    print(f"{os.path.basename(__file__)} is called directly")
else:
    print(f"{__file__} is being imported")
