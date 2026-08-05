"""2121. 相同元素的间隔之和"""


class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        positions = {}
        for index, value in enumerate(arr):
            positions.setdefault(value, []).append(index)
        answer = [0] * len(arr)
        for indices in positions.values():
            count = len(indices)
            prefix = 0
            for order, index in enumerate(indices):
                answer[index] += order * index - prefix
                prefix += index
            suffix = 0
            for order in range(count - 1, -1, -1):
                index = indices[order]
                answer[index] += suffix - (count - 1 - order) * index
                suffix += index
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 1, 3, 1, 2, 3, 3],), [4, 2, 7, 2, 4, 4, 5])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getDistances(*args) == expected
