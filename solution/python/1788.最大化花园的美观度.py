from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(
        self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        flowers = sorted(min(value, target) for value in flowers)
        n = len(flowers)
        prefix = [0]
        for value in flowers:
            prefix.append(prefix[-1] + value)
        answer = 0
        for complete in range(n + 1):
            suffix_cost = target * complete - (prefix[n] - prefix[n - complete])
            if suffix_cost > newFlowers:
                continue
            remaining = newFlowers - suffix_cost
            count = n - complete
            if count == 0:
                answer = max(answer, n * full)
                continue
            low, high = 0, target - 1
            while low < high:
                mid = (low + high + 1) // 2
                index = bisect_right(flowers, mid, 0, count)
                cost = mid * index - prefix[index]
                if cost <= remaining:
                    low = mid
                else:
                    high = mid - 1
            answer = max(answer, complete * full + low * partial)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumBeauty([1, 3, 1, 1], 7, 6, 12, 1) == 14
    assert solution.maximumBeauty([2, 4, 5, 3], 10, 5, 2, 6) == 30
    print("1788 passed")
