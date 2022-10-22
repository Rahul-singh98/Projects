from .models import QuestionModel
from heapq import *
import pickle


class MostViewed:

    def __init__(self, max_size=10):
        self._object_instances = []
        self._max_size = max_size
        # try:
        #     with open('most_viewed_model', 'rb') as f:
        #         self._object_instances = pickle.load(f)
        # except Exception as e:
        #     print("[Error ]",e)
        # finally:
        # heapify(self._object_instances)

    def add(self, question: QuestionModel):
        if len(self._object_instances) >= self._max_size:
            heappop(self._object_instances)
            # self._pop_element()
        question.views = -1 * question.views
        if question not in self._object_instances:
            heappush(self._object_instances, question)
        else:
            idx = self._object_instances.index(question)
            self._object_instances[idx] = question
            heapify(self._object_instances)
        question.views = -1 * question.views

        # with open('most_viewed_model', 'wb') as f:
        #     pickle.dump(self._object_instances, f)
        # self._push_element(question)

    @property
    def get_list(self):
        return self._object_instances
