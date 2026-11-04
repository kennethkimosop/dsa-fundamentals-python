from dsa.arrays_strings import has_duplicate, is_anagram, two_sum


def test_has_duplicate():
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3]) is False
    assert has_duplicate([]) is False


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([1, 2], 10) == []
