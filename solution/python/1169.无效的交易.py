class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        parsed = [transaction.split(",") for transaction in transactions]
        invalid = set()
        for index, (name, time, amount, city) in enumerate(parsed):
            if int(amount) > 1000:
                invalid.add(index)
            for other_index, (other_name, other_time, _, other_city) in enumerate(
                parsed
            ):
                if (
                    name == other_name
                    and city != other_city
                    and abs(int(time) - int(other_time)) <= 60
                ):
                    invalid.add(index)
                    invalid.add(other_index)
        return [
            transaction
            for index, transaction in enumerate(transactions)
            if index in invalid
        ]


if __name__ == "__main__":
    test_cases = [
        (
            ["alice,20,800,mtv", "alice,50,100,beijing"],
            ["alice,20,800,mtv", "alice,50,100,beijing"],
        )
    ]
    for _, (transactions, expected) in enumerate(test_cases):
        assert Solution().invalidTransactions(transactions) == expected
