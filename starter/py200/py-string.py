# 文字列関連操作

name = 'ryan howard'

# 単語の最初の文字を大文字に変更
print(name.title())

# 文字列を大文字に変更
print(name.upper())

# 文字列を小文字に変更
print(name.lower())

# 文字列変数
first_name = 'ryan'
last_name = 'howard'
message = f'My name is {first_name.title()} {last_name}.'
print(f'{message}Now you see me.')

# 3.6以前のバージョンでfは対応していないため、上記を実現するのはformatメソッドを使う
message = 'My name is {} {}.'.format(first_name.title(), last_name.title())
print(f'{message}Now you see me again.')

# タブ
print('1.1 My python')
print('\t1.1.1 first program')
print('\t1.1.2 second program')

# 改行
print('Let me change line!\nIt\'s new line...')

# 空白を取り除く
str = " center "
print(f'left{str.strip()}right')
print(f'left{str.lstrip()}right')
print(f'left{str.rstrip()}right')
str = str.strip()
print(f'left{str}right')
