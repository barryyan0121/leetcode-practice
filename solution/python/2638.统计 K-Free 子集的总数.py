"""2638. 统计 K-Free 子集的总数"""


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        counts = {}
        for value in nums:
            counts[value] = counts.get(value, 0) + 1
        answer = 1
        for residue in range(k):
            values = sorted(value for value in counts if value % k == residue)
            if not values:
                continue
            skip, take = 1, 0
            previous = None
            for value in values:
                weight = 2 ** counts[value]
                if previous is not None and value - previous == k:
                    skip, take = skip + take, skip * (weight - 1)
                else:
                    total = skip + take
                    skip, take = total, total * (weight - 1)
                previous = value
            answer *= skip + take
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 5, 7], 2), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countTheNumOfKFreeSubsets(*args) == expected
