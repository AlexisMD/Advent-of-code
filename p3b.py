f = open("day3.txt")

d = f.read()
t = []
q = dict()
r = dict()

x = 0
y = 0

q[x,y] = 1


#d = "vv"

for fun in d:
    t.append(fun)



for z in t[0::2]:

    if z == ">":
        x += 1
        
    if z == "<":
        x -= 1

    if z == "v":
        y += 1
    if z == "^":
        y -= 1
    q[x,y] = 1

y = 0
x = 0


for z in t[1::2]:

    if z == ">":
        x += 1
        
    if z == "<":
        x -= 1

    if z == "v":
        y += 1
    if z == "^":
        y -= 1
    r[x,y] = 1



final = {**q, **r}

print (len(final))







# ^v^v^v^v^v

# Santa:      ^^^^^
# Robo-Santa: vvvvv


# d = dict()
# d["vasea"] = 4
# d["vasea"] = 3
