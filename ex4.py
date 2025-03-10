import unittest
import random

class Heap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def heapify(self, index):
        """Heapifies downwards from a given index to maintain heap property."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def build_heap(self, arr):
        """Converts an input array into a valid heap."""
        self.heap = arr[:]  # Copy input array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)  # Fix the heap property from bottom-up

    def enqueue(self, element):
        """Adds an element while maintaining heap properties."""
        self.heap.append(element)
        index = len(self.heap) - 1
        parent = (index - 1) // 2

        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def dequeue(self):
        """Removes and returns the smallest element (min-heap root)."""
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root


# ------------------- UNIT TESTS -------------------

class TestHeap(unittest.TestCase):
    def test_sorted_heap(self):
        """Test when input is already a min-heap."""
        heap = Heap()
        sorted_heap = [1, 3, 5, 7, 9, 11, 13, 15]  # Already a valid min-heap
        heap.build_heap(sorted_heap)
        self.assertEqual(heap.heap, sorted_heap)  # Should not change

    def test_empty_heap(self):
        """Test when input is an empty list."""
        heap = Heap()
        heap.build_heap([])
        self.assertEqual(heap.heap, [])  # Heap should remain empty

    def test_random_shuffled_list(self):
        """Test when input is a long shuffled list."""
        heap = Heap()
        arr = list(range(1, 101))  # Numbers 1 to 100
        random.shuffle(arr)  # Shuffle the list
        heap.build_heap(arr)  # Convert to heap

        # Check if the heap property is maintained
        for i in range(len(heap.heap) // 2):  # Only check parent nodes
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap.heap):
                self.assertLessEqual(heap.heap[i], heap.heap[left])  # Parent <= left child
            if right < len(heap.heap):
                self.assertLessEqual(heap.heap[i], heap.heap[right])  # Parent <= right child

    def test_enqueue(self):
        """Test enqueue operation."""
        heap = Heap()
        heap.enqueue(10)
        heap.enqueue(5)
        heap.enqueue(15)
        heap.enqueue(2)

        self.assertEqual(heap.heap[0], 2)  # Root should be the smallest element

    def test_dequeue(self):
        """Test dequeue operation."""
        heap = Heap()
        heap.build_heap([10, 5, 15, 2, 7, 20])
        removed = heap.dequeue()

        self.assertEqual(removed, 2)  # Smallest element (2) should be dequeued
        self.assertTrue(all(heap.heap[i] <= heap.heap[2 * i + 1] for i in range(len(heap.heap) // 2)))  # Ensure heap property

if __name__ == "__main__":
    unittest.main()
