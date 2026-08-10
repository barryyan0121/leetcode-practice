"""2863. 半递减子数组的最大长度"""


class Solution:
    def maxSubarrayLength(self, nums: list[int]) -> int:
        values = sorted(set(nums))
        ranks = {value: index for index, value in enumerate(values)}
        size = len(values)
        tree = [10**9] * (size + 1)

        def update(index: int, value: int) -> None:
            while index <= size:
                tree[index] = min(tree[index], value)
                index += index & -index

        def query(index: int) -> int:
            answer = 10**9
            while index:
                answer = min(answer, tree[index])
                index -= index & -index
            return answer

        answer = 0
        for index, value in enumerate(nums):
            rank = size - ranks[value]
            first = query(rank - 1)
            if first < index:
                answer = max(answer, index - first)
            update(rank, index)
        return answer + 1 if answer else 0


if __name__ == "__main__":
    assert Solution().maxSubarrayLength([7, 6, 5, 4]) == 4
