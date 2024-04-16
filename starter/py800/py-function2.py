# 関数の勉強2

# オプションパラメータ
def make_pizza(*toppings):
    '''お客さんが注文したトッピングをリストアップする。'''
    if toppings:
        print('\nMaking a pizza with the following toppings:')
        for topping in toppings:
            print(f' - {topping}')
    else:
        print('\nYou must choose one topping at least.')

make_pizza()
make_pizza('mushrooms')
make_pizza('mushrooms', 'pepperoni', 'green peppers', 'extra cheese')

def make_freesize_pizza(size, *toppings):
    '''お客さんが注文したトッピングをリストアップする。'''
    if toppings:
        print('\nMaking a {size}-inch pizza with the following toppings:')
        for topping in toppings:
            print(f' - {topping}')
    else:
        print('\nYou must choose one topping at least.')

make_freesize_pizza(16)
make_freesize_pizza(16, 'mushrooms')
make_freesize_pizza(18, 'mushrooms', 'pepperoni', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    '''Dictionaryを作成し、ユーザ情報を格納する。'''
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('ryan', 'howard', location='Tokyo', age = 47)
print(user_profile)


