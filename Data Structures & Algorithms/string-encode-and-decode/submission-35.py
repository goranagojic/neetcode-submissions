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
        while len(s):
            # get string length
            n = int(s[:3])
            s = s[3:]

            # get the message
            messages.append(s[:n])
            s = s[n:]

        return messages



