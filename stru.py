import collections
from collections import deque
import heapq
from collections import defaultdict

'''
# list
mylist = []
mylist.append(3)
mylist.extend([5,7,9])
mylist.insert(0, 1)
mylist.pop()
mylist.pop(0)
mylist.remove(5)
print(mylist)

# stack
mystack = deque(range(5))
mystack.pop()
mystack.append(12)
print(mystack)

# queue
myqueue = deque(range(5))
myqueue.popleft()
myqueue.append(12)
print(myqueue)

# heap
myheap = [5, 1, -3, 0, 8]
heapq.heapify(myheap)
print(myheap)
minimum = heapq.heappop(myheap)
heapq.heappush(myheap, 3)
print(minimum, myheap)

# hash table
# set
myset = set([1, 3, 3, 5, 6])
myset.add(2)
myset.remove(5)
print(myset)
# dict
mydict = {'a': 1, 'c': 3, 'z': 26}
mydict['x'] = 24
mydict.pop('c')
print(mydict)
# ex: defalut dict
myddict = defaultdict(int)
myddict['a'] += 1
print(myddict)
'''


# binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BiTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, key, n, lr) -> Node:
        if lr == 0:
            assert n.left is None
            n.left = Node(key)
            return n.left
        else:
            assert n.right is None
            n.right = Node(key)
            return n.right

    # traversal
    def preorder(self, tree):
        if tree is None:
            return
        print(tree.key, end=' ')
        self.preorder(tree.left)
        self.preorder(tree.right)

    def inorder(self, tree):
        if tree is None:
            return
        self.inorder(tree.left)
        print(tree.key, end=' ')
        self.inorder(tree.right)

    def postorder(self, tree):
        if tree is None:
            return
        self.postorder(tree.left)
        self.postorder(tree.right)
        print(tree.key, end=' ')

    def traversal(self, dire='in'):
        assert dire in ['pre', 'in', 'post']
        if dire == 'pre':
            self.preorder(self.root)
            print()
        elif dire == 'in':
            self.inorder(self.root)
            print()
        elif dire == 'post':
            self.postorder(self.root)
            print()


# BST
class BST(BiTree):
    def __init__(self, root):
        super().__init__(root)

    def insert(self, key):
        n = self.root
        parent = n
        while n:
            parent = n
            if key < n.key:
                n = n.left
            else:
                n = n.right
        if key < parent.key:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

    def search(self, key) -> Node:
        n = self.root
        while n:
            if key < n.key:
                n = n.left
            elif key > n.key:
                n = n.right
            else:
                return n
        return None

    def delete(self, key):
        n = self.root
        parent = n
        dire = 0
        while n:
            if key == n.key:
                if n.left is None and n.right is None:
                    if dire == -1:
                        parent.left = None
                    elif dire == 1:
                        parent.right = None
                    else:
                        self.root = None
                elif n.left is None:
                    if dire == -1:
                        parent.left = n.right
                    elif dire == 1:
                        parent.right = n.right
                    else:
                        self.root = n.right
                elif n.right is None:
                    if dire == -1:
                        parent.left = n.left
                    elif dire == 1:
                        parent.right = n.left
                    else:
                        self.root = n.left
                else:
                    subn = n.right
                    subparent = n
                    counter = 0
                    while True:
                        if subn.left is None:
                            break
                        subparent = subn
                        subn = subn.left
                        counter += 1
                    n.key = subn.key
                    if counter == 0:
                        subparent.right = None
                    else:
                        subparent.left = None
                return
            elif key < n.key:
                parent = n
                n = n.left
                dire = -1
            else:
                parent = n
                n = n.right
                dire = 1


# graph
class Graph:
    def __init__(self, v, edge):
        self.v = v
        self.e = [[] for _ in range(len(v))]
        for e in edge:
            self.e[e[0]].append(e[1])
            self.e[e[1]].append(e[0])

    # search
    def dfs(self, start):
        vnum = len(self.v)
        visited = [False for _ in range(vnum)]
        stack = deque([start])
        while stack:
            v0 = stack.pop()
            if not visited[v0]:
                print(v0, end=' ')
            visited[v0] = True
            for v in self.e[v0]:
                if not visited[v]:
                    stack.append(v)
        print()

    def bfs(self, start):
        vnum = len(self.v)
        visited = [False for _ in range(vnum)]
        queue = deque([start])
        while queue:
            v0 = queue.popleft()
            if not visited[v0]:
                print(v0, end=' ')
            visited[v0] = True
            for v in self.e[v0]:
                if not visited[v]:
                    queue.append(v)
        print()
