filename = "py1000/programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love Java.\n")

with open(filename, "a") as file_object:
    file_object.write("It's append line!\n")