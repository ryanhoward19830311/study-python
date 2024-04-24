from name_function import get_format_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("\nPlease give me a last name: ")
    if last == "q":
        break

    formatted_name = get_format_name(first=first, last=last)
    print(f"\tNeatly formatted name: {formatted_name}.")

