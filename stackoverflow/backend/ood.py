from .constants import Status
from .entity import TextPhotoBasedEntity
import time


class Question(TextPhotoBasedEntity):
    def __init__(self, id, askingMember, title, text, photos=None, tags=None, bounty=0):
        self._title = None
        self._status = None
        self._bounty = None
        self._tags = None
        self._comments = None
        self._answers = None

        super().__init__(id, askingMember, text, photos)
        self._status = Status.OPEN
        self._title = title
        self._bounty = bounty
        if tags is not None:
            self._tags = tags
        else:
            self._tags = []
        self._comments = []
        self._answers = []

    def close(self):
        self._status = Status.CLOSED

    def addComment(self, newComment):
        self._comments.append(newComment)

    def addAnswer(self, newAnswer):
        self._answers.append(newAnswer)

    def getTitle(self):
        return self._title

    def getStatus(self):
        return self._status

    def getBounty(self):
        return self._bounty

    def getTags(self):
        return self._tags

    def getComments(self):
        return self._comments

    def getAnswers(self):
        return self._answers


class Answer(TextPhotoBasedEntity):
    def __init__(self, id, creatingMember, text, photos):
        self._solvedProblem = False
        self._comments = None

        super().__init__(id, creatingMember, text, photos)
        self._comments = []

    def markAsASolution(self):
        self._solvedProblem = True

    def updateText(self, text):
        self.text = text
        self.lastUpdated = round(time.time() * 1000)

    def addComment(self, newComment):
        self._comments.append(newComment)

    def receiveBounty(self, reputation, creator=None):
        creator.receiveBounty(reputation)

    def isSolvedProblem(self):
        return self._solvedProblem

    def getComments(self):
        return self._comments


class Comment(TextPhotoBasedEntity):
    def __init__(self, commenter, text, photos):
        super().__init__(commenter, text, photos)
