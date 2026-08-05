"""2615. 等值距离和"""


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        from collections import defaultdict

        groups = defaultdict(list)
        for index, value in enumerate(nums):
            groups[value].append(index)
        answer = [0] * len(nums)
        for indexes in groups.values():
            total = sum(indexes)
            left = 0
            for position, index in enumerate(indexes):
                right = total - left - index
                answer[index] = (
                    index * position
                    - left
                    + right
                    - index * (len(indexes) - position - 1)
                )
                left += index
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 3, 1, 1, 2],), [5, 0, 3, 4, 0])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().distance(*args) == expected
