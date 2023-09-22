def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and (x % 10) == 0):
            return False

        div = 1
        while x >= 10*div:
            div *= 10
        
        while x:
            if (x % 10) != (x // div):
                return False 
            x = (x % div) // 10
            div = div / 100
        
        return True
