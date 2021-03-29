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
q = algo.quick_sort(q)
print(q)

v = [0, 1, 2, 3, 4]
e = [[0, 1], [1, 2], [0, 2], [2, 3], [0, 3], [3, 4]]
g = stru.Graph(v, e)
g.dfs(0)
g.bfs(0)

v2 = range(6)
e2 = [[0, 1, 6], [0, 2, 4], [1, 3, 3], [4, 1, 2], [2, 4, 3], [4, 3, 1], [2, 5, 6]]
g2 = stru.Graph(v2, e2)
path = g2.dijkstra(0)
print(path)

v3 = range(3)
e3 = [[0, 1, 8], [1, 0, 3], [2, 1, 2], [0, 2, 5]]
g3 = stru.DirectedGraph(v3, e3)
dist = g3.floyd_warshall()
print(dist)
