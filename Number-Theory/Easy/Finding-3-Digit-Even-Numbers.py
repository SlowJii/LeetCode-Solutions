class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freg = Counter(digits)
        unique_nums = set()
        for i in range(1,10):
            if freg[i] == 0:
                continue
            freg[i] -= 1

            for j in range(0,10):
                if freg[j] == 0:
                    continue
                freg[j] -= 1

                for k in range(0,10,2):
                    if freg[k] == 0:
                        continue
                    num = i*100 + j*10 + k
                    unique_nums.add(num)
                    
                freg[j] += 1

            freg[i] += 1

        return sorted(unique_nums)        