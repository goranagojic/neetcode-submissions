class Solution:

    def encode(self, strs: List[str]) -> str:
        # encodes the string 
        # the idea: send the message that will have pairs (header, s). header is always a three character substring that contains
        # stringified length of the succseeding string.

        encoding = ''
        for s in strs:
            n = len(s)
            if n < 10:
                n = f"00{n}"
            elif n < 100:
                n = f"0{n}"
            else:
                n = str(n)
            encoding += n + s
             
        return encoding

    def decode(self, s: str) -> List[str]:
        # decodes the string

        message = []
        p = 0

        while p < len(s):
            n = int(s[p:p+3])
            message.append(s[p+3:p+3+n])
            p += 3 + n

        return message
