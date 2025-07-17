
ltm = [56,74,89,43,20]

total = 0

lmt = []

for k in ltm:

    kt = str(k)

    for ktm in kt:

        kts = int(ktm)

        total+=kts
        
    lmt.append(total)

print("Total sum of digits in the list",total)

print("List after summing up all individually",lmt)