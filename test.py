import algo
import stru

ans = algo.gcd(315, 189)
print(ans)

mylist = [1, 3, 5, 7, 9]
index = algo.bi_search(mylist, 9)
print(index)

tree = stru.BiTree(0)
n1 = tree.insert(1, tree.root, 0)
n2 = tree.insert(2, tree.root, 1)
tree.insert(3, n1, 0)
tree.insert(5, n1, 1)
n6 = tree.insert(6, n2, 0)
tree.insert(7, n2, 1)
tree.insert(8, n6, 0)
tree.insert(9, n6, 1)
tree.traversal('pre')
tree.traversal('in')
tree.traversal('post')

bst = stru.BST(6)
keylist = [2, 8, 1, 4, 7, 10, 3, 5, 9, 11]
for i in keylist:
    bst.insert(i)
bst.traversal()
n = bst.search(5)
print(n.key)
bst.delete(5)
bst.delete(6)
bst.delete(10)
bst.traversal()

q = [9, 2, 5, 3, 1, 0, -1, 3]
algo.bubble_sort(q)
print(q)
