class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = defaultdict(int)

        for cp in cpdomains:
            visit, domain = cp.split()
            subdomain = domain.split('.')
            print(subdomain)
            for i in range(1, len(subdomain)+1):
                ans['.'.join(subdomain[-i:])] += int(visit)
        
        return [f"{value} {key}" for key, value in ans.items()]
        
