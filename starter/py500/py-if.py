# if関連操作

# 配列を定義する
sp500_company = ['bitjp', 'microsoft', 'apple', 'nvidia', 'intel', 'amd']

# 文字列の比較
for company in sp500_company:
    if company.lower() == 'bitjp':
        print(company.upper())
    elif company != 'microsoft':
        print(company)
    else:
        print(company.title())

# 数値の比較
for num in range(1,10):
    if num < 5:
        print(f'{num} is lower then 5')
        if num % 2 == 0 or num == 1:
            print(num)
    elif num >= 5 and num < 9:
        print(f'{num} is grater more then 5')
    else:
        print(num)

# 特定の値が存在の場合の判断（in/ not in）
if 'bitjp' in sp500_company:
    print(f'{sp500_company[sp500_company.index('bitjp')]} is nice.')
if 'abc' not in sp500_company:
    print('abc is not in s&p500.')

# ブーリアン式
myname = 'bitjp'
print(myname == 'bitjp')
print(myname != 'bitjp')

null_arr = []
if not null_arr:
    print('It\'s null array.')

sp500_company = ['bitjp', 'microsoft', 'apple', 'nvidia', 'intel', 'amd']

nice_sp500_company = ['bitjp', 'microsoft']

for company in sp500_company:
    if company in nice_sp500_company:
        print(f'{company} is nice!')
    else:
        print(f'{company} is low!')
