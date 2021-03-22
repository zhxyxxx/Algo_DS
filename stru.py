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

#binary tree
class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class bitree:
    def __init__(self, root):
        self.root = node(root)

    def insert(self, key, n, lr) -> node:
        if lr == 0:
            assert n.left == None
            n.left = node(key)
            return n.left
        else:
            assert n.right == None
            n.right = node(key)
            return n.right

    # traversal
    def preorder(self, tree):
        if tree == None:
            return
        print(tree.key, end=' ')
        self.preorder(tree.left)
        self.preorder(tree.right)

    def inorder(self, tree):
        if tree == None:
            return
        self.inorder(tree.left)
        print(tree.key, end=' ')
        self.inorder(tree.right)

    def postorder(self, tree):
        if tree == None:
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


#BST
class BST(bitree):
    def __init__(self, root):
        super().__init__(root)

    def insert(self, key):
        n = self.root
        while n:
            parent = n
            if key < n.key:
                n = n.left
            else:
                n = n.right
        if key < parent.key:
            parent.left = node(key)
        else:
            parent.right = node(key)

    def search(self, key) -> node:
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
                if n.left==None and n.right==None:
                    if dire == -1:
                        parent.left = None
                    elif dire == 1:
                        parent.right = None
                    else:
                        self.root = None
                elif n.left==None:
                    if dire == -1:
                        parent.left = n.right
                    elif dire == 1:
                        parent.right = n.right
                    else:
                        self.root = n.right
                elif n.right==None:
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
                        if subn.left==None:
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
