def create_phone_number(n):
    text = "("
    for i in range(0,10):
        if i <=2:
            text += str(n[i])
            if i == 2:
                text += ") "
        elif i > 2 and i <=5:
            text += str(n[i])
            if i == 5:
                text += "-"
        elif i > 5 :
            text += str(n[i])
    print(text)
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])