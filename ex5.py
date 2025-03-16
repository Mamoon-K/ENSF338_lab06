import heapq
import random
import timeit

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head or self.head.value > value:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.value < value:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, value):
        heapq.heappush(self.heap, value)
    
    def dequeue(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

def measure_execution_time(queue_class):
    queue = queue_class()
    operations = [("enqueue", random.randint(1, 1000)) if random.random() < 0.7 else ("dequeue", None) for _ in range(1000)]
    
    start_time = timeit.default_timer()
    for op, val in operations:
        if op == "enqueue":
            queue.enqueue(val)
        else:
            queue.dequeue()
    total_time = timeit.default_timer() - start_time
    
    return total_time, total_time / len(operations)

if __name__ == "__main__":
    list_time, list_avg = measure_execution_time(ListPriorityQueue)
    heap_time, heap_avg = measure_execution_time(HeapPriorityQueue)
    
    print(f"List-based Priority Queue: Total Time = {list_time:.6f}s, Average Time per Operation = {list_avg:.6f}s")
    print(f"Heap-based Priority Queue: Total Time = {heap_time:.6f}s, Average Time per Operation = {heap_avg:.6f}s")
    
    # Discussion:
    # The heap-based priority queue is generally faster than the linked list-based implementation.
    # Enqueue in a linked list requires O(n) time due to sorted insertion, while a heap allows O(log n) insertion.
    # Dequeue in both cases is O(1) for a linked list and O(log n) for a heap, but since enqueues are more frequent (70% vs. 30%),
    # the heap-based approach outperforms the linked list in overall execution time.
