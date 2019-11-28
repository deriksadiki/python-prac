from Person import Person

user = Person("derk", "sadiki")
print(user.name)

def myFunc():
    print("hello")

def loop():
    for i in range(7):
        print(i)

def openFile():
    f = open('./data/movie_lines.txt', 'r')
    print(f.readline())

def createFile():
    try:
        file =  open("myfile.txt", "x")
        file.close()
    except:
        print("file exits")
    finally:
        file =  open("myfile.txt", "a")
        file.write("this is the best year to learn python in 2019\n")
        file.close()
        file =  open("myfile.txt", "r")
        lineList = file.readlines()
        file.close()
        print("the last line is " + lineList[len(lineList) - 1])

class person:
    def __init__(self, fname, lname):
        self.name = fname
        self.surname = lname
    def age(self):
        return 20


