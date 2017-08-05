class Solution:
    def judgeSquareSum(self, c):
    	for a in range(int(c ** 0.5) + 1):
    		b = c - (a ** 2)
    		if (int(b ** 0.5) ** 2) == b:
    			return True
    		return False
solution = Solution()
result = solution.judgeSquareSum(7)
print(result)