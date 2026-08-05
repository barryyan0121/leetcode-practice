"""1983. 范围和相等的最宽索引对"""


class Solution:
    def widestPairOfIndices(self, nums1: list[int], nums2: list[int]) -> int:
        first = {0: -1}
        difference = 0
        answer = 0
        for index, (left, right) in enumerate(zip(nums1, nums2)):
            difference += left - right
            if difference not in first:
                first[difference] = index
            else:
                answer = max(answer, index - first[difference])
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 1, 0, 1], [1, 1, 1, 1]), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().widestPairOfIndices(*args) == expected
