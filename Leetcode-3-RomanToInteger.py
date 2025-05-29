

class Solution(object):
    def romanToInt(self, s):
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        res = 0
    #create a map to store the roman numero with the equivalent of the english number
    #     
        for i in range(len(s)):
            if i + 1 < len(s) and my_dict[s[i]] < my_dict[s[i + 1]]:
                res -= my_dict[s[i]]

            else: 
                res += my_dict[s[i]]
        print(res)
        return res
    

sol = Solution()

sol.romanToInt("XC")