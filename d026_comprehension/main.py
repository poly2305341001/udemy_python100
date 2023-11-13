with open('file1.txt') as file1:
  file1_list = file1.readlines()
with open('file2.txt') as file2:
  file2_list = file2.readlines()

int_file1_list = [int(str.strip()) for str in file1_list]
int_file2_list = [int(str.strip()) for str in file2_list]

result = [num for num in int_file1_list if num in int_file2_list]

# Write your code above 👆

print(result)


