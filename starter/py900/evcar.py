from car import Car

class EvCar(Car):
    """EV自動車"""
    def __init__(self, maker: str, model: str, year: int, battery_size: int = 75) -> None:
        super().__init__(maker, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

