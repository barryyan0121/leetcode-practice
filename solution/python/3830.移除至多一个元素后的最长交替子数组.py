from typing import List


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 1
        up0 = [1] * n
        down0 = [1] * n
        up1 = [1] * n
        down1 = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                up0[i] = down0[i - 1] + 1
                up1[i] = down1[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                down0[i] = up0[i - 1] + 1
                down1[i] = up1[i - 1] + 1
            if i == 1:
                up1[i] = down1[i] = 1
            else:
                if nums[i - 2] < nums[i]:
                    up1[i] = max(up1[i], down0[i - 2] + 1)
                elif nums[i - 2] > nums[i]:
                    down1[i] = max(down1[i], up0[i - 2] + 1)
            answer = max(answer, up0[i], down0[i], up1[i], down1[i])
        return answer


if __name__ == "__main__":
    assert Solution().longestAlternating([1, 2, 3, 2, 1]) == 3
