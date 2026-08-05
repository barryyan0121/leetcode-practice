"""2407. 最长递增子序列 II"""


class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        size = max(nums) + 1
        tree = [0] * (2 * size)

        def query(left: int, right: int) -> int:
            answer = 0
            left += size
            right += size + 1
            while left < right:
                if left & 1:
                    answer = max(answer, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    answer = max(answer, tree[right])
                left //= 2
                right //= 2
            return answer

        for value in nums:
            best = query(max(0, value - k), value - 1) + 1
            index = value + size
            tree[index] = max(tree[index], best)
            index //= 2
            while index:
                tree[index] = max(tree[index * 2], tree[index * 2 + 1])
                index //= 2
        return tree[1]


if __name__ == "__main__":
    test_cases = [(([4, 2, 1, 4, 3, 4, 5, 8, 15], 3), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().lengthOfLIS(*args) == expected
