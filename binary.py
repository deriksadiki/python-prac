def binary_to_number(arr):
    x = 0;
    numbers = [8,4,2,1]
    for i in range(4):
        if arr[i] == 1:
            x += numbers[i]
    print(x)
binary_to_number([0,1,1,0])