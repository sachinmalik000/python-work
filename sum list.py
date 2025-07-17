sum = [12, 13, 14, 13,12]

length = len(sum)

total = 0

avg = 0

for k in sum:

    total+=k

    avg+=(total/length)

print("Sum of given list ",total)

print("Avg", avg)   