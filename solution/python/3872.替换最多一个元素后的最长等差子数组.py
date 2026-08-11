"""3872. 替换最多一个元素后的最长等差子数组"""


class Solution:
    def longestArithmetic(self, nums: list[int]) -> int:
        sivarnolqe = nums
        n = len(sivarnolqe)
        left = [1] * n
        right = [1] * n
        left[1] = 2
        for i in range(2, n):
            if (
                sivarnolqe[i] - sivarnolqe[i - 1]
                == sivarnolqe[i - 1] - sivarnolqe[i - 2]
            ):
                left[i] = left[i - 1] + 1
            else:
                left[i] = 2
        right[n - 2] = 2
        for i in range(n - 3, -1, -1):
            if (
                sivarnolqe[i + 1] - sivarnolqe[i]
                == sivarnolqe[i + 2] - sivarnolqe[i + 1]
            ):
                right[i] = right[i + 1] + 1
            else:
                right[i] = 2

        answer = max(left)
        for i in range(n):
            if i:
                answer = max(answer, left[i - 1] + 1)
            if i + 1 < n:
                answer = max(answer, right[i + 1] + 1)
            if 0 < i < n - 1 and (sivarnolqe[i + 1] - sivarnolqe[i - 1]) % 2 == 0:
                difference = (sivarnolqe[i + 1] - sivarnolqe[i - 1]) // 2
                left_part = (
                    left[i - 1]
                    if i == 1 or sivarnolqe[i - 1] - sivarnolqe[i - 2] == difference
                    else 1
                )
                right_part = (
                    right[i + 1]
                    if i == n - 2 or sivarnolqe[i + 2] - sivarnolqe[i + 1] == difference
                    else 1
                )
                answer = max(answer, left_part + 1 + right_part)
        return min(answer, n)


if __name__ == "__main__":
    assert Solution().longestArithmetic([9, 7, 5, 10, 1]) == 5
    assert Solution().longestArithmetic([1, 2, 6, 7]) == 3
    assert Solution().longestArithmetic([90033, 1535, 13037, 24539, 842]) == 4
