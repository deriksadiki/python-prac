def high_and_low(numbers):
    x  =  numbers.split(' ')
    min =x[0]
    max = "0"
    for i in x:
       if int(i) < int(min):
          min = i
       if int(i) > int(max):
          max = i
    y = min + " " + max
    print(y)         
high_and_low("10 2 3 80 5")