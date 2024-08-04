def mergeAlternately(word1, word2):
    term1,term2 = len(word1),len(word2)
    postion1,postion2 = 0,0
    word = 1
    array = []

    while postion1 < term1 and postion2 < term2:
        if word == 1:
            array.append(word1[postion1])
            postion1 = postion1 + 1
            word = 2
        
        else:
            array.append(word2[postion2])
            postion2 = postion2 + 1
            word = 1

    while postion1 < term1:
        array.extend(word1[postion1])
        postion1 = postion1 + 1
    
    while postion2 < term2:
        array.extend(word2[postion2])
        postion2 = postion2 + 1

    return ''.join(array)

mergeAlternately('ace','bdf') 
