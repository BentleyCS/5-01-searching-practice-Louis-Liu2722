import random

def randomSearch(items:list, target:int) -> int:

    count =0

    while True:
        search=random.randint(0, len(items)-1)
        count+=1
        if items[search]==target:
            print(count)
            return search




def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    pass
    count=0
    for i in range(len(items)):
        count+=1
        if items[i]==target:
            return (i, count)
    else:
        return (-1,count)





def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    pass
    start=0
    end=len(items)-1
    count=0

    while start<=end:
        mid=(start+end)//2
        count+=1

        if items[mid]==target:
            return (mid,count)
        elif items[mid]<target:
            start=mid+1
        else:
            items[mid]>target
            end=mid-1
    return (-1,count)






