from collections import defaultdict


def groupAnagrams(slist):

    #create a default dict to add if not dict
    result = defaultdict(list)
    #for each word in string list
    for s in slist:
        # create a vector of 26 letters
        count = [0]*26
        #for each letter in the current word
        for c in s:
            #we fill it with some numeric value
            #in this ascii(current) - ascii(a)
            #lets say word is "cab"
            #vector would be 82 - 80 = 2, 80 - 80, 81 - 80
            #vector is 1 1 1 0 0 0...0
            count[ord(c) - ord("a")] += 1
        
        #vector becomes key and must be hashable so tuple
        #finally we append the string to respective key, now this is list so we can append the next to same list with same key
        result[tuple(count)].append(s)
 
    return result.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))