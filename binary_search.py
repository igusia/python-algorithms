import random 
#searching for an item inside a search structure
def binary_search(search, item):
    low = 0
    high = len(search)-1
    while low <= high:
        mid = (low + high)//2 #if odd -> returns a lower number
        guess = search[mid]
        if guess < item:
            low = mid+1 #it's not mid, so we don't take it 
        elif guess > item:
            high = mid-1 #as with low
        else:
            return mid
    return None
