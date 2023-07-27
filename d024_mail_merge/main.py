#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    strings = starting_letter.readlines()


plain_names = []
for _ in names:
    name = _.strip("\n")
    plain_names.append(name)
# print(plain_names)

for name in plain_names:
    to_name = strings[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/to_{name}.txt", mode="w") as letter:
        letter.write(to_name)
    with open(f"./Output/ReadyToSend/to_{name}.txt", mode="a") as letter:
        for _ in strings[1:]:
            letter.write(_)



