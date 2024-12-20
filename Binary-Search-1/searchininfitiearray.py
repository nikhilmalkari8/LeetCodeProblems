# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start = 0
        end = 1

        while (reader.get(end) < target):
            start = end
            end = end * 2

        while(start <= end):
            mid = (start + end)//2

            if reader.get(mid) == target:
                return mid
            
            elif reader.get(mid) < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1 
        