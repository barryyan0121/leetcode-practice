class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        size = len(nums)
        next_greater = [size] * size
        stack = []
        for index in range(size - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[index]:
                stack.pop()
            next_greater[index] = stack[-1] if stack else size
            stack.append(index)

        levels = (size + 1).bit_length()
        destinations = [next_greater + [size]]
        sums = [
            [nums[index] * (next_greater[index] - index) for index in range(size)] + [0]
        ]
        for _ in range(1, levels):
            previous_destinations = destinations[-1]
            previous_sums = sums[-1]
            current_destinations = [size] * (size + 1)
            current_sums = [0] * (size + 1)
            for index in range(size):
                middle = previous_destinations[index]
                current_sums[index] = previous_sums[index]
                if middle < size:
                    current_destinations[index] = previous_destinations[middle]
                    current_sums[index] += previous_sums[middle]
            destinations.append(current_destinations)
            sums.append(current_sums)

        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def prefix_max_sum(left: int, right: int) -> int:
            current = left
            total = 0
            for level in range(levels - 1, -1, -1):
                if current == size:
                    break
                destination = destinations[level][current]
                if destination <= right:
                    total += sums[level][current]
                    current = destination
            if current <= right:
                total += nums[current] * (right - current + 1)
            return total

        answer = 0
        right = -1
        for left in range(size):
            right = max(right, left - 1)
            while right + 1 < size:
                candidate = right + 1
                cost = prefix_max_sum(left, candidate) - (
                    prefix[candidate + 1] - prefix[left]
                )
                if cost > k:
                    break
                right = candidate
            answer += right - left + 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (([6, 3, 1, 2, 4, 4], 7), 17),
        (([6, 3, 1, 3, 6], 4), 12),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().countNonDecreasingSubarrays(nums, k) == expected
