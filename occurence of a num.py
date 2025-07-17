
# Find All  Indices of an Element

# Question:  Given a list and a value, find all indices of the value in the list.

def val_indices(lst, value):
    return[i for i, x in enumerate(lst) if x==value]
lst = [2,3,6,1,5,2]
value= 2
print(val_indices(lst,value))