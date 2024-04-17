class Car:
    """車クラス"""
    def __init__(self, maker: str, model: str, year: int) -> None:
        """初期化"""
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self) -> str:
        """ディスクリプションをプリント"""
        long_name = f"{self.year} {self.maker} {self.model}"
        return long_name.title()

    def read_odometer(self) -> None:
        """メーターを表示する"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles: int) -> None:
        """メーターを更新する。"""
        if miles < self.odometer_reading:
            print(f"You can't roll back an odometer!")
        else:
            self.odometer_reading = miles

    def increament_odometer(self, miles: int) -> None:
        """メーターを増える。"""
        if miles < 0:
            print(f"You can't roll back an odometer!")
        else:
            self.odometer_reading += miles