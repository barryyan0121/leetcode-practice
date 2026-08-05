class Solution:
    def findMaximumElegance(self, items: list[list[int]], k: int) -> int:
        items.sort(reverse=True)
        chosen = set()
        duplicates = []
        score = 0
        for profit, category in items[:k]:
            score += profit
            if category in chosen:
                duplicates.append(profit)
            chosen.add(category)
        ans = score + len(chosen) * len(chosen)
        for profit, category in items[k:]:
            if category in chosen or not duplicates:
                continue
            score += profit - duplicates.pop()
            chosen.add(category)
            ans = max(ans, score + len(chosen) * len(chosen))
        return ans


if __name__ == "__main__":
    assert Solution().findMaximumElegance([[3, 1], [5, 1], [10, 2]], 2) == 19
