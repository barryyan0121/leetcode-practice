class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        def solve(last1, last2):
            swaps = 0
            for a, b in zip(nums1[:-1], nums2[:-1]):
                if a <= last1 and b <= last2:
                    continue
                if b <= last1 and a <= last2:
                    swaps += 1
                else:
                    return 10**9
            return swaps

        answer = solve(nums1[-1], nums2[-1])
        answer = min(answer, 1 + solve(nums2[-1], nums1[-1]))
        return -1 if answer >= 10**9 else answer


assert Solution().minOperations([1, 2, 7], [4, 5, 3]) == 1
