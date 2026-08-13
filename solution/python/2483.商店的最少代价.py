"""2483. 商店的最少代价"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        best_penalty = penalty
        answer = 0
        for hour, customer in enumerate(customers):
            penalty += 1 if customer == "N" else -1
            if penalty < best_penalty:
                best_penalty = penalty
                answer = hour + 1
        return answer

if __name__ == "__main__":
    assert Solution().bestClosingTime("YYNY") == 2
