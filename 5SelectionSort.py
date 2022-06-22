
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

def selectionSort(arr):
    spot_marker = 0
    comparisons = 0
    while spot_marker < len(arr):
        for num in range(spot_marker,len(arr)):
            comparisons += 1
            if arr[spot_marker] > arr[num]:
                arr[num], arr[spot_marker] = arr[spot_marker], arr[num]
                print(f'swap done at number: {num}')
        spot_marker += 1 
    print (arr)  
    print (comparisons)

selectionSort(l)
