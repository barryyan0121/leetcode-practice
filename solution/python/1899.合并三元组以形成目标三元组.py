"""1899. 合并三元组以形成目标三元组"""


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        best = [0, 0, 0]
        for triplet in triplets:
            if all(value <= limit for value, limit in zip(triplet, target)):
                best = [max(a, b) for a, b in zip(best, triplet)]
        return best == target


if __name__ == "__main__":
    assert Solution().mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])
