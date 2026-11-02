import itertools

import pytest

from kaarkhana.s05_boolean_logic import improved, initial
from kaarkhana.s05_boolean_logic.improved import Document, User

OWNER = 1
OTHER = 2


def expected(is_admin, is_owner, locked):
    """The requirement as a decision table: lock wins, then admin or owner."""
    return (not locked) and (is_admin or is_owner)


@pytest.mark.parametrize("is_admin,is_owner,locked", list(itertools.product([False, True], repeat=3)))
def test_every_combination_matches_the_requirement(is_admin, is_owner, locked):
    user = User(id=OWNER if is_owner else OTHER, is_admin=is_admin)
    document = Document(owner_id=OWNER, locked=locked)
    assert improved.can_edit(user, document) is expected(is_admin, is_owner, locked)


# --- Documented defect of the initial implementation (characterisation) ---


def test_initial_defect_admin_can_edit_a_locked_document():
    admin = User(id=OTHER, is_admin=True)
    locked = Document(owner_id=OWNER, locked=True)
    assert initial.can_edit(admin, locked) is True  # requirement says False
