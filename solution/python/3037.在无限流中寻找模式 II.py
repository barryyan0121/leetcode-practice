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

if __name__ == "__main__":
    class Stream:
        def __init__(self, values): self.values, self.index = values, 0
        def next(self):
            value = self.values[self.index]; self.index += 1; return value
    assert Solution().findPattern(Stream([1,2,1,2,3]), [1,2,3]) == 2
