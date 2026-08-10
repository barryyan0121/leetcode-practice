class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        target = list(num)
        for _ in range(k):
            pivot = len(target) - 2
            while target[pivot] >= target[pivot + 1]:
                pivot -= 1
            successor = len(target) - 1
            while target[successor] <= target[pivot]:
                successor -= 1
            target[pivot], target[successor] = target[successor], target[pivot]
            target[pivot + 1 :] = reversed(target[pivot + 1 :])
        current = list(num)
        swaps = 0
        for index, desired in enumerate(target):
            position = current.index(desired, index)
            while position > index:
                current[position], current[position - 1] = (
                    current[position - 1],
                    current[position],
                )
                position -= 1
                swaps += 1
        return swaps


if __name__ == "__main__":
    solution = Solution()
    assert solution.getMinSwaps("5489355142", 4) == 2
    print("1850 passed")
