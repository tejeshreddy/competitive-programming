class Solution:
    def countAndSay(self, n: int) -> str:
        next_say = "1"
        if n == 1:
            return next_say
        
        i = 2
        
        while i <= n:
            temp = []
            cur_c, cur_v = 0, ""
            
            for k, v in enumerate(next_say):
                if cur_v == "":
                    cur_v = v
                    cur_c = 1
                elif v == cur_v:
                    cur_c += 1
                else:
                    temp.extend([str(cur_c), cur_v])
                    cur_c, cur_v = 1, v

            temp.extend([str(cur_c), cur_v])
            next_say = "".join(temp)
            i += 1
        return next_say
        
            
        