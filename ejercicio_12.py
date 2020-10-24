def stringIsomorphic(s1, s2):
    dic = {} 
    sameSize = len(s1) == len(s2)
    if sameSize:
        for i in range(len(s1)):
            dic[s1[i]] = s2[i]
    print(dic)

stringIsomorphic("abc", "bbc")

