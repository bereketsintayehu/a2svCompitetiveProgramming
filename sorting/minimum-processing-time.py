class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        return max([prt + tt for prt, tt in zip(sorted(tasks, reverse=True), sorted(processorTime * 4))])
