
# Write a Python function to flatten a nested list.

nested_lst = [[2,3],[4,6],[7,8]]
flat =[]
for sublist in nested_lst:
    for item in sublist:
        flat.append(item)
print(flat)