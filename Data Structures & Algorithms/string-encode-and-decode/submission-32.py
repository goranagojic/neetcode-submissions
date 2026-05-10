class Solution:

    def _3_digit_len(self, n):
        if n < 10:
            return "00" + str(n)
        elif n < 100:
            return "0" + str(n)
        else:
            return str(n)

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            # n is always 3 digit string representation of the string length
            # length is fixed to 3 since len(s) is between 0 and 200 by task definition
            n = self._3_digit_len(len(s))

            message = message + n + s
            print(message) # just informative

        return message


    def decode(self, s: str) -> List[str]:

        messages = []
        sidx = 0
        while sidx < len(s)-1:
            # get string length
            n = s[sidx:sidx+3]
            if len(n) == 3 and n.isdigit():
                n = int(n)
            else:
            # n = int(s[sidx:sidx+3])
                print(f"There is some problem with this value of n {n}")
            # s = s[3:]
            sidx += 3

            # get the message
            messages.append(s[sidx:sidx+n])
            print(messages)
            # s = s[n:]
            sidx += n

        return messages



