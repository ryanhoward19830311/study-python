# ループ関連操作

# 配列を定義する
sp500_company = ['bitjp', 'microsoft', 'apple', 'nvidia', 'intel', 'amd']

# ループして、出力
for company in sp500_company:
    print(f'{company.title()} is S&P500 company.')
    print(f'The stock for {company.upper()}  is valuable.\n')

for num in range(2, 8):
    print(num)

numbers = list(range(1, 10, 2))
print(numbers)

# 1~10の平方のリストを作成する。
squares = []
for val in range(1, 11):
    squares.append(val ** 2)

print(squares)

# 最大値、最小値とサマリ
print(f'squaresの最大値は: {max(squares)}')
print(f'squaresの最小値は: {min(squares)}')
print(f'squaresのサマリは: {sum(squares)}')

# 配列の一部を切り出す(例：sp500_company[2:4] => ['apple', 'nvidia'])

print(sp500_company[2:4])
print(sp500_company[:4])
print(sp500_company[2:])

# 最後の三社を出力する
print(sp500_company[-3:])

for company in sp500_company[-4:]:
    print(f'{company.title()} is S&P500 company.')
    print(f'The stock for {company.upper()}  is valuable.\n')

# 配列をコピーする
new_sp500_companies = sp500_company[:]
print(new_sp500_companies)

new_sp500_companies.append('sony')

print(sp500_company)
print(new_sp500_companies)

mybox = [['pc', 'ipad', 'laptop'],['pen', 'pencil', 'scissors' 'eraser']]

i = 0
for drawer in mybox:
    i = i + 1
    print(f'This the No.{i} drawer.')
    for item in drawer:
        print(f'No.{i} drawer has {item.title()}.')
    print('\n', end = '')

# 配列定数
pointer = (200, 30)
# pointer[0] = 390の書き方はRuntimeErrorが起こされる。
print(pointer)
pointer = (250, 30)
print(pointer)

print('Program end!')