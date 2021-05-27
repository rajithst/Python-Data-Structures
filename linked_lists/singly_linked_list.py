class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    """
    Insert operations
    """
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print("Previous Node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    """
    delete operations
    """
    def delete_by_value(self, value):
        curr_node = self.head
        if curr_node and curr_node.data == value:
            self.head = curr_node.next
            curr_node = None
            return

        previous_node = None
        while curr_node is not None and curr_node.data != value:
            previous_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        previous_node.next = curr_node.next
        curr_node = None

    def delete_by_position(self,position):
        if self.head:
            curr_node = self.head
            if position==0:
                self.head = curr_node.next
                curr_node = None
                return
            previous_node = None
            count = 0
            while count != position:
                previous_node = curr_node
                curr_node = curr_node.next
                count+=1
            if curr_node is None:
                return
            previous_node.next = curr_node.next
            curr_node = None

    """
    get length
    """
    def lenght_of_linked_list(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            curr_node = curr_node.next
            count+=1
        return count

    def length_of_linked_list_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.length_of_linked_list_recursive(node.next)


    """
    swap nodes
    """
    def swap_nodes(self,val1,val2):

        curr_node_1 = self.head
        previous_node_1 = None
        while curr_node_1 and curr_node_1.data != val1:
            previous_node_1 = curr_node_1
            curr_node_1 = curr_node_1.next

        curr_node_2 = self.head
        previous_node_2 = None
        while curr_node_2 and curr_node_2.data != val2:
            previous_node_2 = curr_node_2
            curr_node_2 = curr_node_2.next

        if not curr_node_1 or not curr_node_2:
            return

        if previous_node_1:
            previous_node_1.next = curr_node_2
        else:
            self.head = curr_node_2

        if previous_node_2:
            previous_node_2.next = curr_node_1
        else:
            self.head = curr_node_1

        curr_node_1.next,curr_node_2.next = curr_node_2.next,curr_node_1.next

    """
    reverse linked list
    """
    def reverse_list_iteratively(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def reverse_linked_list_recursive(self):

        def _recursive(curr,prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            prev = curr
            return _recursive(curr,prev)

        self.head = _recursive(curr=self.head,prev=None)

    """
    merge sorted linked lists
    """
    def merge_sorted_linked_list(self,new_list):
        p = self.head
        q = new_list.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
            if not p:
                s.next = q
            if not q:
                s.next = p

        self.head = new_head




    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted_linked_list(llist_2)
llist_1.print_list()
