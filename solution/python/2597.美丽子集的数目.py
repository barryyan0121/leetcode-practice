"""2597. 美丽子集的数目"""


class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        nums.sort()
        chosen = []

        def backtrack(index: int) -> int:
            if index == len(nums):
                return 1
            answer = backtrack(index + 1)
            if all(abs(nums[index] - value) != k for value in chosen):
                chosen.append(nums[index])
                answer += backtrack(index + 1)
                chosen.pop()
            return answer

        return backtrack(0) - 1


if __name__ == "__main__":
    test_cases = [(([2, 4, 6], 2), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().beautifulSubsets(*args) == expected
