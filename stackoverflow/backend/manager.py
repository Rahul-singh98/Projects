from .models import QuestionModel
from .mixin import DecreasingViewsMixin, RecentMixin


class QuestionListManager:

    def __init__(self, max_size=10):
        self._context = [MostViewed(max_size), RecentCreated(max_size)]

    def add(self, question: QuestionModel):
        for context in self._context:
            context.add(question)

    @property
    def most_views_list(self):
        return self._context[0].get_list()

    @property
    def recently_created_list(self):
        return self._context[1].get_list()


class MostViewed:

    def __init__(self, max_size=10):
        self._object_instances = []
        self._max_size = max_size

    def add(self, question: QuestionModel):
        question = DecreasingViewsMixin(question)

        if len(self._object_instances) >= self._max_size:
            self._object_instances.pop()

        idx = self._is_exists(question)
        if idx == -1:
            self._object_instances.append(question)
            return
        self._object_instances[idx] = question

    def _is_exists(self, ques):
        for idx, q in enumerate(self._object_instances):
            if q.id == ques.id:
                return idx
        return -1

    def get_list(self):
        return sorted(self._object_instances)


class RecentCreated:

    def __init__(self, max_size=10):
        self._object_instances = []
        self._max_size = max_size

    def add(self, question: QuestionModel):
        question = RecentMixin(question)

        if len(self._object_instances) >= self._max_size:
            self._object_instances.pop()

        idx = self._is_exists(question)
        if idx == -1:
            self._object_instances.append(question)
            return
        self._object_instances[idx] = question

    def _is_exists(self, ques):
        for idx, q in enumerate(self._object_instances):
            if q.id == ques.id:
                return idx
        return -1

    def get_list(self):
        return sorted(self._object_instances)
