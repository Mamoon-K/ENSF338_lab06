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
        return Node(data)  # Return new root
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
    return root  # Always return root


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
def measure_bst_performance(elements):
    root = build_bst(elements)

    def search_all():
        for el in elements:
            search(root, el)

    time = timeit.timeit(search_all, number=10)
    return time / (10 * len(elements)), time


# Function to perform binary search
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Function to measure binary search performance
def measure_binary_search_performance(elements):
    sorted_elements = sorted(elements)

    def search_all():
        for el in elements:
            binary_search(sorted_elements, el)

    time = timeit.timeit(search_all, number=10)
    return time / (10 * len(elements)), time


# Generate sorted and shuffled vectors
elements_sorted = list(range(10000))
elements_shuffled = elements_sorted[:]
random.shuffle(elements_shuffled)

# Measure BST performance
avg_time_bst, total_time_bst = measure_bst_performance(elements_shuffled)

# Measure Binary Search performance
avg_time_binary, total_time_binary = measure_binary_search_performance(elements_shuffled)

# Print performance results
print("BST vs Binary Search Performance Analysis:")
print(f"Average search time (BST): {avg_time_bst:.10f} seconds per element")
print(f"Total search time (BST): {total_time_bst:.10f} seconds (10 runs)")
print(f"Average search time (Binary Search): {avg_time_binary:.10f} seconds \
per element")
print(f"Total search time (Binary Search): {total_time_binary:.10f} seconds \
(10 runs)")

# Performance analysis
# The BST is generally slower for search operations compared to binary search
# in a sorted array. This is because BST search time complexity can degrade to
# O(n) if the tree is unbalanced, whereas binary search always operates in O(log n).
# Sorting the array before performing binary search ensures a consistent and
# efficient searching mechanism.
# Thus, binary search is expected to usually be faster than searching in
# a BST, especially in cases where the BST is unbalanced. If the tree has
# degenerated into a linked list (see ex1 for details), then binary search
# could be faster. This shows when running the program multiple times.
# Sometimes binary search is faster, and sometimes BST is faster.
