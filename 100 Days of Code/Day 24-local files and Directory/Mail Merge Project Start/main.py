# with open("../../my 24 day test.txt") as file:
#     contents = file.read()
#     print(contents)
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter = letters_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, strip_name)
        with open(f"./Output/ReadyToSend/latter_for_{strip_name}.txt", "w") as latter_file:
            latter_file.write(new_letter)
