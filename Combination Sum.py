'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        candidates.sort()
        def findCandidates(target,index,temp,output):
            if target == 0:
                output.append(temp)
                return
            if target < 0:
                return
            for i in range(index,len(candidates)):
                findCandidates(target-candidates[i],i,temp+[candidates[i]],output)
        findCandidates(target,0,[],output)
        return output
        
