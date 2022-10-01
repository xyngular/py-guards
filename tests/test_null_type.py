from copy import copy, deepcopy

from guards import Null
from guards.null import NullType


def test_default_is_false_like():
    assert not Null


def test_only_one_default():
    assert Null is NullType()
    assert copy(Null) is Null
    assert deepcopy(Null) is Null


def test_example():
    from guards import Null

    class SomeClass:
        nullable_str = 'default-str'
        some_int = 3

        def json_dict(self):
            json_dict = {}
            if self.nullable_str is not None:
                json_dict['nullable_str'] = self.nullable_str
            if self.some_int is not None:
                json_dict['some_int'] = self.some_int

            return {k: v if v is not Null else None for k, v in json_dict.items()}

    obj = SomeClass()
    obj.nullable_str = Null
    obj.some_int = None
    assert obj.json_dict() == {'nullable_str': None}
