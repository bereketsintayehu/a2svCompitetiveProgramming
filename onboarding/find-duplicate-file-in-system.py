class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        group = defaultdict(list)

        for path in paths:
            parts = path.split()
            for i in range(1, len(parts)):
                opening = parts[i].find('(')
                key = parts[0] + '/' + parts[i][:opening]
                val = parts[i][opening + 1:-1]

                files[key] = val
                group[val].append(key)
        
        return [path for path in group.values() if len(path) > 1]

        