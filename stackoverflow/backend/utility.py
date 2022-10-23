def max_heapify(heap: list, idx: int):
    size = len(heap)
    if size < 1: return

    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < size and heap[largest] < heap[left]:
        largest = left

    if right < size and heap[largest] < heap[right]:
        largest = right
    
    if(largest != idx):
        heap[largest], heap[idx] = heap[idx], heap[largest]
        max_heapify(heap, largest)


def min_heapify(heap: list, idx: int):
    size = len(heap)
    if size < 1: return

    minimum = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < size and heap[minimum] > heap[left]:
        minimum = left

    if right < size and heap[minimum] > heap[right]:
        minimum = right
    
    if(minimum != idx):
        heap[minimum], heap[idx] = heap[idx], heap[minimum]
        min_heapify(heap, minimum)
