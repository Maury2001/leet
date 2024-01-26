def max_area(arr):
    left, right = 0, len(arr) - 1
    max_volume =0
    
    while left < right:
        h= min(arr[left], arr[right])
        w = right- left
        #max_volume = max(max_volume, h * w)
        #optimized
        max_volume =max(max_volume, (min(arr[left], arr[right])* (right-left)))
        
        # if left is shorter move to right with possibility to find a taller line 
        if arr[left] < arr[right]:
            left += 1
            
        else:
            #condition false means right line is shorter /equal to left line so move pointer left to find taller one
            right -= 1
            
    return max_volume

lst = [1,8,6,2,5,4,8,3,7]
results = max_area(lst)
print(results)