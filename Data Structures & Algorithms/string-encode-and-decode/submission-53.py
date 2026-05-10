class Solution:

    # APPROACH 1.1 - FIXED-SIZE HEADER, growing the encoding
    # def encode(self, strs: List[str]) -> str:
    #     # idea: each record is a 3-digit zero-padded length header followed by the payload.
    #     # n = number of strings, M = total chars across all strings.
    #     # time:  O(M + n) amortized, relying on CPython's refcount-1 in-place `+=` optimization.
    #     # space: O(M + n) for the encoded output.

    #     encoding = ''
    #     for s in strs:                  # n
    #         header = f"{len(s):03d}"
    #         encoding += header + s      # M

    #     return encoding


    # APPROACH 1.2 - FIXED-SIZE HEADER, preallocated encoding
    # def encode(self, strs: List[str]) -> str:
    #     # idea: same wire format, but preallocate a list of 3n+M slots and slice-fill it.
    #     # n = number of strings, M = total chars across all strings.
    #     # time:  O(M + n) — strictly linear, no reliance on CPython's `+=` optimization.
    #     # space: O(M + n).

    #     content_size = 0
    #     for s in strs:
    #         content_size += len(s)

    #     encoding = [''] * (len(strs) * 3 + content_size)

    #     p = 0
    #     for s in strs:
    #         n = len(s)
    #         header = f"{n:03d}"
    #         encoding[p:p+3] = header
    #         p += 3
    #         encoding[p:p+n] = s
    #         p += n

    #     return ''.join(encoding)


    # APPROACH 1 - decoder for both approaches 1.1 and 1.2
    # def decode(self, s: str) -> List[str]:
    #     # n = number of strings produced, M = total chars across decoded strings.
    #     # time:  O(M + n) — each byte of `s` is read once.
    #     # space: O(M + n) for the returned list (O(n) of list overhead + O(M) of slice contents).

    #     message = []
    #     p = 0

    #     while p < len(s):                   # m
    #         n = int(s[p:p+3])               # 1
    #         message.append(s[p+3:p+3+n])    # amortized O(1)
    #         p += 3 + n                      # 1

    #     return message


    # APPROACH 2 - VARIABLE-SIZED HEADER (with growing encoding, that can be modified  to be fixed size)
    # The optimal approach that has variable-length header with hard-coded delimiter
    def encode(self, strs: List[str]) -> str:
        # idea: write `len(s)#s` for each string; `#` terminates the variable-length length prefix.
        # n = number of strings, M = total chars across all strings.
        # time:  O(M + n) — each input char is copied once into a part, then once by `join`.
        # space: O(M + n) for the parts list and the joined output.

        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        # n = number of strings produced, M = total chars across decoded strings.
        # time:  O(M + n) — outer and inner loops together visit each byte of `s` exactly once.
        # space: O(M + n) for the returned list of slices (O(n) of list overhead + O(M) of slice contents).

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            res.append(s[j + 1:j + 1 + n])
            i = j + 1 + n
        return res
