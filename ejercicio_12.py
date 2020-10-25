def stringIsomorphic(s1, s2):
    dic = {} 
    count = 0
    sameSize = len(s1) == len(s2)
    if sameSize:
        for i in range(len(s1)):
            if s1[i] in dic:
                if dic.get(s1[i]) != s2[i]:
                    count += 1
            else:
                dic[s1[i]] = s2[i]
    else:
        print("Hey! The size of the strings are not the same.")
        return False
    if count > 0:
        return False
    else:
        return True


