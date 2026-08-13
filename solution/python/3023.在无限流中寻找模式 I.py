class Solution:
    def findPattern(self, stream: "InfiniteStream", pattern: list[int]) -> int:
        matched = 0
        index = 0
        while True:
            value = stream.next()
            while matched and value != pattern[matched]:
                matched = 0
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
    assert Solution().findPattern(Stream([1,2,3,4,5]), [3,4]) == 2
