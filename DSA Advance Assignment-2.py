#1.Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  
arr = [33,887,60,20,9,8,56,75]
target = int(input("Enter the target:"))
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
#2.Implement Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    sorted_arr = merge(left_half, right_half)
    return sorted_arr
def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged
arr = [20,8,95,88,30,12]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
#3.Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]  
    left = quick_sort(left)
    right = quick_sort(right)
    return left + middle + right
arr = [12,11,13,5,6,7]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
#4.Implement Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [10,15,6,78,90]
insertion_sort(arr)
print("Sorted array:", arr)
#5.Write a program to sort list of strings (similar to that of dictionary)
my_list = ["Iam", "Studying", "Data Science", "At", "Edyoda"]
sorted_list = sorted(my_list)
for word in sorted_list:
    print(word)
