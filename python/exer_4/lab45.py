def sort_words(input_string):
     words = input_string.split("-")
     sorted_words = sorted(words)
     sorted_sequence = "-".join(sorted_words)
     return sorted_sequence

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print("Sorted sequence:", sorted_sequence)
