
"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

"""


def encode(strs):
    res = ""
    for s in strs:
        res+= str(len(s))+"#"+s
        
    return res

def decode(str):
    res, i = [], 0
    while i < len(str):
        j = i

        while str[j] != "#":
            j+=1
            
        length = int(str[i:j])

        res.append(str[j+1: j+1+length])

        i = j+1+length

    return res


strs = ["#", "Change", "this"]
print(f"{strs}")
print(encode(strs))
print(decode(encode(strs)))