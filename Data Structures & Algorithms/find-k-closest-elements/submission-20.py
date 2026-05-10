

class Solution:
    def findClosestElementsTwoPointers(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr - sorted array 
        # k - how many elements to return
        # x - referent value
        # sort result in ascending order
        # the elements will be subsequent because the input array is sorted, the output also can remain sorted easily

        # alocate space for the result - k size array
        res = [0] * k
        # calculate distance of every element in arr from x (abs distance)
        min_d, min_i = 10001, 10001
        tmp = [0] * len(arr)
        for i in range(0, len(arr)):
            d = abs(arr[i] - x)
            if min_d > d:
                min_d = d
                min_i = i
            tmp[i] = d
        # print(tmp)
        # print(f"min_i: {min_i}, min_d: {min_d}")
            # while calculating keep track of the min value

        # loop through distances in the following
        # position yourself to the min elem, l, r pointers
        # while k > 0:
        # check if l or r point to the closer value
        # include that value, move pointer to the left or the right
        # handle l, r boundaries
        res[0] = arr[min_i]
        l, r = min_i-1, min_i+1
        i = 1
        while i < k and (r < len(arr) or l >= 0):
            ld = tmp[l] if l >= 0 else float("inf")
            rd = tmp[r] if r < len(arr) else float("inf")
            if l >= 0 and ld <= rd:
                res[i] = arr[l]
                l -= 1
            elif r < len(arr) and rd < ld:
                res[i] = arr[r]
                r += 1
            else:
                if l >= 0:
                    res[i] = arr[l]
                    l -= 1
                elif r < len(arr):
                    res[i] = arr[r]
                    r += 1
                else:
                    break
            i += 1
            # print(f"l={l}, r={r}, res={res}")
            
        res.sort()
        
        return res

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        min_distance = float("inf")
        s = 0

        for i in range(0, len(arr) - k + 1):
            dist = 0
            for j in range(i, i+k):
                dist += abs(arr[j] - x)
            if dist < min_distance:
                s = i
                min_distance = dist

        res = [0] * k
        for i in range(0, k):
            res[i] = arr[s+i]

        return res
            

