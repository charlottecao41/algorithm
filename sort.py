array = [1,2,5,7,3,3,10]

def merge_sort(array):
    if len(array)<=1:
        return array
        
    else:
        left=array[:len(array)//2]
        right=array[len(array)//2:]

        left = merge_sort(left)
        right = merge_sort(right)

        array = []
        i=0
        j=0

        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
                array.append(left[0])
                del left[0]
            else:
                array.append(right[0])
                del right[0]

        array.extend(left)
        array.extend(right)
        return array
    
    
print("Merge sort",merge_sort(array))