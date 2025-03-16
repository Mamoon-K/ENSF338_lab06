import timeit
import random


# Define the Node class for the BST
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


# Function to insert a node into the BST
def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)


# Function to search for a value in the BST
def search(root, data):
    current = root
    while current is not None:
        if current.data == data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None


# Function to build a BST from a list of elements
def build_bst(elements):
    root = None
    for el in elements:
        if root is None:
            root = Node(el)
        else:
            insert(el, root)
    return root


# Function to measure BST search performance
def measure_search_performance(elements):
    root = build_bst(elements)

    def search_all():
        for el in elements:
            search(root, el)

    time = timeit.timeit(search_all, number=10)
    return time / (10 * len(elements)), time


# Generate sorted and shuffled vectors
elements_sorted = list(range(10000))
elements_shuffled = elements_sorted[:]
random.shuffle(elements_shuffled)

# Measure performance for sorted insertions
avg_time_sorted, total_time_sorted = measure_search_performance(elements_sorted)
# Measure performance for shuffled insertions
avg_time_shuffled, total_time_shuffled = measure_search_performance(elements_shuffled)

# Print performance results
print(f"BST Performance Analysis:")
print(f"Average search time (sorted insertion): {avg_time_sorted:.10f} seconds per element")
print(f"Total search time (sorted insertion): {total_time_sorted:.10f} seconds (10 runs)")
print(f"Average search time (shuffled insertion): {avg_time_shuffled:.10f} seconds per element")
print(f"Total search time (shuffled insertion): {total_time_shuffled:.10f} seconds (10 runs)")


"""""

BST Performance Analysis:

Average search time (sorted insertion): avg_time_sorted seconds
Total search time (sorted insertion): total_time_sorted seconds
Average search time (shuffled insertion): avg_time_shuffled seconds
Total search time (shuffled insertion): total_time_shuffled seconds
A BST built from a sorted vector tends to become unbalanced, degenerating into a linked list,
which results in worse search performance (O(n) complexity instead of O(log n)).
Shuffling the elements before insertion helps create a more balanced tree,
improving search efficiency.

"""
