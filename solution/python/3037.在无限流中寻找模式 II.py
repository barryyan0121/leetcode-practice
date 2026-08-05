"""3037. 在无限流中寻找模式 II"""


class Solution:
    def findPattern(self, stream: "InfiniteStream", pattern: list[int]) -> int:
        failure = [0] * len(pattern)
        matched = 0
        for index in range(1, len(pattern)):
            while matched and pattern[index] != pattern[matched]:
                matched = failure[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            failure[index] = matched
        matched = 0
        index = 0
        while True:
            bit = stream.next()
            while matched and bit != pattern[matched]:
                matched = failure[matched - 1]
            if bit == pattern[matched]:
                matched += 1
            if matched == len(pattern):
                return index - len(pattern) + 1
            index += 1


if __name__ == "__main__":

    class Stream:
        def __init__(self):
            self.values = iter([1, 1, 1, 0, 1])

        def next(self):
            return next(self.values)

    test_cases = [((Stream(), [0, 1]), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findPattern(*args) == expected
