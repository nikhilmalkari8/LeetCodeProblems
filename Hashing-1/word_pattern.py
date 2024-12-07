class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        check = s.split(" ")
        my_dict = {}
        myset = set()

        n1 = len(pattern)
        n2 = len(check)

        if n1!=n2:
            return False

        for i in range(len(pattern)):
            if pattern[i] not in my_dict:
                if check[i] not in myset:
                    my_dict[pattern[i]] = check[i]
                    myset.add(check[i])
                else:
                    return False
            elif my_dict.get(pattern[i]) != check[i]:
                return False
            else:
                continue
        
        return True




        