import re
data = open("day2.txt")
text = data.read()

def prism(l,w,h): # calculating are for rectangular pris
    d = [l,w,h]
    d.sort()
    z = (d[0]+d[1] )* 2 
    volume = l * w * h
    result = volume + z
    return  result




r = 0
for row in text.split():
    a,b,c = [int(u) for u in row.split('x')]
    q = prism (a,b,c)
    r = r + q
print (r)

