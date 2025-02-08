class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head 
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self, head=None):
        if not head:
            current = self.head
        else:
            current = head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        if self.head is None:
            print("The list is empty")
            return
        prev = None
        cur = self.head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        self.head = prev

        return self

    def split(self, head):
        fast = head
        slow = head

        # Move fast pointer two steps and slow pointer one step until fast reaches the end
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        second = slow.next
        slow.next = None
        return second
    
    def merge(self, first, second):
        # If either list is empty, return the other list
        if not first:
            return second
        if not second:
            return first

        # Pick the smaller value between first and second nodes
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            return first
        else:
            second.next = self.merge(first, second.next)
            return second

    def merge_sort(self, head=None):
        if head is None:
            head = self.head
    
        # Base case: if the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Split the list into two halves
        second = self.split(head)

        # Recursively sort each half
        head = self.merge_sort(head)
        second = self.merge_sort(second)
        
        # Merge the two sorted halves
        return self.merge(head, second)
    
def merge_two_lists(list1: LinkedList, list2: LinkedList):
    print("Linked list")
    new_list = LinkedList()
    cur1 = list1.head
    cur2 = list2.head

    while cur1 or cur2:
        if cur1 and not cur2:
            new_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        elif cur2 and not cur1:
            new_list.insert_at_end(cur2.data)
            cur2 = cur2.next
        elif cur1.data <= cur2.data:
            new_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        elif cur2.data <= cur1.data:
            new_list.insert_at_end(cur2.data)
            cur2 = cur2.next

    return new_list


llist = LinkedList()

# Insert nodes at the beginning
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Insert nodes at the end
llist.insert_at_end(20)
llist.insert_at_end(25)

# Print linked list
print("Linked list:")
llist.print_list()

llist.reverse_list()

# Print reserved list
print("Reserved list:")
llist.print_list()

head = llist.merge_sort()

# Print sorted list
print("Sorted list:")
llist.print_list(head)

llist2 = LinkedList()

# Insert nodes at the beginning
llist2.insert_at_beginning(10)
llist2.insert_at_beginning(5)
llist2.insert_at_beginning(3)

# Insert nodes at the end
llist2.insert_at_end(20)
llist2.insert_at_end(25)

llist3 = LinkedList()

# Insert nodes at the beginning
llist3.insert_at_beginning(10)
llist3.insert_at_beginning(5)
llist3.insert_at_beginning(3)

# Insert nodes at the end
llist3.insert_at_end(30)
llist3.insert_at_end(35)

merged_list = merge_two_lists(llist2, llist3)
merged_list.print_list()