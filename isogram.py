def is_isogram(string):
    for i in string:
        counter = 0
        for x in string:
            if x == i:
                counter += 1
            if counter == 2:
                return "false"
                break
    return "true"
print(is_isogram("aba"))