class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for path in paths:
            parts = path.split()
            for i in range(1, len(parts)):
                fileName, content = parts[i].split('(')
                group[content].append(parts[0] + '/' + fileName)
        
        return [fil for fil in group.values() if len(fil) > 1]

        
