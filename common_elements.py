first_list = [1, 2, 3, 5, 'test', 'piwo', 0, 11, 'o']
second_list = [1, 6, 3, 7, 0, 'test']

common_elements = []

for elem in first_list:
    if elem in second_list:
        common_elements.append(elem)
    print(common_elements)

print()
print('list of common elements: ', common_elements)
print('list of common elements: {} '.format(common_elements))

print(f'list of common elements: {common_elements} ')
