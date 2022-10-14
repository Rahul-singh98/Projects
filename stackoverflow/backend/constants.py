from enum import Enum


class Status(Enum):
    OPEN = 0
    CLOSED = 1
    DELETED = 2
    DEFAULT = 3


class AccountStatus(Enum):
    ACTIVE = 0
    CLOSED = 1
    CANCELED = 2
    BLACKLISTED = 3
    BLOCKED = 4