class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0 
        max = ans 
        for i in gain:
            ans += i
            if ans > max:
                max = ans

        return max