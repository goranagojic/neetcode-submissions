import heapq

class Solution:
    def topKFrequentMinHeap(self, nums: List[int], k: int) -> List[int]:
        # top k frequent elements using min-heap
        # total time complexity:
        # O(n) + O(g) + O(1) + 2*g*O(logk) = O(n) + O(g) + 2*O(glogk)
        # g is bounded by n, k is typically a small value futher away from n
        # O(n) + O(n) + O(nlogk) - approximating function O(nlogk)

        # calculate frequences
        # O(n)
        freqs = dict()
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        # prepare data for heap - number frequency pairs
        # O(g)
        freq_l = list()
        for num, freq in freqs.items():
            freq_l.append((freq, num))

        # add to min heap - keep the heap of size k
        freq_h = list()
        heapq.heapify(freq_h) # O(1) since the freq_h is empty

        # g times
        for freq, num in freq_l:
            heapq.heappush(freq_h, (freq, num)) # O(log k)
            if len(freq_h) > k:
                heapq.heappop(freq_h) # O(log k)
            
        return [num for freq, num in freq_h] # O(k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = dict()
        
        # count frequences
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        # create buckets for frequences
        buckets = [list() for _ in range(len(nums)+1)]

        # fill them in with numbers
        for num, freq in freqs.items():
            buckets[freq].append(num)

        # get top-k most frequent
        top_k = list()
        for bucket in reversed(buckets):
            if not bucket:  # skip empty buckets
                continue

            n = k if k <= len(bucket) else len(bucket)
            top_k.extend(bucket[:n])
            k -= n

            if k == 0:
                break

        # or alternative
        # top_k = list()
        # for bucket in reversed(buckets):
        #     for num in bucket:
        #         top_k.append(num)
        #         if len(top_k) == k:
        #             return top_k

        return top_k




        