f = open("day3.txt")

d = f.read()
t = []
q = dict()


x = 0
y = 0
q[x,y] = 1

for fun in d:
    t.append(fun)



for z in t:

    if z == ">":
        x += 1
        
    if z == "<":
        x -= 1

    if z == "v":
        y += 1
    if z == "^":
        y -= 1
    q[x,y] = 1

print (len(q))











# d = dict()
# d["vasea"] = 4
# d["vasea"] = 3
