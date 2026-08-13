from typing import List


class Solution:
    def validCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        ans = []
        for c, b, a in zip(code, businessLine, isActive):
            if a and b in order and c and all(ch.isalnum() or ch == "_" for ch in c):
                ans.append((order[b], c))
        return [c for _, c in sorted(ans)]


if __name__ == "__main__":
    s = Solution()
    assert s.validCoupons(
        ["SAVE20", "", "PHARMA5", "SAVE@20"],
        ["restaurant", "grocery", "pharmacy", "restaurant"],
        [True, True, True, True],
    ) == ["PHARMA5", "SAVE20"]
    assert s.validCoupons(
        ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
        ["grocery", "electronics", "invalid"],
        [False, True, True],
    ) == ["ELECTRONICS_50"]
    print("3606 ok")
