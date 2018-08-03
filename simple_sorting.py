#an implementation of stupid search
def find_smallest(array):
    smallest = array[0]
    index = 0
    for i in range(1,len(array)):
        if array[i]<smallest:
            smallest = array[i]
            index = i
    return index

def sorting(array):
    arr = []
    for i in range(len(array)):
        arr.append(array.pop(find_smallest(array)))
    return arr

print(sorting([1,3,2,5,4]))
