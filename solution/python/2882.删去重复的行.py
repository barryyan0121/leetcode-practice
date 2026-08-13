import pandas as pd
from pandas.testing import assert_frame_equal


def dropDuplicateCustomers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])


class Solution:
    def dropDuplicateCustomers(self, customers: pd.DataFrame) -> pd.DataFrame:
        return dropDuplicateCustomers(customers)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "customer_id": [1, 2, 3, 4],
                    "name": ["Ella", "David", "Zachary", "Alice"],
                    "email": ["a@x.com", "b@x.com", "a@x.com", "c@x.com"],
                }
            ),
            pd.DataFrame(
                {
                    "customer_id": [1, 2, 4],
                    "name": ["Ella", "David", "Alice"],
                    "email": ["a@x.com", "b@x.com", "c@x.com"],
                },
                index=[0, 1, 3],
            ),
        )
    ]

    solver = Solution()
    for index, (customers, expected) in enumerate(test_cases):
        actual = solver.dropDuplicateCustomers(customers)
        assert_frame_equal(actual, expected), f"case {index} failed"
