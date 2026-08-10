from collections import Counter
from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums[:k])
        answer = [len(counts)]
        for right in range(k, len(nums)):
            counts[nums[right]] += 1
            counts[nums[right - k]] -= 1
            if counts[nums[right - k]] == 0:
                del counts[nums[right - k]]
            answer.append(len(counts))
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.distinctNumbers([1, 2, 3, 2, 2], 3) == [3, 2, 2]
    print("1852 passed")
