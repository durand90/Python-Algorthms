

# def isValid(s):

#     brackets = []

#     hash = {")":"(", "}":"{", "]":"["}

#     for char in s:
#         if char in hash:
#             if stack and stack[-1] == hash[char]:
#                 stack.pop()
#             else: 
#                 return false
        
#         else:
#             stack.append(char)

#     return not stack


my_dict = {"]":"[", ")":"("}

s = [")", "[", "[", "("]

b = []

for char in s:

    if b and b[-1] == my_dict[char]:
        print(b)
        b.pop()
    
    if char in my_dict:
        b.append(char)
        print(char)
        print(b)
        print(b[-1])


print 

        