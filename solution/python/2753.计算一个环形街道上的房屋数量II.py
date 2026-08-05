class Solution:
    def houseCount(self, street: "Street", k: int) -> int:
        while not street.isDoorOpen():
            street.moveRight()
        ans = 0
        for i in range(1, k + 1):
            street.moveRight()
            if street.isDoorOpen():
                ans = i
                street.closeDoor()
        return ans


if __name__ == "__main__":
    print("交互题，跳过本地模拟")
