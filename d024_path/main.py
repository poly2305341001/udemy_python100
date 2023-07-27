# TODO: read file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# TODO: write file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text")

with open("my_file.txt", mode="a") as file:
    # file.write("New text")
    file.write("\nNew text")

# TODO: make file
with open("new_file.txt", mode="w") as file:
    file.write("make this file")
    file.write("\nNew text")

