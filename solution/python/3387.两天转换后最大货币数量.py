from collections import defaultdict, deque


class Solution:
    def maxAmount(
        self,
        initialCurrency: str,
        pairs1: list[list[str]],
        rates1: list[float],
        pairs2: list[list[str]],
        rates2: list[float],
    ) -> float:
        def reachable(pairs, rates):
            graph = defaultdict(list)
            for (source, target), rate in zip(pairs, rates):
                graph[source].append((target, rate))
                graph[target].append((source, 1 / rate))
            amount = {initialCurrency: 1.0}
            queue = deque([initialCurrency])
            while queue:
                source = queue.popleft()
                for target, rate in graph[source]:
                    value = amount[source] * rate
                    if value > amount.get(target, 0.0) + 1e-12:
                        amount[target] = value
                        queue.append(target)
            return amount

        day_one = reachable(pairs1, rates1)
        day_two = defaultdict(list)
        for (source, target), rate in zip(pairs2, rates2):
            day_two[source].append((target, rate))
            day_two[target].append((source, 1 / rate))
        answer = 1.0
        for currency, amount in day_one.items():
            values = {currency: 1.0}
            queue = deque([currency])
            while queue:
                source = queue.popleft()
                for target, rate in day_two[source]:
                    value = values[source] * rate
                    if value > values.get(target, 0.0) + 1e-12:
                        values[target] = value
                        queue.append(target)
            answer = max(answer, amount * values.get(initialCurrency, 0.0))
        return answer


if __name__ == "__main__":
    assert (
        abs(
            Solution().maxAmount(
                "EUR",
                [["EUR", "USD"], ["USD", "JPY"]],
                [2.0, 3.0],
                [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]],
                [4.0, 5.0, 6.0],
            )
            - 720.0
        )
        < 1e-8
    )
    assert (
        abs(
            Solution().maxAmount(
                "NGN", [["NGN", "EUR"]], [9.0], [["NGN", "EUR"]], [6.0]
            )
            - 1.5
        )
        < 1e-8
    )
