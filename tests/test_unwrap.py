from xsentinels import unwrap_union, Null, Nullable
from typing import Union, Optional, List
import pytest
from xsentinels.unwrap import UnwrapResults


@pytest.mark.parametrize("test_type,expected_result", [
    (str, UnwrapResults(str, False, False)),
    (Nullable[int], UnwrapResults(int, True, False)),
    (Optional[Nullable[str]], UnwrapResults(str, True, True)),
    (Optional[List[str]], UnwrapResults(List[str], False, True))
])
def test_unwrap(test_type, expected_result):
    result = unwrap_union(test_type)
    assert result.unwrapped_type is expected_result.unwrapped_type
    assert result.is_nullable is expected_result.is_nullable
    assert result.is_optional is expected_result.is_optional
