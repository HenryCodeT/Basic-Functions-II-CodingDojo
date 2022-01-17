# 1-Countdown
print("******* 1-Countdown**********")
def countdown(number):
    arrays = []
    for i in range(number,-1,-1):
        arrays.append(i)    
    return arrays
result = countdown(5) 
print(result)
print("******* 2-Print and Return**********")
# 2-Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]

result=print_and_return([1,2]) 
print(result)

print("******* 3-First Plus Length**********")
# 3-First Plus Length
def first_plus_length(arr):
    return arr[0]+len(arr)
result = first_plus_length([1,2,3,4,5]) 
print(result)

print("******* 4-Values ​​greater than second**********")
# 4-Values ​​greater than second
def values_greater_than_second(arr):
    newlist=[]
    if len(arr)<2:
        return False
    else:
        for i in arr:
            if i>arr[1]:
                newlist.append(i)
    print(len(newlist))
    return newlist
result=values_greater_than_second([5,2,3,2,1,4])
print(result)

print("******* 5-This Length, That Value**********")
# 5-This Length, That Value
def length_and_value(a,b):
    newArray = []
    for i in range(0,a):
        newArray.append(b)
    return newArray
result1=length_and_value(4,7)
print(result1)
result2=length_and_value(6,2)
print(result2)