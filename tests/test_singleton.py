from copy import copy, deepcopy

from guards import Singleton


def test_ensure_only_one():
    class MyType(Singleton):
        pass

    assert MyType() is MyType()
    My = MyType()

    assert copy(My) is My
    assert deepcopy(My) is My


