list_with_binary = [1, 2, 4, 8, 16, 32, 64, 128, 256]
list_with_numbers_to_sum = []


ask_number = input('What number you want to convert? ')
# ask_number = int(ask_number)

info_about_decimal_conv = 'To convert your number to decimal enter D'
info_about_binary_conv = 'To convert your number to binary enter B'

ask_about_type = input('Which metod do you want to use: ')

print(info_about_binary_conv)
print(info_about_decimal_conv)

list_with_digits_of_number = []

index_of_list_digits = 0

each_number = 0

index_of_list_with_binary = 0

if ask_about_type == 'D':
    for elem in ask_number:
        elem = int(elem)
        list_with_digits_of_number.append(elem)
        multiplied_number2 = list_with_digits_of_number[index_of_list_digits] * list_with_binary[index_of_list_with_binary]
        list_with_numbers_to_sum.append(multiplied_number2)
        index_of_list_with_binary += 1
        index_of_list_digits += 1


print(list_with_digits_of_number)
