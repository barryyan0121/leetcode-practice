class Solution:
    def findPattern(self, stream: "InfiniteStream", pattern: list[int]) -> int:
        length = len(pattern)
        target = 0
        current = 0
        for bit in pattern:
            target = (target << 1) | bit
        mask = (1 << length) - 1
        for index in range(length):
            current = (current << 1) | stream.next()
        current &= mask
        index = length
        while current != target:
            current = ((current << 1) | stream.next()) & mask
            index += 1
        return index - length


if __name__ == "__main__":

    class Stream:
        def __init__(self, values):
            self.values, self.index = values, 0

        def next(self):
            value = self.values[self.index]
            self.index += 1
            return value

    assert Solution().findPattern(Stream([1, 0, 1, 1, 0]), [1, 1]) == 2
