def openOrSenior(data):
    for row in range(len(data)):
        if data[row][0] >= 55 and data[row][1]> 7:
            print("Senior")
        else:
            print("Open")

openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]])