with open('py1000\pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open('py1000\pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

filepath = "D:\study\study-python\starter\py1000\pi_digits.txt"
with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string: str = ""
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(pi_string[:20])

birthday = input("Enter your birthday, in thr form md:")
if birthday in pi_string:
    print("Your birthday is in pi!")
else:
    print("I'm sorry.")

with open("D:/study/study-python/starter/py1000/learn_language.txt") as file_object:
    for line in file_object.readlines():
        print(line.strip().replace("Python", "Java"))
