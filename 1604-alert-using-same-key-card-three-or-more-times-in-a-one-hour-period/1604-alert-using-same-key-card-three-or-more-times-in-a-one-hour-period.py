from datetime import datetime

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hmap = collections.defaultdict(list)
        
        for name, time in zip(keyName, keyTime):
            time = time.split(":")
            time = int(time[0]) * 60 + int(time[1])
            hmap[name].append(time)
        
        result = []
        
        for name, times in hmap.items():
            if len(times) < 3:
                continue
            times.sort()
            print(times)
            for i in range(1, len(times) - 1):
                if (times[i + 1] - times[i - 1]) <= 60:
                    result.append(name)
                    break
                
        return sorted(result)
                
                
            