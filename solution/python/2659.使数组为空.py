"""2659. 使数组为空"""


class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        n = len(nums)
        tree = [0] * (n + 1)

        def add(index: int, value: int) -> None:
            index += 1
            while index <= n:
                tree[index] += value
                index += index & -index

        def prefix(index: int) -> int:
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        def kth(rank: int) -> int:
            index = 0
            bit = 1 << (n.bit_length() - 1)
            while bit:
                candidate = index + bit
                if candidate <= n and tree[candidate] < rank:
                    index = candidate
                    rank -= tree[candidate]
                bit >>= 1
            return index

        for index in range(n):
            add(index, 1)
        order = sorted((value, index) for index, value in enumerate(nums))
        alive = n
        current_rank = 1
        answer = 0
        for _, index in order:
            target_rank = prefix(index + 1)
            if target_rank >= current_rank:
                answer += target_rank - current_rank + 1
            else:
                answer += alive - current_rank + target_rank + 1
            add(index, -1)
            alive -= 1
            if alive:
                current_rank = target_rank if target_rank <= alive else 1
        return answer


if __name__ == "__main__":
    assert Solution().countOperationsToEmptyArray([3, 4, -1]) == 5
    assert Solution().countOperationsToEmptyArray([1, 2, 3]) == 3
