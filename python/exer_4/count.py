def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5]
result_list = unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", result_list)
