
str = 'hello priyanshi'

result = ''


for k in range(len(str)):

    if k % 2 == 0:

        result += str[k].upper()
    else:
        result += str[k].lower()
            
print(result)