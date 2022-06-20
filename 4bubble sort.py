l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(l) - 1):
            if arr[num] > arr[num+1]:
                print (f"sawp happened at {arr[num]} and {arr[num + 1]}")
                arr[num], arr[num+1] = arr[num + 1], arr[num]
                swap_happened = True 
                print (arr)
    

bubble_sort(l)