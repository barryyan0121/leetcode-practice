class Solution:
    def findPattern(self, stream: "InfiniteStream", pattern: list[int]) -> int:
        prefix = [0] * len(pattern)
        matched = 0
        for index in range(1, len(pattern)):
            while matched and pattern[index] != pattern[matched]:
                matched = prefix[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            prefix[index] = matched
        matched = index = 0
        while True:
            value = stream.next()
            while matched and value != pattern[matched]:
                matched = prefix[matched - 1]
            if value == pattern[matched]:
                matched += 1
            if matched == len(pattern):
                return index - len(pattern) + 1
            index += 1
