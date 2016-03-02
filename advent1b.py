text = open("santa.txt")
data = text.read()
santa  = 0
count  = 0
for c in data:
    if c == "(":
        count += 1
        santa += 1
    if c == ")":
        count += 1
        santa -= 1
    if santa == -1:
        break
print (count)

