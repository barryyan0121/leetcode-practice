class Solution:
    def maxBalancedSubsequenceSum(self, nums: list[int]) -> int:
        keys = sorted({value - index for index, value in enumerate(nums)})
        size = 1
        while size < len(keys):
            size <<= 1
        tree = [-(10**30)] * (2 * size)

        def query(right):
            result = -(10**30)
            left, right = size, size + right + 1
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left >>= 1
                right >>= 1
            return result

        answer = -(10**30)
        positions = {key: i for i, key in enumerate(keys)}
        for index, value in enumerate(nums):
            position = positions[value - index]
            best = query(position - 1)
            current = value + max(0, best)
            leaf = size + position
            tree[leaf] = max(tree[leaf], current)
            leaf >>= 1
            while leaf:
                tree[leaf] = max(tree[leaf * 2], tree[leaf * 2 + 1])
                leaf >>= 1
            answer = max(answer, current)
        return answer


assert Solution().maxBalancedSubsequenceSum([3, 3, 5, 6]) == 14
