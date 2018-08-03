import random 
#searching an item inside a search structure
def binary_search(search, item):
    low = 0
    high = len(search)-1
    while low <= high:
        mid = (low + high)//2 #if odd -> returns the lower number
        guess = search[mid]
        if guess < item:
            low = mid+1
        elif guess > item:
            high = mid-1 #it's not mid, so we don't take it 
        else:
            return mid
    return None
a = binary_search([1,2,3,4,5,6,7,8,9,10], random.randint(1,10))
print(a)
