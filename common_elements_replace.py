first_list = [1, 2, 3, 5, 'test', 'piwo', 0, 11, 'o']
second_list = [1, 6, 3, 7, 0, 'test']

common_elements = []

for elem in first_list:
    if elem in second_list:
        common_elements.append(elem)
    print(common_elements)

print()

print(f'list of common elements: {common_elements} ')

# 1 -> 1
# 2 -> 3
# 3 -> test
# 4 ->'
print('------------------------')

for i in range(len(common_elements)):
    print(f'{i+1} -> {common_elements}')

print()