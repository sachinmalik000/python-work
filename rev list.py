

ll = [2,4,6,8,10,12]

left = 0

right = len(ll)-1

while left < right:

        temp = ll[left]

        ll[left] = ll[right]

        ll[right] = temp   

        left+=1

        right= right-1

print("Rev List:", ll)
    