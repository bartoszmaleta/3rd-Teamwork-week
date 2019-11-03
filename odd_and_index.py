my_string = 'ala ma kota'
list_wiht_letter_from_my_string = []

for index in range(len(my_string)):
    if index % 2 != 0:
        print(my_string[index])

        list_wiht_letter_from_my_string.append(my_string[index])

print(list_wiht_letter_from_my_string)