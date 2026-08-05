"""3910. 统计节点和为偶数的连通子图"""


class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        neighbors = [0] * n
        for left, right in edges:
            neighbors[left] |= 1 << right
            neighbors[right] |= 1 << left
        answer = 0
        for subset in range(1, 1 << n):
            if (
                subset.bit_count() % 2
                and sum(nums[index] for index in range(n) if subset >> index & 1) % 2
            ):
                continue
            start = subset & -subset
            reached = start
            frontier = start
            while frontier:
                neighbors_in = 0
                for index in range(n):
                    if frontier >> index & 1:
                        neighbors_in |= neighbors[index]
                frontier = neighbors_in & subset & ~reached
                reached |= frontier
            if (
                reached == subset
                and sum(nums[index] for index in range(n) if subset >> index & 1) % 2
                == 0
            ):
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 0, 1], [[0, 1], [1, 2]]), 2), (([1], []), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().evenSumSubgraphs(*args) == expected
