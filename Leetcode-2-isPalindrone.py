
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        store = ""
        for i in range(len(x) - 1, -1, -1):
            store += x[i]

        if x == store:
            print(x, store)
            return "palindrome"
        else: 
            print(x)
            print(store)
            return "not a palindrome"


sol = Solution()

x = "mateetam"

print(sol.isPalindrome(x))




# def reverse_string(s):
#     result = ""
#     for i in range(len(s) - 1, -1, -1):
#         result += s[i]
#     return result

# print(reverse_string("hello"))  # Output: "olleh"