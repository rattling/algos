class SortedLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.pointer

    def __repr__(self):
        rep = ""
        for node in self:
            rep += "-->" + str(node.data)
        return rep if rep else "Empty List"

    def add(self, data, priority):
        if self.head is None:
            self.head = Node(data, None, priority)
        elif self.head.priority > priority:
            node = Node(data, self.head, priority)
            self.head = node
        else:
            curr = self.head
            while curr:
                if curr.pointer is None or curr.pointer.priority > priority:
                    curr.pointer = Node(data, curr.pointer, priority)
                    break
                curr = curr.pointer

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.pointer  # Update head correctly
            return
        curr = self.head
        while curr and curr.pointer:
            if curr.pointer.data == data:
                curr.pointer = curr.pointer.pointer
                break
            curr = curr.pointer

    def search(self, data):
        for node in self:
            if node.data == data:
                return True
        return False


class Node:
    def __init__(self, data, pointer, priority):
        self.data = data
        self.pointer = pointer
        self.priority = priority

    def __repr__(self):
        return f"Node({self.data}, priority={self.priority})"


if __name__ == "__main__":
    l = SortedLinkedList()  # Use SortedLinkedList, not LinkedList
    l.add("apples", 1)
    l.add("oranges", 2)
    l.add("bananas", 1)
    l.add("mangos", 3)
    print(l)
    l.delete("oranges")
    print(l)
    l.delete("mangos")
    print(l)
    print(l.search("mangos"))
    print(l.search("apples"))
