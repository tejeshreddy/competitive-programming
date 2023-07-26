class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) >= hour + 1  : return -1
        left,right = 1, 10 ** 7
        while left<right:
            mid=(left+right)//2
            if sum([ceil(i/mid) for i in dist[:-1]])+(dist[-1]/mid) <= hour :
                right=mid
            else:
                left=mid+1
        return left