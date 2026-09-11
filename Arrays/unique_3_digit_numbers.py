class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        number = set()
        n = len(digits)
        for i in range(n):
            if(digits[i] == 0):
                continue

            for j in range(n):
                if j == i:
                    continue
                
                for k in range(n):
                    if k == i & k == j:
                        continue 
                    

                if digits[k] % 2 != 0:  #last even
                    continue

                num = digits[i] * 100 + digits[j] * 10 + digits[k]
                number.add(num)

        return len(number)