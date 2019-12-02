def maskify(cc):
    x  = len(cc)
    y = x - 4
    text = ""
    for i in range(x):
        if i >= y:
            text += cc[i]
        else:
            text += "#"
    print(text)
maskify("4556364607935616")