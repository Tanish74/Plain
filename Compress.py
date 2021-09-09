vowels = ['a','e','i','o','u']
number = [1,2,3,4,5]
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
        elif data[i] in vowels:
            for v in range(5):
                if vowels[v] == data[i]:
                    if v == 0:
                        compress.append('@')
                    else:
                        compress.append(vowels[v])
        elif data[i] == 'b':
            compress.append('&')
        else:
            compress.append(data[i])

    return compress
        

def decompress(data):
    length = getLength(data)
    ans = []

    for i in range(length):
        if data[i]=="*":
            ans.append(" ")
        elif data[i]=='@':
            ans.append("a")
        elif data[i]=='&':
            ans.append('b')
        # elif data[i] in number:
        #     ans.append(vowels[i-1])
        else:
            ans.append(data[i])

    return ans

comp = compress('There is a tree nearby')

for el in comp:
    print(el,end="")

decomp = decompress(comp)

print(" ")

for tr in decomp:
    print(tr,end="")