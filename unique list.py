
# ✅ Steps to Remove Duplicates from a List (Without Using Any Method)
# Start with a list that contains some duplicate values.

# Prepare an empty list to store only the unique values.

# Go through each item in the original list one by one.

# For each item, check if it is already in the new list.

# If the item is not in the new list, add it to the new list.

# If the item is already in the new list, skip it.

# Continue this process until all items in the original list have been checked.

# The final list now contains only unique elements, with duplicates removed.

lst = [3,5,4,7,4,2,3,4]

emp_list = []

for item in lst:

    if item not in emp_list:

        emp_list.append(item)
print(emp_list)