"""2568. 最小无法得到的或值"""


class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        values = set(nums)
        answer = 1
        while answer in values:
            answer <<= 1
        return answer


if __name__ == "__main__":
    assert Solution().minImpossibleOR([2, 1, 4]) == 8
