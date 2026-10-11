class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        else:
            encoded_string = "~" + str(len(strs[0])) + "#" + strs[0]
            for i in range(1, len(strs)):
                code = "~" + str(len(strs[i])) + "#"
                encoded_string = encoded_string + code + strs[i]
            return encoded_string



    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_string =[]
        j = 1
        if s == "":
            return []
        while j < len(s):
            if s[j].isdigit() and s[j+1] == "#":
                integr = int(s[j])
                if integr > 0:
                    decoded_string.append(s[j+2: j+2+integr])
                else:
                    decoded_string.append("")
                j = j+3+integr 
            elif s[j:j+2].isdigit() and s[j+2] == "#":
                integr = int(s[j:j+2])
                decoded_string.append(s[j+3: j+3+integr])
                j = j+4+integr
            elif s[j:j+3].isdigit():
                integr = int(s[j:j+3])
                decoded_string.append(s[j+4: j+4+integr])
                j = j+5+integr            

        
        return decoded_string


            
            
        
