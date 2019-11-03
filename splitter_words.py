my_string = 'ala ma kota'

my_string_splitted = my_string.split()

print(my_string_splitted)

for word in my_string_splitted:
    print(word)


for word in my_string_splitted:
    print(len(word), end=' ')

print()