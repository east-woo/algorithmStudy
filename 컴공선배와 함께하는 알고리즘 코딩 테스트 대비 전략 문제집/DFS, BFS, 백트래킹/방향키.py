import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_tree():
    # Creating a binary tree for demonstration
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def bfs(root):
    if not root:
        return [], []

    q = deque([root])
    visit_order = []
    edges = []

    while q:
        node = q.popleft()
        visit_order.append(node.value)

        if node.left:
            q.append(node.left)
            edges.append((node.value, node.left.value))

        if node.right:
            q.append(node.right)
            edges.append((node.value, node.right.value))

    return visit_order, edges


# Build the binary tree
root = build_binary_tree()

# Perform BFS traversal
visit_order, edges = bfs(root)

# Create the graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Define the position of nodes in a tree layout
pos = nx.spring_layout(G, seed=42)  # You can change the layout for different visualization styles
labels = {node: str(node) for node in G.nodes()}

# Plot the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='skyblue', font_size=10, font_color='black',
        arrows=False)
plt.title("BFS Visit Order on Binary Tree")
plt.show()
