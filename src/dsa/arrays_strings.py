"""Array and string problems"""
from collections import Counter


def has_duplicate(nums):
    """Return True if any value appears more than once. Time: O(n). Space: O(n). """
    return len(nums) != len(set(nums))


def is_anagram(a, b):
    """Return True if b is a rearrangement of a.
    Time O(n). Space: O(1) for a fixed alphabet"""

    return Counter(a) == Counter(b)


def two_sum(nums, target):
    """Return the indices of two numbers that add up to target, or [].
    One pass with a dictionary of values already seen.

    Time O(n). Space: O(n). Checking every pair would be O(n squared)"""

    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
