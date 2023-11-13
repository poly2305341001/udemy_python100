student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# with open("nato_phonetic_alphabet.csv") as data:
#     data_df = pandas.read_csv(data)
# df_comprehension = {row[0]:row[1] for (idx, row) in data_df.iterrows()}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (idx, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# # print(word)
# word_to_nato_code = [df_comprehension[alphabet] for alphabet in word if alphabet in df_comprehension]
# print(word_to_nato_code)
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)