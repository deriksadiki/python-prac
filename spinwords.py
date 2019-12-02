def spin_words(sentence):
    x  =  len(sentence)
    y = ""
    for i in reversed(range(x)):
        y += sentence[i]
    print(y)  

spin_words("Welcome")