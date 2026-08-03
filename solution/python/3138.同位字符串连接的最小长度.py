from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        length = len(s)
        divisors = [size for size in range(1, length + 1) if length % size == 0]
        for size in divisors:
            expected = Counter(s[:size])
            if all(
                Counter(s[index : index + size]) == expected
                for index in range(size, length, size)
            ):
                return size
        return length


if __name__ == "__main__":
    test_cases = [("abba", 2), ("cdef", 4), ("ababab", 2)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().minAnagramLength(s) == expected
