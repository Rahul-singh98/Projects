from .models import QuestionModel


class BaseMixin:

    def __init__(self, question: QuestionModel):
        self._base = question

    @property
    def title(self):
        return self._base.title

    @property
    def id(self):
        return self._base.id

    @property
    def entity(self):
        return self._base.entity

    @property
    def answer(self):
        return self._base.answer

    @property
    def tags(self):
        return self._base.tags

    @property
    def comments(self):
        return self._base.comments

    @property
    def views(self):
        return self._base.views

    @property
    def getVoteCount(self):
        return len(self._base.entity.membersWhoDownvoted.all()) - len(self._base.entity.membersWhoUpvoted.all())

    @property
    def getAnswersCount(self):
        return len(self._base.answer.all())

    @property
    def getTags(self):
        return self._base.tags.all()

    @property
    def getComments(self):
        return self._base.comments.all()

    @property
    def getAnswers(self):
        return self._base.answer.all()

    @property
    def votes_count(self):
        return self._base.votes_count


class DecreasingViewsMixin(BaseMixin):

    def __lt__(self, cls):
        return self.views > cls.views

    def __eq__(self, cls):
        return self.views == cls.views

    def __gt__(self, cls):
        return self.views < cls.views


class RecentMixin(BaseMixin):

    def __lt__(self, cls):
        return self.entity.creationDateTime > cls.entity.creationDateTime

    def __eq__(self, cls):
        return self.entity.creationDateTime == cls.entity.creationDateTime

    def __gt__(self, cls):
        return self.entity.creationDateTime < cls.entity.creationDateTime