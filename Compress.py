vowels = ['a','e','i','o','u']
space = ' '

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

    for i in range(len(compress)):
        print(compress[i],end = "")

print(compress('Tanish is a good boy'))