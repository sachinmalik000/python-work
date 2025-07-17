
# 5. Find the Frequency of Elements in a List

def freq(lst):
    freq ={}
    for item in lst:
        freq[item]=freq.get(item,0) + 1
    return freq
lst = [12,10,15,11,10,12]

print(freq(lst)