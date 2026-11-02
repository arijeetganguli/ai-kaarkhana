"""S5 initial implementation: may a user edit a document?

Requirement: a locked document cannot be edited by anyone. Otherwise admins and
the document owner may edit.

PROBLEM
    `and` binds tighter than `or`, so the expression means
    `is_admin or (is_owner and not locked)`. Admins bypass the lock.
"""


def can_edit(user, document):
    return user.is_admin or user.id == document.owner_id and not document.locked
