class Solution:
    def para(self):
        d = {
                "(": ")",
                "{": "}",
                "[": "]"
            }

        for key,value in d.items():
            print(f"{key}: {value}")

s = Solution()
s.para()
