class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # get each element frequency as value
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # now get values to be "keys"
        # since there can be duplicates we use list
        freqs_l = list()
        for num, freq in freqs.items():
            freqs_l.append((freq, num))

        # now sort by frequency desc 
        freqs_l = sorted(freqs_l, key=lambda f: f[0], reverse=True)
        # print(freqs_l)

        # ... and return top k elements
        return [num for _, num in freqs_l[:k]]



        


         
        