text = input("Please enter a text: ")
def findVowel():
    newText = ""
    for i in text:
       if i in "AEIOUaeiou":
           newText += "x"
       else:
           newText += i
    return newText 
print(findVowel())




