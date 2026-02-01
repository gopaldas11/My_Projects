# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # This is dictionary comprehension.

def generate_phonatic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
            print("The word is not valid. Try again.")
            generate_phonatic()
    else:
        print(output_list)

generate_phonatic()





