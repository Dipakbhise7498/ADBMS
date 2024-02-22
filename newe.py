mydict = {0 : 'Apple', 1 : 'Orange'}
x = all(mydict)
print(x)

# Returns False because the first key is false.
# For dictionaries the all() function checks the keys, not the values.