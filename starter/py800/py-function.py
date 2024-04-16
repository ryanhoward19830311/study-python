# 関数の勉強


def greet_user():
    '''簡単な挨拶をする'''
    print('おはようございます。')

def greet_user2(username):
    '''簡単な挨拶をする'''
    print(f'おはようございます。{username}')

greet_user()

greet_user2('林様！')


def describe_pet(animal_type, pet_name='Alex'):
    '''ペットの情報を表示する'''
    print(f'\n私は{animal_type}を持っている。')
    print(f'\n名前は{pet_name}です。')

describe_pet('犬', 'カカシ')

describe_pet('猫', 'アーサー')

describe_pet(animal_type='金魚',  pet_name='はなこ')

def get_format_name(first_name, last_name, middle_name=''):
    '''フルネームを戻す'''
    if (middle_name == ''):
        full_name = f'{first_name}　{last_name}'
    else:
        full_name = f'{first_name}　{middle_name}　{last_name}'
    return full_name.title()

full_name=get_format_name(first_name='林', last_name='太郎')

print(f'フルネームは「{full_name}」です。')

full_name=get_format_name(first_name='Ryan', last_name='Howard', middle_name='Disco')

print(f'フルネームは「{full_name}」です。')

def build_person(first_name, last_name, age=None):
    person={
        'first_name': first_name.title(),
        'last_name': last_name.title()
    }
    if age:
        person['age'] = age
    return person

user1 = build_person('joe', 'johnson')
user2 = build_person('ryan', 'howard', 41)
print([user1, user2])

while True:
    print('\nPlease tell me your name:')
    print('(enter \'q\' at any time to quit)')

    f_name = input('first name:')
    if f_name == 'q':
        break

    l_name = input('last name:')
    if l_name == 'q':
        break

    full_name = get_format_name(first_name=f_name, last_name=l_name)
    print(f'Hello!{full_name}!')


def process_list(names):
    for name in names:
        print(f'Hello,!{name.title()}')

users=['ryan', 'john', 'sandy', 'rose']
process_list(users)

def print_models(unprint_designs, complated_models):
    while unprint_designs:
        current_design = unprint_designs.pop()
        print(f'Printing model: {current_design}')
        complated_models.append(current_design)

def show_complated_models(complated_models):
    print('\nThe following models have been printed:')
    for complated_model in complated_models:
        print(complated_model)

unprinted_models = ['phone case', 'car', 'robot ai']
complated_modesl = []

print_models(unprint_designs=unprinted_models, complated_models=complated_modesl)
show_complated_models(complated_models=complated_modesl)
print(f'unprinted_models:{unprinted_models}')

unprinted_models = ['phone case', 'car', 'robot ai']
complated_modesl = []

# リストの内容を変更させないため、リストのコピーを渡す。unprinted_models[:]
print_models(unprint_designs=unprinted_models[:], complated_models=complated_modesl)
show_complated_models(complated_models=complated_modesl)
print(f'unprinted_models:{unprinted_models}')