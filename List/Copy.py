# using copy lib

# import copy

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# original[0].append(99)

# print("Original:", original)
# print("Shallow Copy:", shallow)
# print("Deep Copy:", deep)



# using slicing 
original = [[1, 2], [3, 4]]

shallow_copy = original[:]

deep_copy = [inner[:] for inner in original]

original[0].append(99)

print("Original List:", original)
print("Shallow Copy :", shallow_copy)
print("Deep Copy    :", deep_copy)
