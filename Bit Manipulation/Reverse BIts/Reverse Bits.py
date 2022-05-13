"""
https://leetcode.com/problems/reverse-bits/
"""
def reverseBits(self, n: int) -> int:
        rev = 0
        
        for _ in range(32):
            rev = rev << 1
            if(n&1== 1):
                rev = rev ^ 1
            
            n = n >>1
        
        
        return rev