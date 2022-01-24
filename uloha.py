import random
N = 25
array = []
for i in range(N):
    if random.randint(0,1):
        array.append(i)

print(array)
x_int = input("Vyhľadať číslo: ")
x = int(x_int)
print(x)
def binarne_vyhladavanie(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
result = binarne_vyhladavanie(array, x)

if result != -1:
    print("Číslo sa nachádza v poradí:", str(result))
else:
    print("Čislo sa v poli nenachádza")

element = 25
array = [1,2,5,4,13,14,17,18,21,22,25]
