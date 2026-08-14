from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        index_sum = [0]
        count_sum = [0]
        for i, value in enumerate(nums):
            index_sum.append(index_sum[-1] + value * i)
            count_sum.append(count_sum[-1] + value)

        answer = float("inf")
        for center in range(n):
            nearby = nums[center]
            if center:
                nearby += nums[center - 1]
            if center + 1 < n:
                nearby += nums[center + 1]
            if nearby + maxChanges >= k:
                if k <= nearby:
                    answer = min(answer, k - nums[center])
                else:
                    answer = min(answer, 2 * k - nearby - nums[center])
                continue

            left, right = 0, n
            while left <= right:
                radius = (left + right) // 2
                start = max(center - radius, 0)
                end = min(center + radius, n - 1)
                if count_sum[end + 1] - count_sum[start] >= k - maxChanges:
                    right = radius - 1
                else:
                    left = radius + 1
            start = max(center - left, 0)
            end = min(center + left, n - 1)
            if count_sum[end + 1] - count_sum[start] > k - maxChanges:
                start += 1
            left_count = count_sum[center + 1] - count_sum[start]
            right_count = count_sum[end + 1] - count_sum[center + 1]
            answer = min(
                answer,
                index_sum[end + 1]
                - index_sum[center + 1]
                - center * right_count
                + center * left_count
                - (index_sum[center + 1] - index_sum[start])
                + 2 * maxChanges,
            )
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.minimumMoves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1) == 3
    assert s.minimumMoves([0, 0, 0, 0], 2, 3) == 4
    assert s.minimumMoves([1, 0, 0, 0, 0, 1], 2, 0) == 5
    print("3086 ok")
