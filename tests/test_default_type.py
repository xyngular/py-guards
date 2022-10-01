from copy import copy, deepcopy

from guards import Default
from guards.default import DefaultType


def test_default_is_false_like():
    assert not Default


def test_only_one_default():
    assert Default is DefaultType()
    assert copy(Default) is Default
    assert deepcopy(Default) is Default
