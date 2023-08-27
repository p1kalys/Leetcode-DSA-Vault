class Solution(object):
    def wordPattern(self, pattern, s):
        l = s.split(" ")
        d = {}

        #check if they are same in length
        if len(pattern) != len(l):
            return False

        for i in range(len(pattern)):
            if pattern[i] in d.keys() or l[i] in d.values():
                if d.get(pattern[i]) != l[i]:
                    return False
            else:
                d.update({pattern[i]: l[i]})
        return True
        