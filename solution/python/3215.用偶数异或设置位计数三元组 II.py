from collections import Counter
from typing import List


class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        cnt1 = Counter(x.bit_count() & 1 for x in a)
        cnt2 = Counter(x.bit_count() & 1 for x in b)
        cnt3 = Counter(x.bit_count() & 1 for x in c)
        ans = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if ((i + j + k) & 1) == 0:
                        ans += cnt1[i] * cnt2[j] * cnt3[k]
        return ans


if __name__ == "__main__":
    assert Solution().tripletCount([1, 2], [3], [4, 5]) == 2
    assert Solution().tripletCount([2, 1, 0], [8, 5], [1, 2, 3]) == 9
