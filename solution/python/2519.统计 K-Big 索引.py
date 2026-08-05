"""2519. 统计 K-Big 索引"""


class Solution:
    def kBigIndices(self, nums: list[int], k: int) -> int:
        values = {value: index + 1 for index, value in enumerate(sorted(set(nums)))}
        size = len(values)
        tree = [0] * (size + 1)

        def add(index: int) -> None:
            while index <= size:
                tree[index] += 1
                index += index & -index

        def query(index: int) -> int:
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        left = [False] * len(nums)
        for index, value in enumerate(nums):
            rank = values[value]
            left[index] = query(rank - 1) >= k
            add(rank)
        tree = [0] * (size + 1)
        answer = 0
        seen = 0
        for index in range(len(nums) - 1, -1, -1):
            rank = values[nums[index]]
            if left[index] and query(rank - 1) >= k:
                answer += 1
            add(rank)
            seen += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 3, 6, 5, 1, 4], 2), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kBigIndices(*args) == expected
