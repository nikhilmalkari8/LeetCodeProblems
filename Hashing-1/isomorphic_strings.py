"Time complexity of this would be O(N), because we will be iterating through the string s"
"Space complexity of this would be O(1), because, the maximum size the dictionary and the set can grow is 26, making it O(1)"

#Explanation

"we have a dictionary and a set, dictionary will store all the matching fro, s to t"
"We will store the values from t into a set, to make sure, they are not getting repeated when we check for s"

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict = {}
        myset = set()

        n1 = len(s)
        n2 = len(t)

        if n1!=n2:
            return False

        for i in range(len(s)):
            if s[i] not in my_dict:
                if t[i] not in myset:
                    my_dict[s[i]] = t[i]
                    myset.add(t[i])
                else:
                    return False
            elif my_dict.get(s[i]) != t[i]:
                return False
            else:
                continue
        
        return True