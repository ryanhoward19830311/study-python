
num = input("Input a number:")
try:
    print(5/int(num))
except ZeroDivisionError:
    print("0は除数として使えません。")

while True:
    first_number = input("\nFirst number:")
    if first_number == "q":
        break
    second_number = input("\nSecond number:")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("0は除数として使えません。")
    else:
        print(answer)


filename = "py1000/test.txt"
try:
    with open(filename, encoding="utf-8") as fileobj:
        contents = fileobj.read()
except FileNotFoundError:
    print("File not found!")




filename = "py1000/learn_language.txt"
try:
    with open(filename, encoding="utf-8") as fileobj:
        contents = fileobj.read()
        print(contents.split())
except FileNotFoundError:
    print("File not found!")


def count_words(p_filename):
    try:
        with open(p_filename) as fo:
            cot = fo.read().strip()
    except FileNotFoundError:
        pass
    else:
        print(f"{p_filename}: {len(cot.split())}")

filenames = ["py1000/learn_language.txt", "py1000/pi_digits.txt","py1000/programming.txt", "py1000/test.txt"]
for filename in filenames:
    count_words(filename)
