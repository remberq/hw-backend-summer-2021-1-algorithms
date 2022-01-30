from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    @staticmethod
    def sorting(lst):
        new = []
        for item in lst:
            if item not in new:
                new.append(item)
        return new

    def dfs(self) -> list[Node]:

        def walker(node, path):
            outer = node.outbound
            if node in path:
                return []
            path.append(node)
            if outer:
                for nod in outer:
                    path.extend(walker(nod, path))
            return self.sorting(path)

        return walker(self._root, [])

    def bfs(self) -> list[Node]:
        visited = []
        queue = []
        visited.append(self._root)
        queue.extend(self._root.outbound)
        while queue:
            s = queue.pop(0)
            if s not in visited:
                visited.append(s)
                queue.extend(s.outbound)
        return visited


a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)
a.point_to(c)
g = Graph(a)
print(g.bfs())
