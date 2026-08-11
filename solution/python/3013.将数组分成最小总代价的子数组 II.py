"""3013. 将数组分成最小总代价的子数组 II"""


class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        values = sorted(set(nums[1:]))
        size = len(values)
        counts = [0] * (size + 1)
        sums = [0] * (size + 1)

        def update(value: int, delta: int) -> None:
            index = __import__("bisect").bisect_left(values, value) + 1
            while index <= size:
                counts[index] += delta
                sums[index] += value * delta
                index += index & -index

        def smallest_total(amount: int) -> int:
            index = 0
            step = 1 << (size.bit_length() - 1)
            while step:
                candidate = index + step
                if candidate <= size and counts[index + step] < amount:
                    index = candidate
                    amount -= counts[candidate]
                step >>= 1
            total = 0
            pos = index
            while pos:
                total += sums[pos]
                pos -= pos & -pos
            return total + amount * values[index]

        amount = k - 2
        right = min(len(nums) - 1, 1 + dist)
        for index in range(2, right + 1):
            update(nums[index], 1)
        answer = float("inf")
        for first in range(1, len(nums) - k + 2):
            answer = min(answer, nums[0] + nums[first] + smallest_total(amount))
            update(nums[first + 1], -1)
            new_right = first + dist + 1
            if new_right < len(nums):
                update(nums[new_right], 1)
        return answer


if __name__ == "__main__":
    assert Solution().minimumCost([1, 3, 2, 6, 4, 2], 3, 3) == 5
    assert Solution().minimumCost([10, 1, 2, 2, 2, 1], 4, 3) == 15
    assert Solution().minimumCost([10, 8, 18, 9], 3, 1) == 36
