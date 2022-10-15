from .constants import AccountStatus


class Member:

    def __init__(self, id):
        self._id = id
        self._accountStatus = 0
        self._name = None
        self._displayName = None
        self._email = None
        self._reputation = 0
        self._isModerator = False
        self._isAdmin = False

        self._accountStatus = AccountStatus.ACTIVE

    def closeAccount(self):
        self._accountStatus = AccountStatus.CLOSED

    def cancelAccount(self):
        self._accountStatus = AccountStatus.CANCELED

    def blacklist(self):
        self._accountStatus = AccountStatus.BLACKLISTED

    def block(self):
        self._accountStatus = AccountStatus.BLOCKED

    def blockMember(self, member):
        if self._isAdmin:
            member.block()
            return True
        return False

    def unblockMember(self, member):
        if self._isAdmin:
            member._accountStatus = AccountStatus.ACTIVE
            return True
        return False

    def closeQuestion(self, question):
        if self._isAdmin or self._isModerator or self._id == question.getCreator().getId():
            question.close()
            return True
        return False

    def promoteToAdmin(self):
        self._isAdmin = True

    def promoteToModerator(self):
        self._isModerator = True

    def giveBountyTo(self, bountyReputation, receiver):
        if bountyReputation <= self.getReputation() and self._id != receiver.getId():
            self._reputation -= bountyReputation
            receiver.receiveBounty(bountyReputation)
        return False

    @property
    def receiveBounty(self, bountyReputation):
        self._reputation += bountyReputation

    @property
    def getReputation(self):
        return self._reputation

    @property
    def getId(self):
        return self._id

    @property
    def getStatus(self):
        return self._accountStatus

    @property
    def getName(self):
        return self._name

    @property
    def getDisplayName(self):
        return self._displayName

    @property
    def getEmail(self):
        return self._email


class RegisteredMember(Member):
    
    def __init__(self, id, name, displayName, email):
        super().__init__(id)
        self._name = name
        self._displayName = displayName
        self._email = email
        


class Admin(Member):

    def __init__(self, id, name, displayName, email):
        super().__init__(id)
        self._name = name
        self._displayName = displayName
        self._email = email
        self.promoteToAdmin()


class Moderator(Member):

    def __init__(self, id, name, displayName, email):
        super().__init__(id)
        self._name = name
        self._displayName = displayName
        self._email = email
        self.promoteToModerator()
        