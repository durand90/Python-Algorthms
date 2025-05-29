
class Solution(object):
    def longestCommonPrefix(self, strs):

        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]

        keep_track = ""

        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
               
               keep_track += first[i]

            else: 
                break
        print(keep_track)
        return keep_track 
    


ar = ["Puppy", "Hully", "Gurr", "Putty"]

sol = Solution()

sol.longestCommonPrefix(ar)