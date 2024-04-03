# 配列関連操作

# 配列を定義する
sp500_company = ['bitjp', 'microsoft', 'apple', 'nvidia', 'intel', 'amd']
print(sp500_company)

# 配列の1個目のエレメントを出力する
print(sp500_company[0])

# 配列の最後のエレメントを出力するには-1を指定する。
print(sp500_company[-1])
print(sp500_company[-2])

message = f'My company is {sp500_company[0].upper()}.'
print(message)
message = f'使っているシステムは{sp500_company[1].upper()}社の製品Windows11です。'
print(message)

# 配列のエレメントの値を変更する。
print(sp500_company)
print('Change [apple] to [redhat].')
sp500_company[2] = 'redhat'
print(sp500_company)

# 配列にエレメントを追加する。
print('Add [apple] to the end.')
sp500_company.append('apple')
print(sp500_company)

print('Add [google] before apple.')
sp500_company.insert(-1, 'google')
print(sp500_company)

# 配列からエレメントを取り除く
print('Delete [microsoft] from array.')
del sp500_company[1]
print(sp500_company)

print('Delete the end element, then print it.')
print(sp500_company.pop())
print(sp500_company)

print('Use pop method, delete the second company, then print it.')
print(sp500_company.pop(1))
print(sp500_company)

print('Use remove method, delete intel.')
company_name = 'intel'
sp500_company.remove(company_name)
print(f'{company_name} is be deleted.')
print(sp500_company)

# 配列のソート
print('Sort the companies.')
sp500_company.sort()
print(sp500_company)
print('Sort the companies with reverse.')
sp500_company.sort(reverse = True)
print(sp500_company)

# 一時的にソートを変更する
print(f'一時的にソートした配列：{sorted(sp500_company)}')
print(f'本来の配列：{sp500_company}')

print(f'一時的にソートした配列(逆順)：{sorted(sp500_company, reverse = True)}')
print(f'本来の配列：{sp500_company}')

# 配列を逆順にする。
sp500_company = ['bitjp', 'microsoft', 'apple', 'nvidia', 'intel', 'amd']
print(sp500_company)
print('配列を逆順にする。')
sp500_company.reverse()
print(sp500_company)

# 配列の長さ(エレメントの数)
print(f'配列の長さ(エレメントの数)は{len(sp500_company)}である。')

