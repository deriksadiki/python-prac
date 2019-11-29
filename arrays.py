import math
import random
from datetime import date

words = ["man", "woman", "music", "food", "cars"]
numbers = [30,45,20,36,0,10];

# print(random.choice(words))
# print(random.choice(numbers))
today =  date.today()
prevDate = date(2019, 10,29)
exa =  prevDate.strftime("%m-%d-%y. %Y")
numDays = today - prevDate
print(exa)