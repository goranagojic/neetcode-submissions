class Solution:

    def encode(self, strs: List[str]) -> str:
        # idea: each record is a 3-digit zero-padded length header followed by the payload.
        # n = number of strings, M = total chars across all strings.
        # time:  O(M + n) amortized, relying on CPython's refcount-1 in-place `+=` optimization.
        # space: O(M + n) for the encoded output.

        encoding = ''
        for s in strs:
            header = f"{len(s):03d}"
            encoding += header + s

        return encoding


    def encode1(self, strs: List[str]) -> str:
        # encodes the string 
        # the idea: send the message that will have pairs (header, s). header is always a three character substring that contains
        # stringified length of the succseeding string.
        # time complexity: O(nm)
        # space complexity: O(m+3*n) -> O(nm)

        content_size = 0
        for s in strs:
            content_size += len(s)

        encoding = [''] * (len(strs) * 3 + content_size)

        p = 0
        for s in strs:
            s_n = ''
            n = len(s)              # 1
            if n < 10:              # 1
                s_n = f"00{n}"
            elif n < 100:
                s_n = f"0{n}"
            else:
                s_n = str(n)

            encoding[p:p+3] = s_n
            p += 3
            encoding[p:p+n] = s
            p += n
             
        return ''.join(encoding)



    def decode(self, s: str) -> List[str]:
        # decodes the string
        # time complexity: O(m)
        # space complexity: O(n)

        message = []
        p = 0

        while p < len(s):                   # m
            n = int(s[p:p+3])               # 1
            message.append(s[p+3:p+3+n])    # amortized O(1)
            p += 3 + n                      # 1

        return message
