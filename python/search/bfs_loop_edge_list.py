from collections import deque

print("Hello")


def BFS(graph, root):
    q = deque()
    visited = set()

    q.append(root)
    visited.add(root)

    while q:
        node = (
            q.popleft()
        )  # popleft for FIFO. Taking something off the queue as we have (or are about to) explore its immediate neighbours already
        print(node)

        for neighbour in graph.get(
            node, []
        ):  # useful to prevent errors on terminal nodes (leaves)
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"]}
graph = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
]
BFS(graph, next(iter(graph)))
