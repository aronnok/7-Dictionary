
import operator

# Main Dictionary
dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary: ", dictionary)

# Update Dictionary To Ascending Order
sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
print("Dictionary in ascending order: ", sorted_dictionary)

# Update Dictionary To Descending Order
sorted_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))
print("Dictionary in descending order: ", sorted_dictionary)


