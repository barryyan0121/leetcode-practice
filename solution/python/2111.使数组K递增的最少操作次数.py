"""2111. 使数组 K 递增的最少操作次数"""

from bisect import bisect_right


class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        answer = 0
        for start in range(k):
            sequence = arr[start::k]
            lis = []
            for value in sequence:
                index = bisect_right(lis, value)
                if index == len(lis):
                    lis.append(value)
                else:
                    lis[index] = value
            answer += len(sequence) - len(lis)
        return answer


if __name__ == "__main__":
    test_cases = [(([5, 4, 3, 2, 1], 1), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kIncreasing(*args) == expected
