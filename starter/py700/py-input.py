# 入力関数の勉強

# ターミナルからユーザ入力を受ける
message = input('Tell me somthing, I will tell you!:\n')
print(f'Your Input is [{message}]')

# int()メソッド
age = input('Input your age(1-99):\n')
age = int(age)
if age <= 99 and age > 0:
  print(f'Your age is {age} years old.')
else:
  print('Input error!')

# あまり演算子%
print(f'7 % 3 = {7 % 3}')