import string

with open(file="text_files/p022_names.txt", mode="r") as file:
    names_str = file.read()
    names_str = names_str.replace('"', '')
    names_list = names_str.split(",")
    names_list.sort()

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
alphabet_dict = {alphabet_list[i]: i + 1 for i in range(len(alphabet_list))}

total_name_score = 0
for names in names_list:
    index = names_list.index(names) + 1
    alphabetical_value = 0
    for letter in names:
        alphabetical_value += alphabet_dict[letter]
    total_name_score += alphabetical_value * index
print(total_name_score)
