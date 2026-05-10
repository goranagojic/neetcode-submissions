class Solution:
    def _place_num_bucket(self, num, buckets):
        for i, bucket in enumerate(buckets):
            if num in bucket:
                continue
            bucket.add(num)
            break

        return
            

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # SOLUTION 1 - Calculate a frequency dictionary for all values in num list
        # time complexity: ???
        # frequencies = dict()    # key: number, value: frequency
        # for num in nums:
        #     if frequencies.get(num) is None:
        #         frequencies[num] = 1
        #     else:
        #         frequencies[num] += 1

        # # then get the list of pairs
        # freq_list = list(frequencies.items())
        # # sort by frequency
        # freq_list.sort(key=lambda v: v[1], reverse=True)

        # return [num for num, freq in freq_list[:k]]

        # SOLUTION 2 - Use heap data structure - this structure is often used in TopK problems
        # TODO

        # SOLUTION 3 - Use bucket sort
        # 1) Buckets are frequences of number appearing in the array - in this way, the memory complexity of the solution is bounded to N, 
        # since the highest frequency can be N (single number appearing N times)
        buckets = [set() for _ in nums]

        # populate buckets
        for num in nums:
            self._place_num_bucket(num, buckets)

        print(buckets)

        # iterate through buckets to get most frequent elements
        result = set()

        # skip all unpopulated buckets on the end of the array
        for bucket in reversed(buckets):
            if len(bucket) == 0:
                continue

            for element in bucket:
                if k > 0:
                    if element not in result:
                        result.add(element)
                        k = k - 1
                    else:
                        continue
                else:
                    break

        return list(result)

               
        

            
            
