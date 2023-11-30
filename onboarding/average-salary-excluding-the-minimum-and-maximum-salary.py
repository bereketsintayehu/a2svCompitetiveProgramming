class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = 1000
        minSalary = 10 ** 6
        salarySum = 0

        for sal in salary:
            maxSalary = max(maxSalary, sal)
            minSalary = min(minSalary, sal)
            salarySum += sal
            
        return (salarySum - minSalary - maxSalary)/(len(salary) - 2)