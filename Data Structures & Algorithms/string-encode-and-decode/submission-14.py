class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for elem in strs:
            elem_length = str(len(elem)) + ':' 
            output = output + elem_length + elem
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        kopim_many = ""
        while (i < len(s)):
            if '0' <= s[i] <= '9':
                kopim_many += s[i]
                i+=1
            elif s[i] == ':':
                full_mana = int(kopim_many)
                output.append(s[i+1:i+full_mana+1]) 
                i = i + full_mana + 1
                kopim_many = ""
        return output

