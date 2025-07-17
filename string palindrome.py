str = input("Enter the input string")

left = 0

right =len(str)-1

while left < right:

    if str[left] == str[right]:

        left+=1
        right-=1

        

    else:

        print("Not Palindrome")

print("Palindrome")


    

    







