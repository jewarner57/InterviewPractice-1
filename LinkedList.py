from Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def prepend(self, data):
        """Add an item to the beginning of the list."""

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

        # if only one node, set it to tail
        if self.tail is None:
            self.tail = self.head

    def append(self, data):
        """Add an item to the end of the list."""

        newNode = Node(data)

        if self.tail is not None:
            self.tail.next = newNode

        self.tail = newNode

        # if only one node set it to head
        if self.head is None:
            self.head = newNode

    def printList(self):
        """Print each item in the list."""
        node = self.head

        while node is not None:
            # print without a newline
            print(node.data, end=' ')
            node = node.next
        # print a new line
        print()

    def delete_from_head(self):
        """Delete the first item of the list."""
        if self.head is not None:
            self.head = self.head.next

    def delete_from_tail(self):
        """Delete the last item of the list."""
        if self.head is not None and self.tail is not None:
            node = self.head
            while node.next is not self.tail:
                node = node.next
            node.next = None
            self.tail = node

    def find(self, item):
        """Return true if item is found. Else return false"""
        node = self.head
        while node is not None:
            if node.data == item:
                return True
            node = node.next
        return False

    def delete(self, item):
        """Deletes an item in the list, sends true if deleted, false if not."""
        node = self.head
        prev = None

        while node is not None:
            if node.data == item:
                if prev is None:
                    self.delete_from_head()
                else:
                    prev.next = node.next
                return True

            prev = node
            node = node.next
        return False

    def reverse(self):
        """Reverse the linked list"""

        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        # Set the new head to be the last item
        self.head = prev
