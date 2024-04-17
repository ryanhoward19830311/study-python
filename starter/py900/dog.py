class Dog:
    """犬クラスの定義
    """

    def __init__(self, name, age) -> None:
        """初期化属性"""
        self.name = name
        self.age = age

    def sit(self):
        """お座り"""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """転がる"""
        print(f'{self.name} rolled over!')

    def tell_me_age(self):
        """年齢判明"""
        print(f'{self.name} is {self.age} yrs.')