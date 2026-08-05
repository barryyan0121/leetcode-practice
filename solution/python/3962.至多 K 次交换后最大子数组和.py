"""3962. 至多 K 次交换后最大子数组和"""


class Fenwick:
    def __init__(self, size: int):
        self.count = [0] * (size + 1)
        self.total = [0] * (size + 1)

    def add(self, index: int, count: int, value: int) -> None:
        while index < len(self.count):
            self.count[index] += count
            self.total[index] += count * value
            index += index & -index

    def prefix(self, index: int) -> tuple[int, int]:
        count = total = 0
        while index:
            count += self.count[index]
            total += self.total[index]
            index -= index & -index
        return count, total

    def kth_sum(self, amount: int, values: list[int]) -> int:
        if amount <= 0:
            return 0
        position = 0
        count = total = 0
        step = 1 << (len(self.count).bit_length() - 1)
        while step:
            candidate = position + step
            if candidate < len(self.count) and count + self.count[candidate] <= amount:
                position = candidate
                count += self.count[candidate]
                total += self.total[candidate]
            step >>= 1
        if count == amount:
            return total
        return total + (amount - count) * values[position]


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        values = sorted(set(nums))
        ranks = {value: index + 1 for index, value in enumerate(values)}
        size = len(values)
        answer = -(10**30)
        for left in range(len(nums)):
            inside = Fenwick(size)
            outside = Fenwick(size)
            for value in nums:
                outside.add(ranks[value], 1, value)
            base = 0
            for right in range(left, len(nums)):
                value = nums[right]
                rank = ranks[value]
                inside.add(rank, 1, value)
                outside.add(rank, -1, value)
                length = right - left + 1
                limit = min(k, length, len(nums) - length)
                base += value

                def gain(swaps: int) -> int:
                    smallest = inside.kth_sum(swaps, values)
                    outside_count, outside_total = outside.prefix(size)
                    largest = outside_total - outside.kth_sum(
                        outside_count - swaps, values
                    )
                    return largest - smallest

                low, high = 0, limit + 1
                while low + 1 < high:
                    middle = (low + high) // 2
                    if gain(middle) > 0:
                        low = middle
                    else:
                        high = middle
                answer = max(answer, base + gain(low))
        return answer


if __name__ == "__main__":
    test_cases = [(([1, -1, 0, 2], 1), 3), (([4, 3, 2, 4], 2), 13), (([-1, -2], 0), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxSum(*args) == expected
