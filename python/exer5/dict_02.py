# exercize 4 2nd question

emails = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com",
    "David": "david@example.com"
}

# i. Add Initial Items
emails["Eve"] = "eve@example.com"

# ii. Sort the specified keys or values
sorted_emails_keys = sorted(emails.keys())
sorted_emails_values = sorted(emails.values())

# iii. Delete an element from the dictionary
del emails["David"]

# iv. Print the items presents in the dictionary as a sequence of (key, value) tuples
items_as_tuples = list(emails.items())

# v. Count the frequency of elements
from collections import Counter
frequency = Counter(emails.values())

# vi. Count the key: value pair from the dictionary
num_items = len(emails)

# vii. Get all the keys and values of the dictionary in a list form
all_keys = list(emails.keys())
all_values = list(emails.values())

# viii. Get the specified keys and values from the dictionary
specified_keys = ["Alice", "Bob"]
specified_values = [emails[key] for key in specified_keys if key in emails]

# ix. Add an element to the last in the dictionary
emails["Zoe"] = "zoe@example.com"

# x. Update the element of the dictionary
emails["Alice"] = "new_alice@example.com"

# xi. Create a shallow copy of a dictionary
emails_copy = emails.copy()

# xii. Removes and returns the last key: value pair from the dictionary
last_key_value_pair = emails.popitem()

# xiii. Delete all the key: value pairs from the dictionary
emails.clear()

# Display the results
print("Sorted keys:", sorted_emails_keys)
print("Sorted values:", sorted_emails_values)
print("Items as tuples:", items_as_tuples)
print("Frequency of values:", frequency)
print("Number of items:", num_items)
print("All keys:", all_keys)
print("All values:", all_values)
print("Specified keys:", specified_keys)
print("Specified values:", specified_values)
print("Emails dictionary after operations:", emails)
print("Shallow copy of emails dictionary:", emails_copy)
print("Last key-value pair removed:", last_key_value_pair)
