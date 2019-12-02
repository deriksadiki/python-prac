def find_short(s):
    words = s.split(' ')
    x = len(words[0])
    for i in range(len(words)):
        if (len(words[i]) < x):
            x = len(words[i])
    print(x)
find_short("i want to travel the world writing code one day")