# 数型

# 整数
print(3 + 2)
i = 0
print(i + 1)
i = (i + 1) * 2
print(i)
print(i/2)
print(i/3)

# 小数
print(0.4 + 1.2)
# 精度問題が起きる式
print(0.1 + 0.2)

# float型があれば、結果は必ずfloat型
print(2.0 + 1)

# 大きい数値の場合、アンダーバーで分割表示できる。
universe_age = 14_000_000_000
print(universe_age)

# 複数の変数へ同時に値を設定する。
x, y, z = 1, 2, 0
print(f'x: {x}; y: {y}; z: {z};')

# 定数の定義（Pythonは定数型がないため、定数は大文字の変数名として、変数と区別する）
MAX_COUNT = 10000
print(MAX_COUNT)
MAX_COUNT = 10001
print(MAX_COUNT)