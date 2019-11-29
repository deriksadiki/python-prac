def likes(names):
    length = len(names)
    if length == 0:
        print("no one likes this")
    elif length == 1:
        print(names[0] + " likes this")
    elif length == 2:
        print(names[0] + " and " + names[1] + " likes this")
    elif length == 3:
        print( names[0] + ", " + names[1] + " and " + names[2] + " likes this")
    elif length >= 4:
        x =  length - 2
        print(names[0] + ", " + names[1] + " and " + str(x) + " others like this")
        
        
likes(['Alex', 'Jacob'])