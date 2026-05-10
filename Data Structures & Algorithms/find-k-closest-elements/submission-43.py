

class Solution:
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:

        # if arr len <= k, return arr
        if len(arr) <= k:
            return arr

        # move the window throu array
        l, r = 0, k
        while r < len(arr):
            d_new = abs(arr[r] - x)
            d_old = abs(arr[l] - x)
            if d_new < d_old:
                l += 1
                r += 1
            elif d_new == d_old:
                if arr[r] == arr[l]:
                    l += 1
                    r += 1
                elif arr[r] > arr[l]:
                    break
            else:
                break
        
        return arr[l:r]


    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr - sorted array 
        # k - how many elements to return
        # x - referent value
        # sort result in ascending order
        
        # complexities:
        #   time: O(n) + O(k) total is O(n+k)
        #   space: O(k) for the result. 

        # the idea:
        # scan the input arr to find the element with minimal distance, that will certanly be included into result.
        # In the additional pass iterate while you don't add k elements in total to the result, scaning the left and the right 
        # element of the minimal distance element. This will be two-pointer approach. If l distance is smaller then right (and in bounds), add that element, 
        # otherwise add right. In tie-breaker include the smaller value. 
        # This is one of the possible solutions, but not the optimal one.

        # calculate distance of every element in arr from x (abs distance)
        # O(n) time complexity
        min_d, min_i = float('inf'), -1
        for i in range(0, len(arr)):
            d = abs(arr[i] - x)
            if min_d > d:
                min_d = d
                min_i = i

        # add the reamining k-1 elements closest to x
        # two pointer approach, one on the left, and the other on the right of minimal distance
        # pick the smaller of two distances, and add them to the result
        # add left elem, before right since they are smaller (and array has to be sorted asc at the end). however, since i add the smallest distance element at the beginning
        l, r = min_i-1, min_i+1

        # O(k) time complexity
        i = 1
        while i < k and (r < len(arr) or l >= 0):
            ld = abs(arr[l] - x) if l >= 0 else float("inf")
            rd = abs(arr[r] - x) if r < len(arr) else float("inf")
            if ld < rd: # condition is false if ld is out-of-bounds (because ld is huge (inf)), so no explicit boundary checking here
                l -= 1
            elif rd < ld:
                r += 1
            else:
                if ld != float("inf"): # same here, if ld is inf, means it is out-of-bounds
                    l -= 1
                elif rd != float("inf"):
                    r += 1
                else:
                    break
            i += 1
        
        return arr[l+1:r]

    def findClosestElementsBruteForce(self, arr: List[int], k: int, x: int) -> List[int]:
        # brute force solution, checks every possible subarray of size k
        # complexities:
        #   time: O(n*k)
        #   space: O(k) for the output, O(1) extra space
        # as expected, this solution sometimes gets time limit exceeded when running tests
        
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