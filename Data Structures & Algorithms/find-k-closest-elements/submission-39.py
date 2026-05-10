

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
        # see what to do with sorting


    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr - sorted array 
        # k - how many elements to return
        # x - referent value
        # sort result in ascending order
        
        # complexities:
        #   time: O(n) + O(k) + O(klogk) total is O(n+klogk)
        #   space: O(n) for tmp array, where n i a length of arr + O(k) for the result. final extra space complexity is O(k), total O(n+k)

        # the idea:
        # precalculate distances of all elements in the array from the element x, keeping track of the minimal distance because that will be the element that
        # must be included into result. In the additional pass iterate while you don't add k elements in total to the result, scaning the left and the right 
        # element of the minimal distance element. This will be two-pointer approach. If l distance is smaller then right (and in bounds), add that element, 
        # otherwise add right. since i dont add the minimal element in the right position (because i don't know how many elements will preceede) that element is added
        # to the first position and the res array is sorted later. This is not the optimal solution.

        # alocate space for the result - k size array
        # O(n) space complexity
        res = [0] * k
        # calculate distance of every element in arr from x (abs distance)
        # O(n) time complexity
        min_d, min_i = 10001, 10001
        tmp = [0] * len(arr)
        for i in range(0, len(arr)):
            d = abs(arr[i] - x)
            if min_d > d:
                min_d = d
                min_i = i
            tmp[i] = d

        # add the reamining k-1 elements closest to x
        # two pointer approach, one on the left, and the other on the right of minimal distance
        # pick the smaller of two distances, and add them to the result
        # add left elem, before right since they are smaller (and array has to be sorted asc at the end). however, since i add the smallest distance element at the beginning
        # this is not that relevant because i have to sort the res anyway
        # res[0] = arr[min_i]
        l, r = min_i-1, min_i+1
        i = 1
        # O(k) time complexity
        while i < k and (r < len(arr) or l >= 0):
            ld = tmp[l] if l >= 0 else float("inf")
            rd = tmp[r] if r < len(arr) else float("inf")
            if ld < rd: # condition is false if ld is out-of-bounds (because ld is huge (inf)), so no explicit boundary checking here
                # res[i] = arr[l]
                l -= 1
            elif rd < ld:
                # res[i] = arr[r]
                r += 1
            else:
                if ld != float("inf"): # same here, if ld is inf, means it is out-of-bounds
                    # res[i] = arr[l]
                    l -= 1
                elif rd != float("inf"):
                    # res[i] = arr[r]
                    r += 1
                else:
                    break
            i += 1
            
        # # O(klogk) time complexity
        # res.sort()
        
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