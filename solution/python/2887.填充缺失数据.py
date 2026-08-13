import pandas as pd
from pandas.testing import assert_frame_equal


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products


class Solution:
    def fillMissingValues(self, products: pd.DataFrame) -> pd.DataFrame:
        return fillMissingValues(products)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame({"name": ["A", "B", "C"], "quantity": [1.0, None, 3.0]}),
            pd.DataFrame({"name": ["A", "B", "C"], "quantity": [1.0, 0.0, 3.0]}),
        )
    ]

    solver = Solution()
    for index, (products, expected) in enumerate(test_cases):
        actual = solver.fillMissingValues(products.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
