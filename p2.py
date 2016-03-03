import re
data = open("day2.txt")
text = data.read()

def prism(l,w,h): # calculating are for rectangular prism
    x = l*w
    y = w*h
    z = h*l
    d = min(x,y,z)
    area = 2*(x + y + z) + d    
    print (area)

 



text = re.sub('[x]', '', text)

