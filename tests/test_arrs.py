from utils import arrs
from utils.dicts import get_val


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2]) == [1, 2]


def test_get_val():
    assert arrs.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert arrs.get_val({"git": "mercurial"}) == "mercurial"
    assert arrs.get_val({}, "vcs") == 'git'
    assert arrs.get_val({}, "vcs", "bazaar") == 'bazaar'
