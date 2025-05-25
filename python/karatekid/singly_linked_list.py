class LinkedList:
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
        return rep

    def add_left(self, data):
        node = Node(data, self.head)
        self.head = node

    def add_right(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            for n in self:
                if n.pointer is None:
                    n.pointer = Node(data, None)
                    break

    def delete(self, data):
        if self.head.data == data:
            self.head.pointer = None
        else:
            curr = self.head
            while curr.pointer:
                if curr.pointer.data == data:
                    curr.pointer = (
                        curr.pointer.pointer if curr.pointer.pointer else None
                    )
                    break
                curr = curr.pointer

    def search(self, data):
        for node in self:
            if node.data == data:
                return True
        return False


class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


if __name__ == "__main__":
    l = LinkedList()
    l.add_left("apples")
    l.add_left("oranges")
    l.add_left("bananas")
    l.add_right("mangos")
    print(l)
    l.delete("oranges")
    print(l)
    l.delete("mangos")
    print(l)
    print(l.search("mangos"))
    print(l.search("apples"))
