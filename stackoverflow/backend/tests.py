from django.test import TestCase
from .constants import *
from .manager import Admin, RegisteredMember
from .ood import Question


class TestRegistereMember(TestCase):

    def setUp(self) -> None:
        self._name = "test"
        self._d_name = "test_1234"
        self._email = "test@gmail.com"
        self._id = 1
        self._member = RegisteredMember(self._id, self._name, self._d_name, self._email)

    def test_getName(self):
        self.assertEqual(self._member.getName(), self._name)

    def test_getId(self):
        self.assertEqual(self._member.getId(), self._id)

    def test_getEmail(self):
        self.assertEqual(self._member.getEmail(), self._email)

    def test_getDisplayName(self):
        self.assertEqual(self._member.getDisplayName(), self._d_name)

    def test_cancelAccount(self):
        self._member.cancelAccount()
        self.assertIs(self._member.getStatus(), AccountStatus.CANCELED)

    def test_closeAccount(self):
        self._member.closeAccount()
        self.assertIs(self._member.getStatus(), AccountStatus.CLOSED)

    def test_blacklist(self):
        self._member.blacklist()
        self.assertIs(self._member.getStatus(), AccountStatus.BLACKLISTED)

    def test_block(self):
        self._member.block()
        self.assertIs(self._member.getStatus(), AccountStatus.BLOCKED)

    def test_blockMember(self):
        member = RegisteredMember(1, "test1", "tets2134sdf", "test2@gmail.com")
        self.assertFalse(self._member.blockMember(member))

    def test_unblockMember(self):
        member = RegisteredMember(1, "test1", "tets2134sdf", "test2@gmail.com")
        self.assertFalse(self._member.unblockMember(member))

    def test_receiveBounty(self):
        BOUNTY = 5
        self._member.receiveBounty(BOUNTY)
        self.assertEqual(self._member.getReputation(), BOUNTY)

    def test_closeQuestion(self):
        askingMember = RegisteredMember(2, "test1", "tets2134sdf", "test2@gmail.com")
        question = Question(1, askingMember, "Is zero or one", "Test Text")
        self.assertFalse(self._member.closeQuestion(question))


class TestAdmin(TestCase):

    def setUp(self) -> None:
        self.admin = Admin(1, "admin", "admin", "admin@gmail.com")
        self.member = RegisteredMember(2, "test1", "tets2134sdf", "test2@gmail.com")

    def test_blockMember(self):
        self.assertTrue(self.admin.blockMember(self.member))

    def test_unblockMember(self):
        self.admin.blockMember(self.member)
        self.assertTrue(self.admin.unblockMember(self.member))

    def test_closeQuestion(self):
        question = Question(1, self.member, "Is zero or one", "Test Text")
        self.assertTrue(self.admin.closeQuestion(question))