# whileループの勉強

current_num = 1
prompt = '\nTell me somthing, and I will repeat it back to you:'
prompt += '\nYou have a maximum of four attempts, or Enter \'quit\' to end the program.\n'
message = ''
while current_num < 5 and message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f'NO.{current_num}:{message}')
    current_num += 1

flag = True
current_num = 0
while flag:
    message = input(prompt)
    if message == 'quit' or current_num == 5:
        flag = False
    else:
        print(f'NO.{current_num} is {message}.')

    current_num += 1

# break、continue文
current_num = 0
while True:
    current_num += 1
    city = input('Input quit to End:')
    if city == 'quit':
        break
    if current_num % 2 == 0:
        continue
    print(city)

# arrayとの連携
unconfirmed_users = ['ryan', 'admin', 'neo']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed.")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


unconfirmed_users = ['ryan', 'admin', 'neo', 'ryan', 'neo', 'nancy', 'terry', 'rose', 'ryan']

while 'ryan' in unconfirmed_users:
    unconfirmed_users.remove('ryan')

print(unconfirmed_users)

# dictionaryとの連携
responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat\'s your name?')
    response = input('While mountain would you like to limb someday?')

    responses[name] = response

    repeat = input('Would you like to let another person respond?(yes/no)')
    if repeat.lower() == 'no':
        polling_active = False

print('---------- Poll Results ----------')
for name, response in responses.items():
    print(f'{name} would like to climb {response}.')

