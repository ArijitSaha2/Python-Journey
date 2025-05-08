marks = {
       'Andy': 20,
       'Angelina': 19,
       'Annie': 15,
       0 : 'Harry'
}
# print(marks.items()) # .items() is a method in Python that returns a view object displaying a list of key-value pairs from a dictionary, where each pair is represented as a tuple.

# print(marks.keys()) # .keys() is a method in python that returns only keys.

# print(marks.values())# .values() is a method in python that returns only values.

# marks.update({'Andy': 18, 'Jessika':30}) # .update() can modify existing values or add new key+values

# This method looks similar but are different from each other :

print(marks.get('Andy1')) # This will give us none as its not there
print(marks['Andy1']) # This will print an error as the specied key doesn't exist

# marks.pop('Annie') # Removes the specified pair(Key-value) from the list

# a = marks.popitem() # Removes the last inserted key-value pair from dictionary and returns it as a tuple(key-value). It will always return the tuple (key, value), whether or not a variable is assigned to it.
print(marks)
# print(a)