class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hmap = collections.defaultdict(int)
        
        for d in cpdomains:
            count, domain = d.split(" ")
            sub_domain = domain.split(".")
            for i in range(len(sub_domain)):
                hmap[".".join(sub_domain[i:])] += int(count)
        
        return [str(v)+ " " + k for k, v in hmap.items()]
    
        
                
                
        
        
        