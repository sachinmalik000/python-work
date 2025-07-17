
str = input("Enter the input string")

lt = list(str)

left = 0

right =len(str)-1

while left < right:

        temp = lt[left]

        lt[left] = lt[right]

        lt[right] = temp        

        left+=1
        
        right-=1

reversed_string = ''.join(lt)

print("REV STR", reversed_string)


    

    







