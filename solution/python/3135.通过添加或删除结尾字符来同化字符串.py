"""3135. 通过添加或删除结尾字符来同化字符串"""


class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        previous = [0] * (len(target) + 1)
        longest = 0
        for first in initial:
            current = [0] * (len(target) + 1)
            for index, second in enumerate(target, 1):
                if first == second:
                    current[index] = previous[index - 1] + 1
                    longest = max(longest, current[index])
            previous = current
        return len(initial) + len(target) - 2 * longest


if __name__ == "__main__":
    test_cases = [(("abcde", "cdef"), 3), (("axxy", "yabx"), 6), (("xyz", "xyz"), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
