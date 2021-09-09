
def getLength(x):
    length = 0
    for i in x:
        length +=1
    return int(length)


def compress(data):
    length = getLength(data)
    compress = []
    for i in range(length):
        if data[i]==" ":
           compress.append('*')
        else:
            compress.append(data[i])

    l2 = getLength(compress)

    return compress
        

def decompress(data):
    length = getLength(data)
    ans = []

    for i in range(length):
        if data[i]=="*":
            ans.append(" ")
        else:
            ans.append(data[i])

    l2 = getLength(ans)

    return ans

comp = compress('There is a tree nearby')

for el in comp:
    print(el,end="")

decomp = decompress(comp)

print(" ")

for tr in decomp:
    print(tr,end="")