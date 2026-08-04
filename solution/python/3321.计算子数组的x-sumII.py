import heapq


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        frequencies = {}
        groups = {}
        versions = {}
        small = []
        large = []
        small_count = large_count = 0
        large_sum = 0

        def push_small(value: int) -> None:
            heapq.heappush(small, (-frequencies[value], -value, value, versions[value]))

        def push_large(value: int) -> None:
            heapq.heappush(large, (frequencies[value], value, versions[value]))

        def clean_small() -> None:
            while small:
                _, _, value, version = small[0]
                if groups.get(value) != "small" or versions[value] != version:
                    heapq.heappop(small)
                else:
                    break

        def clean_large() -> None:
            while large:
                _, value, version = large[0]
                if groups.get(value) != "large" or versions[value] != version:
                    heapq.heappop(large)
                else:
                    break

        def rebalance() -> None:
            nonlocal small_count, large_count, large_sum
            desired = min(x, len(frequencies))
            while large_count < desired:
                clean_small()
                _, _, value, _ = heapq.heappop(small)
                groups[value] = "large"
                versions[value] += 1
                large_count += 1
                small_count -= 1
                large_sum += frequencies[value] * value
                push_large(value)
            while large_count > desired:
                clean_large()
                _, value, _ = heapq.heappop(large)
                groups[value] = "small"
                versions[value] += 1
                large_count -= 1
                small_count += 1
                large_sum -= frequencies[value] * value
                push_small(value)
            while True:
                clean_small()
                clean_large()
                if not small or not large:
                    break
                best_small = (-small[0][0], -small[0][1])
                weakest_large = (large[0][0], large[0][1])
                if best_small <= weakest_large:
                    break
                _, _, small_value, _ = heapq.heappop(small)
                _, large_value, _ = heapq.heappop(large)
                groups[small_value] = "large"
                groups[large_value] = "small"
                versions[small_value] += 1
                versions[large_value] += 1
                large_sum += frequencies[small_value] * small_value
                large_sum -= frequencies[large_value] * large_value
                push_large(small_value)
                push_small(large_value)

        def change(value: int, delta: int) -> None:
            nonlocal small_count, large_count, large_sum
            if value not in frequencies:
                frequencies[value] = delta
                versions[value] = 1
                groups[value] = "small"
                small_count += 1
                push_small(value)
                rebalance()
                return
            group = groups[value]
            old_frequency = frequencies[value]
            new_frequency = old_frequency + delta
            versions[value] += 1
            if group == "large":
                large_sum += delta * value
            if new_frequency == 0:
                del frequencies[value]
                groups[value] = "gone"
                if group == "large":
                    large_count -= 1
                else:
                    small_count -= 1
            else:
                frequencies[value] = new_frequency
                if group == "large":
                    push_large(value)
                else:
                    push_small(value)
            rebalance()

        for value in nums[:k]:
            change(value, 1)
        answer = [large_sum]
        for index in range(k, len(nums)):
            change(nums[index - k], -1)
            change(nums[index], 1)
            answer.append(large_sum)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 1, 2, 2, 3, 4, 2, 3], 6, 2), [6, 10, 12]),
        (([3, 8, 7, 8, 7, 5], 2, 2), [11, 15, 15, 15, 12]),
    ]
    for _, ((nums, k, x), expected) in enumerate(test_cases):
        assert Solution().findXSum(nums, k, x) == expected
