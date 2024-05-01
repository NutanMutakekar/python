def extract_even_indices(input_list):
    even_indices_elements = []
    for i in range(len(input_list)):
        if i % 2 == 0:
            even_indices_elements.append(input_list[i])
    return even_indices_elements

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_indices_elements = extract_even_indices(input_list)
print("Elements at even indices:", even_indices_elements)

