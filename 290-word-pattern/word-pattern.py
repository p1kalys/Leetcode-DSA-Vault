class Solution(object):
    def wordPattern(self, pattern, s):
        l = s.split(" ")
        dic = {}

        #check if they are same in length
        if len(pattern) != len(l):
            return False

        for i in range(len(pattern)):
            #add to dic if not exist
            if pattern[i] not in dic.keys():
                #add to dic if string's words do not exist
                if l[i] not in dic.values():
                    dic[pattern[i]] = l[i]
                else:
                    return False
            else:
                #pass if they are the same, else break and return False
                if dic[pattern[i]] == l[i]:
                    continue
                else:
                    return False

        return True