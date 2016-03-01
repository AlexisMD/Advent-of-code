text = open("santa.txt") # input file
data = text.read()
santa  = 0

for c in data:
    if c == "(":
        santa += 1
    if c== ")":
        santa -= 1
print (santa)
