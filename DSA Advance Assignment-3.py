#1.Implement Binary tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)
if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    search_key = 40
    result = search(root, search_key)
    if result:
        print(f"\n{search_key} found in the tree.")
    else:
        print(f"\n{search_key} not found in the tree.")
#2.Find height of a given tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def find_height(root):
    if root is None:
        return -1  
    else:
        left_height = find_height(root.left)
        right_height = find_height(root.right)
        return max(left_height, right_height) + 1
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    height = find_height(root)
    print(f"The height of the tree is: {height}")
#3.Perform Pre-order, Post-order, In-order traversal
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")
if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    print("Inorder Traversal:")
    inorder_traversal(root)
    print("\nPreorder Traversal:")
    preorder_traversal(root)
    print("\nPostorder Traversal:")
    postorder_traversal(root)
#4.Function to print all the leaves in a given binary tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def print_leaves(root):
    if root:
        if root.left is None and root.right is None:
            print(root.val, end=" ")  # Print the leaf node
        else:
            print_leaves(root.left)
            print_leaves(root.right)
if __name__ == "__main__":
    # Construct a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Leaf nodes in the binary tree:")
    print_leaves(root)
#5.Implement BFS (Breath First Search) and DFS (Depth First Search)
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Breadth-First Search (BFS):")
    g.bfs(2)
    print("\nDepth-First Search (DFS):")
    visited = [False] * len(g.graph)
    g.dfs(2, visited)
#6.Find sum of all left leaves in a given Binary Tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def sum_of_left_leaves(root):
    if root is None:
        return 0
    if root.left and root.left.left is None and root.left.right is None:
        left_leaf_sum = root.left.val
    else:
        left_leaf_sum = 0
    left_sum = sum_of_left_leaves(root.left)
    right_sum = sum_of_left_leaves(root.right)
    return left_leaf_sum + left_sum + right_sum
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(19)
    root.right = TreeNode(27)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(16)
    result = sum_of_left_leaves(root)
    print(f"The sum of left leaves in the binary tree is: {result}")
#7.Find sum of all nodes of the given perfect binary tree
def sum_of_perfect_binary_tree(height):
    total_nodes = (2 ** (height + 1)) - 1
    sum_nodes = total_nodes * (total_nodes + 1) // 2
    return sum_nodes
if __name__ == "__main__":
    tree_height = int(input("Enter the tree_height:"))
    result = sum_of_perfect_binary_tree(tree_height)
    print(f"The sum of all nodes in a perfect binary tree of height {tree_height} is: {result}")
#8.Count subtress that sum up to a given value x in a binary tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def count_subtrees_with_sum(root, x):
    if root is None:
        return 0
    left_count = count_subtrees_with_sum(root.left, x)
    right_count = count_subtrees_with_sum(root.right, x)
    current_sum = root.val + left_count + right_count
    if current_sum == x:
        return 1 + left_count + right_count
    else:
        return left_count + right_count
if __name__ == "__main__":
    # Construct a sample binary tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    target_sum = int(input("Enter the target_sum:"))
    result = count_subtrees_with_sum(root, target_sum)
    print(f"Number of subtrees with the sum {target_sum}: {result}")
#9.Find maximum level sum in Binary Tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def max_level_sum(root):
    if root is None:
        return 0
    max_sum = float('-inf')  
    result_level = 1  
    level = 1 
    queue = [root]
    while queue:
        level_sum = 0
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum
            result_level = level
        level += 1
    return result_level, max_sum
if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(10)
    level, _sum = max_level_sum(root)
    print(f"Maximum level sum is at level {level} with a sum of {_sum}")
#10.Print the nodes at odd levels of a tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def print_nodes_at_odd_levels(root, level=1):
    if root is None:
        return
    if level % 2 != 0:
        print(root.val, end=" ")
    print_nodes_at_odd_levels(root.left, level + 1)
    print_nodes_at_odd_levels(root.right, level + 1)
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(17)
    print("Nodes at odd levels:")
    print_nodes_at_odd_levels(root)