from .models import QuestionModel
import pickle


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


class HomePageObjects:
    def __init__(self, max_size=10):
        self.most_viewed = MostViewed(max_size)

    def add(self, question: QuestionModel):
        self.most_viewed.add(question)


class MostVoted:
    def __init__(self, max_size=10):
        self._object_instances = []
        self._max_size = max_size


class MostViewed:

    def __init__(self, max_size=10):
        self._object_instances = []
        self._max_size = max_size

    def add(self, question: QuestionModel):
        if len(self._object_instances) >= self._max_size:
            self._object_instances.pop()
        
        idx = self._is_exists(question)
        if idx == -1:
            self._object_instances.append(question)
            return 
        self._object_instances[idx] = question

    def _is_exists(self, ques):
        for idx, q in enumerate(self._object_instances):
            if q.id == ques.id: return idx
        return -1

    @property
    def get_list(self):
        return sorted(self._object_instances)
