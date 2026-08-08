from threading import Lock


class TrafficLight:
    def __init__(self):
        self.green_road = 1
        self.lock = Lock()

    def carArrived(
        self, carId: int, roadId: int, direction: int, turnGreen, crossCar
    ) -> None:
        with self.lock:
            if roadId != self.green_road:
                turnGreen()
                self.green_road = roadId
            crossCar()


if __name__ == "__main__":
    test_cases = [(2, ["green", "cross"])]
    for _, (road_id, expected) in enumerate(test_cases):
        calls = []
        TrafficLight().carArrived(
            1, road_id, 1, lambda: calls.append("green"), lambda: calls.append("cross")
        )
        assert calls == expected
