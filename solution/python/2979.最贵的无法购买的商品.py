class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        reachable = [False] * (primeOne * primeTwo)
        reachable[0] = True
        for value in range(primeOne * primeTwo):
            if reachable[value]:
                if value + primeOne < len(reachable):
                    reachable[value + primeOne] = True
                if value + primeTwo < len(reachable):
                    reachable[value + primeTwo] = True
        return max(value for value, possible in enumerate(reachable) if not possible)


if __name__ == "__main__":
    assert Solution().mostExpensiveItem(2, 5) == 3
    assert Solution().mostExpensiveItem(5, 7) == 23
