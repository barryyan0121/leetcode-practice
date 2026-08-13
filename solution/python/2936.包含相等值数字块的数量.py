class Solution(object):
    def countBlocks(self, nums) -> int:
        size = nums.size()
        answer = 0
        index = 0
        while index < size:
            value = nums.at(index)
            left, right = index, size - 1
            while left < right:
                middle = (left + right + 1) // 2
                if nums.at(middle) == value:
                    left = middle
                else:
                    right = middle - 1
            answer += 1
            index = left + 1
        return answer


if __name__ == "__main__":

    class Array:
        def __init__(self, values):
            self.values = values

        def size(self):
            return len(self.values)

        def at(self, index):
            return self.values[index]

    assert Solution().countBlocks(Array([1, 1, 2, 2, 2, 3])) == 3
