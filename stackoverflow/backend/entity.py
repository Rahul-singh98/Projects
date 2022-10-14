import time
from datetime import datetime
from .constants import Status


class TextPhotoBasedEntity:
    def __init__(self, id, creator, text, photos):
        self.id = 0
        self.text = None
        self.creationDateTime = 0
        self.lastUpdated = 0
        self.creator = None
        self.photos = None
        self.membersWhoDownvotedThisEntity = None
        self.membersWhoUpvotedThisEntity = None
        self.numberOfUsersReportedThisEntity = 0
        self.status = None

        self.id = id
        self.status = Status.DEFAULT
        self.creator = creator
        self.text = text
        photos = []
        if photos is not None:
            self.photos = photos
        self.membersWhoDownvotedThisEntity = set()
        self.membersWhoUpvotedThisEntity = set()
        self.creationDateTime = round(time.time() * 1000)
        self.lastUpdated = round(time.time() * 1000)
        self.numberOfUsersReportedThisEntity = 0

    def equals(self, that):
        if isinstance(that, TextPhotoBasedEntity):
            return self.id == (that).id
        return False

    def upVote(self, memberId):
        if not self.membersWhoUpvotedThisEntity.contains(memberId):
            if self.membersWhoDownvotedThisEntity.contains(memberId):
                self.membersWhoDownvotedThisEntity.remove(memberId)
            else:
                self.membersWhoUpvotedThisEntity.add(memberId)

    def downVote(self, memberId):
        if not self.membersWhoDownvotedThisEntity.contains(memberId):
            if self.membersWhoUpvotedThisEntity.contains(memberId):
                self.membersWhoUpvotedThisEntity.remove(memberId)
            else:
                self.membersWhoDownvotedThisEntity.add(memberId)

    def report(self):
        self.numberOfUsersReportedThisEntity += 1

    def updateText(self, text):
        self.text = text
        self.lastUpdated = round(time.time() * 1000)

    def removePhoto(self, photosToBeDeleted):
        self.photos.removeAll(photosToBeDeleted)
        self.lastUpdated = round(time.time() * 1000)

    def addPhotos(self, newPhotosToBeAdded):
        self.photos.extend(newPhotosToBeAdded)
        self.lastUpdated = round(time.time() * 1000)

    @property
    def getUpvoteCount(self):
        return len(self.membersWhoUpvotedThisEntity)

    @property
    def getDownvoteCount(self):
        return len(self.membersWhoDownvotedThisEntity)

    def getCreator(self):
        return self.creator

    def delete(self):
        self.status = Status.DELETED

    def getId(self):
        return self.id

    @property
    def getText(self):
        return self.text

    @property
    def getCreator(self):
        return self.creator

    @property
    def getCreationDateTime(self):
        return self.creationDateTime

    @property
    def getLastUpdated(self):
        return self.lastUpdated

    def getPhotos(self):
        return self.photos

    def getMembersWhoDownvotedThisEntity(self):
        return self.membersWhoDownvotedThisEntity

    def getMembersWhoUpvotedThisEntity(self):
        return self.membersWhoUpvotedThisEntity

    @property
    def getVoteCount(self):
        return self.getUpvoteCount - self.getDownvoteCount

    def getNumberOfUsersReportedThisEntity(self):
        return self.numberOfUsersReportedThisEntity

    def getStatus(self):
        return self.status

    @property
    def pretty_date(self):
        now = datetime.now()
        diff = now - datetime.fromtimestamp(self.lastUpdated//1000)
        seconds = diff.seconds
        days = diff.days

        if days < 0:
            return ""

        if days == 0:
            if seconds < 0:
                return "just now"
            if seconds < 60:
                return str(seconds) + " seconds ago"
            if seconds < 120:
                return "a minute ago"
            if seconds < 3600:
                return str(seconds // 60) + " minutes ago"
            if seconds < 7200:
                return "an hour ago"
            if seconds < 86400:
                return str(seconds // 3600) + " hours ago"
        if days == 1:
            return "Yesterday"
        if days < 7:
            return str(days) + " days ago"
        if days < 31:
            return str(days // 7) + " weeks ago"
        if days < 365:
            return str(days // 30) + " months ago"
        return str(days // 365) + " years ago"