import hashlib

def hasher(mystring): #Generate md5
    return hashlib.md5(mystring.encode("utf-8")).hexdigest()
w = 0
word = "ckczppom"
d = hasher(word)
while not d.startswith("000000"):
    w += 1
    word = "ckczppom"
    word += str(w)
    d = hasher(word)
else:
    print(w)
