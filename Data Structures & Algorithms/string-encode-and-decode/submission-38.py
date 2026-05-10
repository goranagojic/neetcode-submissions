class Solution:

    def _3_digit_len(self, n):
        # space complexity: O(3)
        # time complexity: O(1)
        if n < 10:
            return "00" + str(n)
        elif n < 100:
            return "0" + str(n)
        else:
            return str(n)

    def encodeExpensive(self, strs: List[str]) -> str:
        # WARNING! strings in python are imutable, so concatenating strings each time
        # copies both strings to the new location
        message = ""
        
        # time complexity O(N)
        # space complexity O(N)
        for s in strs:
            # n is always 3 digit string representation of the string length
            # length is fixed to 3 since len(s) is between 0 and 200 by task definition
            n = self._3_digit_len(len(s))  # O(1)

            message = message + n + s  # concatenating like this is O(T^2) time because string is created by allocating space for n, s, message and than copying all of three to the common buffer
            print(message) # just informative

        return message

    def encode(self, strs: List[str]) -> str:
        message = []
        # repeats n times
        # time complexity O(N)
        # space complexity O(N)
        for s in strs:
            # n is always 3 digit string representation of the string length
            # length is fixed to 3 since len(s) is between 0 and 200 by task definition
            n = self._3_digit_len(len(s))  # O(1)

            message.append(n)
            message.append(s)

        return "".join(message) # this join is linear

    def decodeExpensive(self, s: str) -> List[str]:
        # space complexity of O(n)

        messages = []
        # time complexity O(n)
        while len(s):
            # get string length
            n = int(s[:3])
            s = s[3:] 

            # get the message
            messages.append(s[:n])
            s = s[n:]

        return messages

    def decode(self, s: str) -> List[str]:
        # space complexity of O(n)

        messages = []
        s_idx = 0
        # time complexity O(n)
        while s_idx < len(s):
            # get string length
            n = int(s[s_idx:s_idx+3])
            s_idx += 3

            # get the message
            messages.append(s[s_idx:s_idx+n])
            s_idx += n

        return messages