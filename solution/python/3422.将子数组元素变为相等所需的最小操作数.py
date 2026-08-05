import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        low: list[tuple[int, int]] = []
        high: list[tuple[int, int]] = []
        side = [0] * len(nums)
        low_sum = high_sum = low_count = high_count = 0

        def prune() -> None:
            while low and side[low[0][1]] != 1:
                heapq.heappop(low)
            while high and side[high[0][1]] != 2:
                heapq.heappop(high)

        def balance() -> None:
            nonlocal low_count, high_count, low_sum, high_sum
            prune()
            while low_count < high_count:
                value, index = heapq.heappop(high)
                side[index] = 1
                heapq.heappush(low, (-value, index))
                high_count -= 1
                low_count += 1
                high_sum -= value
                low_sum += value
                prune()
            while low_count > high_count + 1:
                neg_value, index = heapq.heappop(low)
                value = -neg_value
                side[index] = 2
                heapq.heappush(high, (value, index))
                low_count -= 1
                high_count += 1
                low_sum -= value
                high_sum += value
                prune()

        def add(index: int) -> None:
            nonlocal low_count, high_count, low_sum, high_sum
            prune()
            value = nums[index]
            if not low or value <= -low[0][0]:
                heapq.heappush(low, (-value, index))
                side[index] = 1
                low_count += 1
                low_sum += value
            else:
                heapq.heappush(high, (value, index))
                side[index] = 2
                high_count += 1
                high_sum += value
            balance()

        def remove(index: int) -> None:
            nonlocal low_count, high_count, low_sum, high_sum
            value = nums[index]
            if side[index] == 1:
                low_count -= 1
                low_sum -= value
            else:
                high_count -= 1
                high_sum -= value
            side[index] = 0
            balance()

        answer = float("inf")
        for right, _ in enumerate(nums):
            add(right)
            if right >= k - 1:
                prune()
                median = -low[0][0]
                answer = min(
                    answer,
                    median * low_count - low_sum + high_sum - median * high_count,
                )
                remove(right - k + 1)
        return int(answer)


if __name__ == "__main__":
    test_cases = [
        (([4, -3, 2, 1, -4, 6], 3), 5),
        (([-2, -2, 3, 1, 4], 2), 0),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums, k) == expected
