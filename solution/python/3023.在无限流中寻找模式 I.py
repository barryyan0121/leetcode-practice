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
