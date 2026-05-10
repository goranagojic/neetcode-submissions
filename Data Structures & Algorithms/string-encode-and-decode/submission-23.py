class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            n = len(s)

            # convert n to 3-digit string
            # will be a function
            if n < 10:
                n = "00" + str(n)
            elif n < 100:
                n = "0" + str(n)
            else:
                n = str(n)

            message = message + n + s
            print(message)

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



