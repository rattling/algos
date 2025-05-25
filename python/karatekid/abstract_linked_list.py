class AbstractLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.pointer

    def __repr__(self):
        nodes = [str(node.data) for node in self]
        return " -> ".join(nodes) if nodes else "Empty List"

    # Low-level insertion operations:
    def insert_at_head(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.pointer:
            curr = curr.pointer
        curr.pointer = new_node

    # The generic insertion method uses the hook to determine position.
    # By default, the hook always returns False, meaning no sorted insertion.
    def insert(self, data):
        new_node = Node(data, None)
        # If list is empty, insert at head.
        if self.head is None:
            self.head = new_node
            return

        # Use the hook: if the new data should be inserted before the head,
        # do that.
        if self.should_insert_before(self.head, data):
            new_node.pointer = self.head
            self.head = new_node
            return

        # Otherwise, traverse to find the right spot.
        curr = self.head
        while curr.pointer and not self.should_insert_before(curr.pointer, data):
            curr = curr.pointer
        new_node.pointer = curr.pointer
        curr.pointer = new_node

    # Hook method. In unsorted lists, it always returns False.
    def should_insert_before(self, node, new_data):
        return False

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.pointer
            return
        curr = self.head
        while curr and curr.pointer:
            if curr.pointer.data == data:
                curr.pointer = curr.pointer.pointer
                return
            curr = curr.pointer

    def search(self, data):
        for node in self:
            if node.data == data:
                return True
        return False


class UnsortedLinkedList(AbstractLinkedList):
    # For unsorted lists, we want to support both left and right insertion.
    # We can simply expose methods that use the low-level insertions.
    def add_left(self, data):
        self.insert_at_head(data)

    def add_right(self, data):
        self.insert_at_tail(data)

    # The generic 'insert' method here could be either hidden or repurposed;
    # typically, you'll use add_left/add_right for unsorted behavior.
    # We leave should_insert_before unchanged (always False).


class SortedLinkedList(AbstractLinkedList):
    def __init__(self, key=lambda x: x):
        super().__init__()
        self.key = key  # Function to extract the comparison key

    # Override the hook to enforce sorted order.
    def should_insert_before(self, node, new_data):
        # Insert new_data before node if its key is less than node.data's key.
        return self.key(new_data) < self.key(node.data)

    # In a sorted list, you typically don't expose left/right insertions
    # because they could break the sorted order.
    # The public API might only expose the generic 'insert' method.
    def add(self, data):
        self.insert(data)


class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

    def __repr__(self):
        return f"Node({self.data})"


# Example usage:
if __name__ == "__main__":
    # Unsorted list with left/right insertions:
    print("Unsorted list:")
    ul = UnsortedLinkedList()
    ul.add_left("apples")
    ul.add_left("oranges")
    ul.add_right("bananas")
    print(ul)
    ul.delete("oranges")
    print(ul)
    print("Search for 'bananas':", ul.search("bananas"))

    # Sorted list (sorted alphabetically):
    print("\nSorted list:")
    sl = SortedLinkedList(key=lambda x: x)
    sl.add("apples")
    sl.add("oranges")
    sl.add("bananas")
    print(sl)
    sl.delete("oranges")
    print(sl)
    print("Search for 'oranges':", sl.search("oranges"))
