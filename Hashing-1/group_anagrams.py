"Time Complexity for this code would be O(N*k) since we are iterating through every value in the list and also additionally at every value, we are sorting it"


#Explanation

"We iterate through each value in the list, sort it and make it a key, if they key isnt present, we first initiate the values are going to be a list"
"Next, when ever we get an anagram of it, we append it in the list associate with the key and finally return all the values"

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for i in range(len(strs)):
            check = ''.join(sorted(strs[i]))

            if check not in my_dict:
               my_dict.setdefault(check, []).append(strs[i])
            else:
                my_dict[check].append(strs[i])
        
        values = list(my_dict.values())

        return values
            
        