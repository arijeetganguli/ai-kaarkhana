"""S5 improved implementation.

The lock is checked first and the grouping is explicit, so the code reads like
the requirement.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    is_admin: bool = False


@dataclass(frozen=True)
class Document:
    owner_id: int
    locked: bool = False


def can_edit(user, document):
    if document.locked:
        return False
    return user.is_admin or user.id == document.owner_id
