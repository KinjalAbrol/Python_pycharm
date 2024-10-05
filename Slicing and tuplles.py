# slicing
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys)
print(piano_keys[2:5])
# slicing to a position to end of list.
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:])
# slicing to a position to starting to given position of list.
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[:5])
# also specify third number.this number sets the increment and get every other item then it skip the second one.
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:5:2])
# if i want to get hold of every number and want to skip the second one.
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[::2])# give list starting to end and skip every second number.
# negative one as increment.
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[::-1])# it reverse the list for us.starting from end to beginning.

# using tuples
piano_keys = ["a","b","c","d","e","f","g"]
piano_tuples = ("do","re","mi","fa","so","la","ti")
print(piano_tuples[2:5])

