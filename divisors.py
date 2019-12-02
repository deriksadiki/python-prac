def divisors(integer):
    x = []
    i = 2
    while i < integer:
        if integer % i == 0:
            x.append(i)
        i += 1
    if len(x) == 0:
        print(str(integer) + " is a prime")
    else:
        print(x)
divisors(13)
