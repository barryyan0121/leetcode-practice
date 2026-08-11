import heapq


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        vermolunea = n
        limit = 10 ** len(str(n))
        prime = [True] * limit
        prime[0] = prime[1] = False
        for number in range(2, int(limit**0.5) + 1):
            if prime[number]:
                prime[number * number :: number] = [False] * len(prime[number * number :: number])
        if prime[n] or prime[m]:
            return -1
        distance = {vermolunea: vermolunea}
        heap = [(vermolunea, vermolunea)]
        while heap:
            cost, number = heapq.heappop(heap)
            if cost != distance[number]:
                continue
            if number == m:
                return cost
            digits = list(str(number))
            for pos in range(len(digits)):
                old = digits[pos]
                for digit in (str(int(old) - 1), str(int(old) + 1)):
                    if digit not in "0123456789" or (pos == 0 and digit == "0"):
                        continue
                    digits[pos] = digit
                    next_number = int("".join(digits))
                    if not prime[next_number]:
                        next_cost = cost + next_number
                        if next_cost < distance.get(next_number, float("inf")):
                            distance[next_number] = next_cost
                            heapq.heappush(heap, (next_cost, next_number))
                digits[pos] = old
        return -1


if __name__ == "__main__":
    test_cases = [
        ((10, 12), 85),
        ((4, 8), -1),
        ((6, 2), -1),
    ]
    for _, ((n, m), expected) in enumerate(test_cases):
        assert Solution().minOperations(n, m) == expected
