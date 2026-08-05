class Solution:
    def houseCount(self, street: "Street", k: int) -> int:
        for _ in range(k):
            street.closeDoor()
            street.moveRight()
        street.openDoor()
        count = 1
        street.moveRight()
        while not street.isDoorOpen():
            count += 1
            street.moveRight()
        return count


if __name__ == "__main__":
    print("交互题，跳过本地模拟")
