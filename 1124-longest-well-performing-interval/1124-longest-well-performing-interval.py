class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n , new= len(hours) , []
        for hour in hours :
            new.append(1 if hour > 8 else -1)
        prefix , curr = [],0
        for num in new :
            curr += num
            prefix.append(curr)
        
        res,dic = 0,{}
        print(prefix)
        for i, num in enumerate(prefix):
            if num > 0:
                res = max(i + 1 ,res)
                if num not in dic :
                    dic[num] = i
                continue
            if num - 1 in dic:
                j = dic[num - 1]
                print(num,j)
                res = max(res, i - j)
            if num not in dic:
                dic[num] = i
        return res