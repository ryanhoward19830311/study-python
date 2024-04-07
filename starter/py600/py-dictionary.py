# Dictionaryの使用

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(f'alien_0: {alien_0}')

# key, value pairの追加
alien_0['x_pos'] = 0
alien_0['y_pos'] = 23

print(f'alien_0 now: {alien_0}')

alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x_pos'] = 23
alien_1['y_pos'] = 23

print(f'alien_1: {alien_1}')

# key, value pairの削除
del alien_1['color']
print(f'alien_1 now: {alien_1}')

# マルチ行でDictionaryを定義する。
favorite_language = {
  'jordan': 'python',
  'harden': 'c',
  'curry': 'java',
  'howard': 'typescript',
  'durant': 'java',
}

language = favorite_language['curry'].title()
vip_person = ['jordan', 'harden', 'wade']
print(f'Curry\'s favorite language is {language}.')

# get()メソッドの使用
print(favorite_language.get('james')) # return None
print(favorite_language.get('james', 'No james data!'))

# iteration
for name, lang in favorite_language.items():
    print(f'{name.title()}\'s favorite language is {lang.title()}.\n')

for name in favorite_language.keys():
    print(f'\nNow we get {name.title()}\'s data.')

    if name in vip_person:
        print(f'{name.title()} is vip!')

# keys()メソッド, values()メソッドでそれぞれのリストを戻す
for name in vip_person:
    if name not in favorite_language.keys():
        print(f'\nWe must get {name.title()}\'s data!')

# sorted()メソッドで並び替え
for name in sorted(favorite_language.keys()):
    print(f'{name.title()}')

print(f'\n')
# set()メソッドで重複を取り除く
for language in set(favorite_language.values()):
    print(f'{language.title()}')

# セットの定義
languages = {'python', 'C', 'java', 'typescript', 'C#'}
print(languages)

# ネストされたオブジェクト Nested Object
print('\n\nNested Object の練習!\n')
tank1 = {'color': 'green', 'point': 5, 'x_pos': 0, 'y_pos': 0}
tank2 = {'color': 'green', 'point': 5, 'x_pos': 30, 'y_pos': 0}
tank3 = {'color': 'green', 'point': 5, 'x_pos': 60, 'y_pos': 0}

tanks = []
tanks.append(tank1)
tanks.append(tank2)
tanks.append(tank3)

for tank in tanks:
    print(tank)