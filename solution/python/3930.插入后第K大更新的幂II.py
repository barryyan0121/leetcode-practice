"""3930. 插入后第 K 大更新的幂 II"""


class Solution:
    def powerUpdate(
        self, nums: list[int], p: int, queries: list[list[int]]
    ) -> list[int]:
        values = sorted(set(nums + [value for value, _ in queries]))
        index = {value: i + 1 for i, value in enumerate(values)}
        tree = [0] * (len(values) + 1)

        def add(position: int) -> None:
            while position < len(tree):
                tree[position] += 1
                position += position & -position

        def kth(rank: int) -> int:
            position = 0
            step = 1 << (len(tree).bit_length() - 1)
            while step:
                candidate = position + step
                if candidate < len(tree) and tree[candidate] < rank:
                    rank -= tree[candidate]
                    position = candidate
                step >>= 1
            return values[position]

        for value in nums:
            add(index[value])
        mod = 1_000_000_007
        answer = []
        for value, rank_from_largest in queries:
            add(index[value])
            rank_from_smallest = len(nums) + len(answer) + 2 - rank_from_largest
            exponent = kth(rank_from_smallest)
            p = pow(p, exponent, mod)
            answer.append(p)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2], 4, [[3, 1], [1, 2]]), [64, 4096]),
        (([7, 5], 6, [[4, 3], [7, 2]]), [1296, 220296870]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().powerUpdate(*args) == expected
